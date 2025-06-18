# src/pipeline.py
import logging
from typing import List
from src.task import Task


class Pipeline:
    def __init__(self, tasks: List[Task]):
        self.tasks = tasks

    def run(self):
        """
        Executa a lista de tarefas em sequência. O pipeline é interrompido
        se qualquer uma das tarefas levantar uma exceção.
        """
        data = None  # Dados iniciais são nulos
        for task in self.tasks:
            try:
                # O resultado de uma tarefa é a entrada para a próxima
                data = task.execute(data)
            except Exception:
                logging.error(
                    f"Pipeline interrompido por erro na tarefa '{task.name}'."
                )
                break  # Encerra o pipeline
