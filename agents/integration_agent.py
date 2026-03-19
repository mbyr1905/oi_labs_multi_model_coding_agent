import json
import time
import re

from graph.state import AgentState
from llm.groq_llm import get_llm
from utils.logger import logger
from utils.mlflow_tracker import log_param, log_metric, log_text, log_error

def _normalize_json_like(text: str) -> str:
    """Try to normalize common non-strict JSON output into valid JSON."""
    # Remove trailing commas (e.g., after the last item in objects/arrays)
    text = re.sub(r",\s*([}\]])", r"\1", text)

    # Quote unquoted object keys: {key: ...} -> {"key": ...}
    text = re.sub(r"(?P<prefix>[{,\s])(?P<key>[A-Za-z_][A-Za-z0-9_]*)\s*:\s*", r"\g<prefix>\"\g<key>\": ", text)

    # Convert single-quoted strings to double-quoted strings.
    # This is a best-effort transformation and may not be perfect for all edge cases.
    text = re.sub(r"(?<![\\\"])'((?:\\.|[^'\\])*)'", r'"\1"', text)

    return text


def extract_json(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    match = re.search(r"```json(.*?)```", text, re.DOTALL)
    if match:
        text = match.group(1).strip()

    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError(f"No JSON found. Output:\n{text}")

    json_str = match.group().strip()

    # First try parsing pretty-printed JSON as-is.
    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        pass

    # Try to normalize common non-strict JSON output from LLMs.
    normalized = _normalize_json_like(json_str)
    return json.loads(normalized)


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

        {{
        "files": [
            {{
            "path": "",
            "content": ""
            }}
        ]
        }}

         ========================
        STRICT RULES
        ========================
        - Do NOT include explanations
        - Do NOT include markdown (no ```json)
        - Do NOT include text outside JSON
        - Ensure JSON is valid and parsable
        - Ensure all files have proper content
        - Output STRICTLY valid JSON 
        """

        log_text(prompt, "integration_prompt.txt")

        res = llm.invoke(prompt)
        output = res.content

        logger.debug(f"INTEGRATION_AGENT | Raw output: {output}")
        log_text(output, "integration_response.txt")

        if not output.strip():
            raise ValueError("Empty output")

        integration_code = extract_json(output)

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