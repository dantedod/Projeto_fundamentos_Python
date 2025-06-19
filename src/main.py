# src/main.py
"""
Módulo principal para execução do pipeline.

Define e executa a sequência de tarefas do pipeline.
"""

import os

from src.pipeline import Pipeline
from src.tasks.carregar import CarregarTask
from src.tasks.extrair import ExtrairTask
from src.tasks.transformar import TransformarTask


def main():
    """
    Ponto de entrada do script.

    Define o pipeline com as tarefas na ordem correta e o executa.
    """
    log_file = "logs/execucao.log"
    if os.path.exists(log_file):
        open(log_file, "w").close()

    pipeline_tasks = [ExtrairTask(), TransformarTask(), CarregarTask()]

    pipeline = Pipeline(tasks=pipeline_tasks)
    pipeline.run()


if __name__ == "__main__":
    main()
