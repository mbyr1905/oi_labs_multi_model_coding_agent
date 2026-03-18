import json
import time
import re

from graph.state import AgentState
from llm.groq_llm import get_llm
from utils.logger import logger
from utils.mlflow_tracker import log_param, log_metric, log_text, log_error

def extract_json(text):
    try:
        return json.loads(text)
    except:
        pass

    match = re.search(r"```json(.*?)```", text, re.DOTALL)
    if match:
        return json.loads(match.group(1).strip())

    match = re.search(r"\{.*?\}", text, re.DOTALL)
    if match:
        return json.loads(match.group())

    raise ValueError(f"No valid JSON found. Output:\n{text}")


def backend_code_agent(state: AgentState):
    try:
        start_time = time.time()
        logger.info("BACKEND_CODE_AGENT | Started")

        llm = get_llm()

        architecture = state["architecture_plan"]
        backend_tasks = state["task_plan"]["backend_tasks"]

        log_param("backend_code_model", "llama-3.3-70b-versatile")

        prompt = f"""
            You are a senior backend engineer.

            Generate production-ready FastAPI backend code.

            ARCHITECTURE:
            {architecture}

            TASKS:
            {backend_tasks}

            Requirements:
            - Use FastAPI best practices
            - Use modular structure
            - Include:
                - models
                - schemas
                - routes
                - service layer

            Return ONLY valid JSON:

            {{
            "files": [
            {{
                "path": "",
                "content": ""
            }}
            ]
            }}

            Rules:
            - No explanation
            - No markdown
            """

        log_text(prompt, "backend_code_prompt.txt")

        res = llm.invoke(prompt)
        output = res.content

        logger.debug(f"BACKEND_CODE_AGENT | Raw output: {output}")

        log_text(output, "backend_code_response.txt")

        if not output or output.strip() == "":
            raise ValueError("LLM returned empty output")

        backend_code = extract_json(output)
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