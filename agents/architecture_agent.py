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

    raise ValueError("No valid JSON found in LLM output")


def architecture_agent(state: AgentState):

    try:

        start_time = time.time()
        logger.info("ARCHITECTURE_AGENT | Started")
        llm = get_llm()
        system_spec = state["system_spec"]
        log_param("architecture_model", "llama-3.3-70b-versatile")
        prompt = f"""
            You are a senior software architect.

            Based on the system specification below, design a complete system architecture.

            SYSTEM SPEC:
            {system_spec}

            Return JSON with:

            {{
            "architecture_type": "",
            "backend": {{
                "framework": "",
                "modules": []
            }},
            "database": {{
                "tables": []
            }},
            "frontend": {{
                "framework": "",
                "pages": []
            }},
            "apis": []
            }}
            Prefer MONOLITH architecture unless explicitly required.
            Rules:
            - Do not invent features outside system_spec
            - Keep architecture scalable
            - Output valid JSON only
            """
        log_text(prompt, "architecture_prompt.txt")
        response = llm.invoke(prompt)
        output = response.content
        logger.debug(f"Architecture Plan| Raw output: {output}")
        if not output or output.strip() == "":
            raise ValueError("LLM returned empty output")
        log_text(output, "architecture_response.txt")
        architecture_plan = extract_json(output)
        state["architecture_plan"] = architecture_plan
        runtime = time.time() - start_time
        log_metric("architecture_agent_runtime", runtime)
        logger.debug(f"Architecture Plan: {state.get('architecture_plan')}")
        logger.info("ARCHITECTURE_AGENT | Completed")
        return state

    except Exception as e:

        logger.error(f"ARCHITECTURE_AGENT | ERROR: {str(e)}")
        log_error(e)
        raise e