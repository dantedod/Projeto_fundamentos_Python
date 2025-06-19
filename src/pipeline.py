# src/pipeline.py
"""Módulo que define a classe Pipeline para execução sequencial de tarefas."""

import logging
from typing import List

from src.task import Task


class Pipeline:
    """
    Classe que representa um pipeline de execução de tarefas.

    Executa uma lista de tarefas sequencialmente, interrompendo caso
    alguma tarefa lance uma exceção.
    """

    def __init__(self, tasks: List[Task]):
        """
        Inicializa o pipeline com uma lista de tarefas.

        Args:
            tasks (List[Task]): Lista de objetos Task a serem executados.
        """
        self.tasks = tasks

    def run(self):
        """
        Executa a lista de tarefas em sequência.

        O pipeline é interrompido se qualquer
                uma das tarefas levantar uma exceção.
        """
        data = None  # Dados iniciais são nulos
        for task in self.tasks:
            try:
                # O resultado de uma tarefa é a entrada para a próxima
                data = task.execute(data)
            except Exception:
                logging.error("Pipeline interrompido por erro na tarefa '%s'.", task.name)
                break  # Encerra o pipeline
