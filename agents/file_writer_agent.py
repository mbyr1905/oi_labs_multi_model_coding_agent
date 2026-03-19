import time

from graph.state import AgentState
from utils.logger import logger
from utils.mlflow_tracker import log_metric, log_error
from utils.file_writer import write_files



def file_writer_agent(state: AgentState):
    try:
        start_time = time.time()
        logger.info("FILE_WRITER_AGENT | Started")

        code_key = state.get("code_key") 
        base_dir = state.get("output_dir", "generated_code")
        mode = state.get("write_mode", "overwrite")
        if not code_key:
            raise ValueError("code_key not provided in state")

        code_data = state.get(code_key)

        if not code_data or "files" not in code_data:
            raise ValueError(f"No valid files found in {code_key}")

        created_files = write_files(base_dir, code_data["files"], mode=mode)
        logger.info(f"FILE_WRITER_AGENT | Created: {len(result['created'])}, Updated: {len(result['updated'])}, Mode: {mode}")
        runtime = time.time() - start_time
        log_metric("file_writer_runtime", runtime)
        logger.info(f"FILE_WRITER_AGENT | Completed")
        return state

    except Exception as e:
        logger.error(f"FILE_WRITER_AGENT | ERROR: {str(e)}")
        log_error(e)
        raise e