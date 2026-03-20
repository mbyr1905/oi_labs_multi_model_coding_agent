import json
import time
import re

from graph.state import AgentState
from llm.groq_llm import get_llm
from utils.logger import logger
from utils.mlflow_tracker import log_param, log_metric, log_text, log_error
import json
import re
import ast
from utils.extract_json import extract_json

def debug_agent(state: AgentState):
    try:
        start_time = time.time()
        logger.info("DEBUG_AGENT | Started")

        llm = get_llm(temperature=0)
        backend = state.get("backend_code")
        frontend = state.get("frontend_code")
        integration = state.get("integration_code")

        log_param("debug_model", "llama-3.3-70b-versatile")

        prompt = f"""
        You are a senior software engineer responsible for fixing generated code.
        
        ========================
        BACKEND CODE
        ========================
        {backend}
        
        ========================
        FRONTEND CODE
        ========================
        {frontend}
        
        ========================
        INTEGRATION CODE
        ========================
        {integration}
        
        ========================
        TASK
        ========================
        Analyze and fix issues:
        
        - Fix syntax errors
        - Fix import paths
        - Fix API endpoint mismatches
        - Fix missing dependencies
        - Ensure frontend works with backend
        - Improve code quality slightly
        
        ========================
        IMPORTANT RULES
        ========================
        - DO NOT regenerate entire project
        - ONLY modify broken or incorrect parts
        - Keep changes minimal
        - Preserve structure
        - Do NOT remove working code
        ========================
        STRICT RULES
        ========================
        - Do NOT include explanations
        - Do NOT include markdown (no ```json)
        - Do NOT include text outside JSON
        - Ensure JSON is valid and parsable
        - Ensure all files have proper content
        - Output STRICTLY valid JSON 
        - Escape newlines properly
        - Output valid JSON only
        ========================
        OUTPUT FORMAT
        ========================
        Return ONLY changed files:
        
        {{
            "files": [
            {{
                "path": "",
                "content": ""
            }}
            ]
        }}
        """

        log_text(prompt, "debug_prompt.txt")

        res = llm.invoke(prompt)
        output = res.content

        logger.debug(f"DEBUG_AGENT | Raw output: {output}")
        log_text(output, "debug_response.txt")

        if not output.strip():
            raise ValueError("Empty output")

        fixed_code = extract_json(output)
        state["fixed_code"] = fixed_code
        state["code_key"] = "fixed_code"
        state["output_dir"] = "src_code"
        state["write_mode"] = "overwrite"
        runtime = time.time() - start_time
        log_metric("debug_runtime", runtime)

        logger.info(f"DEBUG_AGENT | Completed")

        return state

    except Exception as e:
        logger.error(f"DEBUG_AGENT | ERROR: {str(e)}")
        log_error(e)
        raise e