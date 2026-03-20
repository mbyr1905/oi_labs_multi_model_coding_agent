import json
import time
import re

from graph.state import AgentState
from llm.groq_llm import get_llm
from utils.logger import logger
from utils.mlflow_tracker import log_metric, log_param, log_text, log_error
from utils.extract_json import extract_json


def evaluation_agent(state: AgentState):
    try:
        start_time = time.time()
        logger.info("EVALUATION_AGENT | Started")

        llm = get_llm(temperature=0) 

        backend = state.get("backend_code")
        frontend = state.get("frontend_code")
        integration = state.get("integration_code")

        retry_count = state.get("retry_count", 0)

        log_param("evaluation_model", "llama-3.3-70b-versatile")

        prompt = f"""
        You are a senior code reviewer.

        Evaluate the generated system.

        ========================
        BACKEND
        ========================
        {backend}

        ========================
        FRONTEND
        ========================
        {frontend}

        ========================
        INTEGRATION
        ========================
        {integration}

        ========================
        TASK
        ========================

        Evaluate based on:

        - Code correctness
        - API consistency
        - Integration correctness
        - Structure quality

        ========================
        OUTPUT FORMAT
        ========================

        {{
        "score": 0-100,
        "issues": ["..."],
        "decision": "good" or "bad"
        }}

        Rules:
        - score > 80 → good
        - else → bad
        - return ONLY JSON
        """

        log_text(prompt, "evaluation_prompt.txt")

        res = llm.invoke(prompt)
        output = res.content

        logger.debug(f"EVALUATION_AGENT | Raw output: {output}")
        log_text(output, "evaluation_response.txt")

        evaluation = extract_json(output)
        state["evaluation"] = evaluation
        runtime = time.time() - start_time
        log_metric("evaluation_runtime", runtime)
        log_metric("evaluation_score", evaluation.get("score", 0))

        logger.info(f"EVALUATION_AGENT | Score: {evaluation.get('score')}")
        state["retry_count"] = retry_count + 1
        return state
    except Exception as e:
        logger.error(f"EVALUATION_AGENT | ERROR: {str(e)}")
        log_error(e)
        raise e