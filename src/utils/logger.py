"""Configure logger and provide a decorator for task logging."""

import logging
import os
import time
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "execucao.log")

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
)


def _write_to_log_file(message):
    """Write a message to the log file."""
    with open(LOG_FILE, "a", encoding="UTF-8") as file:
        file.write(f"{message}\n")


def log_task(func):
    """Log the start, success, and failure of a task execution."""

    def wrapper(task_instance, *args, **kwargs):
        task_name = task_instance.name if hasattr(task_instance, "name") else str(task_instance)
        logging.info(f"Executando tarefa: {task_name}")
        start_time = time.time()

        try:
            result = func(task_instance, *args, **kwargs)
            endtime = time.time()
            duration = endtime - start_time

            logging.info(f"Tarefa {task_name} finalizada com sucesso.\n")

            log_message = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {task_name}: OK -{duration:.3f}s"
            _write_to_log_file(log_message)

            return result
        except Exception as e:
            endtime = time.time()
            duration = endtime - start_time

            error_message = f"Erro na tarefa {task_name}: {e}"
            logging.error(f"{error_message}\n")

            log_message = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {task_name}: ERRO - {duration:.3f}s - {e}"
            _write_to_log_file(log_message)

            raise

    return wrapper
