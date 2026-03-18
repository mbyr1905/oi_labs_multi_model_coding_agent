import json
import os
import re
import time
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from groq import Groq
from graph.state import AgentState
from utils.logger import logger 
from utils.mlflow_tracker import log_param, log_metric, log_text, log_error
from llm.groq_llm import get_llm


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

def requirement_agent(state: AgentState):
    try:
        start_time = time.time()
        llm = get_llm()
        logger.info("Starting requirement_agent")
        prd_text = state["prd_text"]
        figma_path = state.get("figma_image_path")
        log_param("requirements_agent_model", "llama-3.3-70b-versatile")
        figma_context = ""
        if figma_path and os.path.exists(figma_path):
            logger.info(f"Figma design detected: {figma_path}")
            figma_context = "A UI design image is provided for UI reference.Extract possible pages and UI components."
        else:
            logger.info("No figma image provided")

        prompt = f"""
            You are a senior system architect.

            Analyze the product requirements and optional design input.

            PRD:
            {prd_text}

            {figma_context}

            Return ONLY valid JSON.


            {{
            "frontend": "",
            "backend": "",
            "database": "",
            "features": [],
            "pages": [],
            "components": []
            }}

            Rules:
            - Only extract features mentioned in PRD
            - Output valid JSON
            Do NOT include explanation.
            Do NOT include markdown.
        """
        log_text(prompt, "requirement_agent_prompt.txt")
        res = llm.invoke(prompt)
        output = res.content
        log_text(output, "requirement_agent_response.txt")
        system_spec = extract_json(output)

        state["system_spec"] = system_spec

        state["pages"] = system_spec["pages"]

        state["components"] = system_spec["components"]
        runtime = time.time() - start_time
        
        logger.debug(f"Parsed system_spec: {system_spec}")
        
        log_metric("requirement_agent_runtime", runtime)
        log_metric("pages_detected", len(state["pages"]))
        log_metric("components_detected", len(state["components"]))
        
        logger.info(f"Completed requirement_agent")
        return state
    except Exception as e:
        logger.error(f"Error in requirement_agent: {e}")
        log_error(e)
        raise e