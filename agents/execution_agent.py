import subprocess
import time

from graph.state import AgentState
from utils.logger import logger
from utils.mlflow_tracker import log_metric, log_error


STEP = "EXECUTION_AGENT"


def execution_agent(state: AgentState):
    try:
        start_time = time.time()
        logger.info(f"{STEP} | Started")

        # Try running backend app
        result = subprocess.run(
            ["python", "src_code/backend/main.py"],
            capture_output=True,
            text=True,
            timeout=10
        )

        errors = result.stderr

        success = result.returncode == 0
        state['execution_result'] = {
            "success": success,
            "errors": errors
        }
        logger.info(f"{STEP} | Success: {success}")

        return state
    except Exception as e:
        logger.error(f"{STEP} | ERROR: {str(e)}")
        log_error(e)
        raise e