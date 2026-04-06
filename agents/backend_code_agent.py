import json
import time
import re

from graph.state import AgentState
from llm.groq_llm import get_llm
from utils.extract_json import extract_json
from utils.logger import logger
from utils.guardrails import validate_code_structure
from utils.mlflow_tracker import log_param, log_metric, log_text, log_error

def backend_code_agent(state: AgentState):
    try:
        start_time = time.time()
        logger.info("BACKEND_CODE_AGENT | Started")

        llm = get_llm()
        backend_tasks = state["task_plan"]["backend_tasks"]

        log_param("backend_code_model", "mistral:latest")
        backend_previous_code = state.get("backend_code", "No previous code")
        frontend_previous_code = state.get("frontend_code", "No previous code")
        evaluation = state.get("evaluation", "No evaluation yet")
        execution_result = state.get("execution_result", "No execution result yet")
        prompt = f"""
            You are a senior backend engineer.

            Generate production-ready FastAPI backend code, Code should also be generated.

            SYSTEM SPEC:
            {state["system_spec"]}

            ARCHITECTURE:
            {state["architecture_plan"]}

            BACKEND TASKS:
            {backend_tasks}
            
            ========================
            PREVIOUS BACKEND CODE
            ========================
            {backend_previous_code}
            
            ========================
            PREVIOUS FRONTEND CODE
            ========================
            {frontend_previous_code}
            
            ========================
            EXECUTION RESULT
            ========================
            {execution_result}

            ========================
            EVALUATION FEEDBACK
            ========================
            {evaluation}
            
            IMPORTANT:
            - If previous code exists:
                - DO NOT regenerate everything
                - ONLY fix backed_code issues based on execution and evaluation
                - Preserve working code
            
            
            Requirements:
            - Use FastAPI best practices
            - Use modular architecture
            - Generate the code in each of the code file that youcreated
            - Follow the architecture strictly
            - Include:
                - models (SQLAlchemy)
                - schemas (Pydantic)
                - routes (APIs)
                - service layer
            - Ensure all modules are connected properly
            - Use clean folder structure
            
            Return ONLY valid JSON:
            ========================
            Strict Rules:
            ========================
            - No explanation
            - No markdown
            - Do NOT include text outside JSON
            - Ensure JSON is valid and parsable
            - Ensure all files have proper content
            - Output STRICTLY valid JSON  
            - Should be extracted using json extract, skip quotes, new lines and all other cases where jason will be failing
            ========================
            SPECIAL FILE RULES
            ========================
            - Create ONE common requirements.txt file
            - The file path MUST be: ../requirements.txt
            - This ensures it is created inside src_code/backend folder but can be accessed by both frontend and backend, and no other folders other than this
            - Do NOT create requirements.txt inside backend folder
            STRICT VALIDITY RULES:
            - Do NOT use non-existent libraries
            - Do NOT invent APIs
            - Use only real Python / FastAPI / React constructs
            - Ensure imports are valid
            
            {{
            "files": [
            {{
                "path": "",
                "content": ""
            }}
            ]
            }}
            """

        log_text(prompt, "backend_code_prompt.txt")

        res = llm.invoke(prompt)
        output = res.content

        logger.debug(f"BACKEND_CODE_AGENT | Raw output: {output}")

        log_text(output, "backend_code_response.txt")

        if not output or output.strip() == "":
            raise ValueError("LLM returned empty output")

        backend_code = extract_json(output)
        issues = validate_code_structure(backend_code)
        if issues:
            log_error(f"Guardrail issues: {issues} for backend code")
            logger.error(f"BACKEND_CODE_AGENT | Guardrail issues: {issues} for backend code")
            raise ValueError(f"Guardrail failed: {issues} for backend code")
        state["backend_code"] = backend_code
        logger.debug(f"BACKEND_CODE_AGENT | Parsed backend_code")

        runtime = time.time() - start_time
        log_metric("backend_code_runtime", runtime)

        logger.info("BACKEND_CODE_AGENT | Completed")
        state["code_key"] = "backend_code"
        state["output_dir"] = "src_code/backend"

        return state

    except Exception as e:
        logger.error(f"BACKEND_CODE_AGENT | ERROR: {str(e)}")
        log_error(e)
        raise e