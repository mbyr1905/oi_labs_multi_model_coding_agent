import json
import time
import re

from graph.state import AgentState
from llm.groq_llm import get_llm
from utils.logger import logger
from utils.mlflow_tracker import log_param, log_metric, log_text, log_error
from utils.extract_json import extract_json
from utils.guardrails import validate_code_structure

def integration_agent(state: AgentState):
    try:
        start_time = time.time()
        logger.info(f"INTEGRATION_AGENT | Started")

        llm = get_llm()

        system_spec = state["system_spec"]
        architecture = state["architecture_plan"]
        backend = state["backend_code"]
        frontend = state["frontend_code"]

        log_param("integration_model", "llama-3.3-70b-versatile")

        prompt = f"""
        You are a senior full-stack engineer.

        Your job is to CONNECT frontend with backend.

        ========================
        SYSTEM SPEC
        ========================
        {system_spec}

        ========================
        ARCHITECTURE
        ========================
        {architecture}

        ========================
        BACKEND (REFERENCE)
        ========================
        {backend}

        ========================
        FRONTEND (REFERENCE)
        ========================
        {frontend}

        ========================
        TASK
        ========================
        - Replace dummy data in frontend with real API calls
        - Create API utility layer (lib/api.ts)
        - Ensure API endpoints match backend routes
        - Add loading + error handling
        - Keep UI unchanged as much as possible

        ========================
        RULES
        ========================
        - DO NOT regenerate entire frontend
        - ONLY modify necessary files
        - Keep code minimal and clean
        - Use fetch (preferred)
        - Follow Next.js best practices

        ========================
        OUTPUT FORMAT
        ========================
        Return ONLY valid JSON:
        
        STRICT VALIDITY RULES:
        - Do NOT use non-existent libraries
        - Do NOT invent APIs
        - Use only real Python / FastAPI / React constructs
        - Ensure imports are valid
        
        ========================
        STRICT RULES
        ========================
        - Do NOT include explanations
        - Do NOT include markdown (no ```json)
        - Do NOT include text outside JSON
        - Ensure JSON is valid and parsable
        - Ensure all files have proper content
        - Output STRICTLY valid JSON 

        {{
        "files": [
            {{
            "path": "",
            "content": ""
            }}
        ]
        }}
        """

        log_text(prompt, "integration_prompt.txt")

        res = llm.invoke(prompt)
        output = res.content

        logger.debug(f"INTEGRATION_AGENT | Raw output: {output}")
        log_text(output, "integration_response.txt")

        if not output.strip():
            raise ValueError("Empty output")

        integration_code = extract_json(output)
        issues = validate_code_structure(integration_code)
        if issues:
            log_error(f"Guardrail issues: {issues} for integration code")
            logger.error(f"INTEGRATION_AGENT | Guardrail issues: {issues} for integration code")
            raise ValueError(f"Guardrail failed: {issues} for integration code")
        runtime = time.time() - start_time
        log_metric("integration_runtime", runtime)

        logger.info(f"INTEGRATION_AGENT | Completed")

        return {
            **state,
            "integration_code": integration_code,
            "code_key": "integration_code",
            "output_dir": "src_code/frontend"
        }

    except Exception as e:
        logger.error(f"INTEGRATION_AGENT | ERROR: {str(e)}")
        log_error(e)
        raise e