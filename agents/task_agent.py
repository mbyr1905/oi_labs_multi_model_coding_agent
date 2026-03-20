import json
import time
import re
from graph.state import AgentState
from llm.groq_llm import get_llm
from utils.logger import logger
from utils.mlflow_tracker import log_param, log_metric, log_text, log_error
from utils.extract_json import extract_json

def task_agent(state: AgentState):
    try:
        start_time = time.time()
        logger.info("TASK_AGENT | Started")
        llm = get_llm()
        architecture_plan = state["architecture_plan"]
        log_param("task_agent_model", "llama-3.3-70b-versatile")
        prompt = f"""
        You are a senior software engineer.

        Break down the architecture into actionable development tasks.

        ARCHITECTURE:
        {architecture_plan}

        Return ONLY valid JSON:

        {{
        "backend_tasks": [],
        "database_tasks": [],
        "frontend_tasks": [],
        "integration_tasks": []
        }}

        Rules:
        - Tasks must be actionable and implementable
        - Do not include explanation and reasoning in the output, include only JSON
        """

        log_text(prompt, "task_agent_prompt.txt")

        res = llm.invoke(prompt)
        output = res.content
        logger.debug(f"TASK_AGENT | Raw output: {output}")
        log_text(output, "task_agent_response.txt")

        if not output or output.strip() == "":
            raise ValueError("LLM returned empty output")

        task_plan = extract_json(output)

        logger.debug(f"TASK_AGENT | Parsed task_plan: {task_plan}")
        state["task_plan"] = task_plan
        runtime = time.time() - start_time
        log_metric("task_agent_runtime", runtime)
        logger.info("TASK_AGENT | Completed")

        return state

    except Exception as e:
        logger.error(f"TASK_AGENT | ERROR: {str(e)}")
        log_error(e)
        raise e