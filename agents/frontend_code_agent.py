import json
import time
import re
from graph.state import AgentState
from llm.groq_llm import get_llm
from utils.logger import logger
from utils.mlflow_tracker import log_param, log_metric, log_text, log_error
from utils.extract_json import extract_json
from utils.guardrails import validate_code_structure


def frontend_code_agent(state: AgentState):
    try:
        start_time = time.time()
        logger.info("FRONTEND_CODE_AGENT | Started")

        llm = get_llm() 
        
        frontend_tasks = state["task_plan"]["frontend_tasks"]
        components = state["components"]
        pages = state["pages"]

        log_param("frontend_code_model", "llama-3.3-70b-versatile")

        prompt = f"""
            You are a senior frontend engineer building a production-ready e-commerce web application.

            Your task is to generate a complete frontend using Next.js (App Router), TypeScript, and Tailwind CSS.

            ========================
            SYSTEM SPECIFICATION
            ========================
            {state["system_spec"]}

            ========================
            ARCHITECTURE PLAN
            ========================
            {state["architecture_plan"]}
            
            ========================
            BACKEND CODE
            ========================
            {state["backend_code"]}

            ========================
            FRONTEND TASKS
            ========================
            {frontend_tasks}

            ========================
            PAGES TO BUILD
            ========================
            {pages}

            ========================
            UI COMPONENTS
            ========================
            {components}

            ========================
            REQUIREMENTS
            ========================
            - Use Next.js (App Router structure)
            - Use TypeScript (.tsx files)
            - Use Tailwind CSS for styling, also refer to mastercard design system for reference
            - Follow modular and scalable folder structure

            ========================
            IMPLEMENTATION RULES
            ========================
            - Create reusable components (Navbar, ProductCard, etc.)
            - Each page must be properly structured and functional
            - Use realistic dummy data where backend integration is not available
            - Maintain consistency with backend APIs (naming, routes, structure)
            - Check the backend code and create the UI so that they should be able to integrate seamlessly later
            - Keep components clean and separated
            - Use proper imports and exports
            - Avoid hardcoding everything in one file
            - Follow best practices for React and Next.js

            ========================
            OUTPUT FORMAT
            ========================
            Return ONLY valid JSON:
            ========================
            STRICT RULES
            ========================
            - Do NOT include explanations
            - Do NOT include markdown (no ```json)
            - Do NOT include text outside JSON
            - Ensure JSON is valid and parsable
            - Ensure all files have proper content
            - Output STRICTLY valid JSON 
            
            ========================
            SPECIAL FILE RULES
            ========================
            - Create ONE common requirements.txt file
            - The file path MUST be: ../requirements.txt
            - This ensures it is created inside src_code/
            - Do NOT create requirements.txt inside frontend folder
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

        log_text(prompt, "frontend_code_prompt.txt")

        res = llm.invoke(prompt)
        output = res.content

        logger.debug(f"FRONTEND_CODE_AGENT | Raw output: {output}")

        log_text(output, "frontend_code_response.txt")

        if not output or output.strip() == "":
            raise ValueError("LLM returned empty output")

        frontend_code = extract_json(output)
        issues = validate_code_structure(frontend_code)
        if issues:
            log_error(f"Guardrail issues: {issues} for frontend code")
            logger.error(f"FRONTEND_CODE_AGENT | Guardrail issues: {issues} for frontend code")
            raise ValueError(f"Guardrail failed: {issues} for frontend code")
        state["frontend_code"] = frontend_code
        runtime = time.time() - start_time
        log_metric("frontend_code_runtime", runtime)

        logger.info(f"FRONTEND_CODE_AGENT | Completed")
        state["code_key"] = "frontend_code"
        state["output_dir"] = "src_code/frontend"
        
        return state

    except Exception as e:
        logger.error(f"FRONTEND_CODE_AGENT | ERROR: {str(e)}")
        log_error(e)
        raise e