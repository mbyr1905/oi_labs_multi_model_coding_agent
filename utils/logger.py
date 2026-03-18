import logging
import os


LOG_DIR = "logs"
LOG_FILE = "logs/pipeline.log"


os.makedirs(LOG_DIR, exist_ok=True)


logger = logging.getLogger("ai_pipeline")

logger.setLevel(logging.DEBUG)


formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)


file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")

file_handler.setFormatter(formatter)


console_handler = logging.StreamHandler()

console_handler.setFormatter(formatter)


if not logger.handlers:

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def log_step(step_name, message):

    logger.info(f"{step_name} | {message}")