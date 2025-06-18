# src/main.py
from src.pipeline import Pipeline
from src.tasks.extrair import ExtrairTask
from src.tasks.transformar import TransformarTask
from src.tasks.carregar import CarregarTask
import os


def main():
    """
    Ponto de entrada do script.
    Define o pipeline com as tarefas na ordem correta e o executa.
    """

    # Apaga o log antigo para uma execução limpa
    log_file = "logs/execucao.log"
    if os.path.exists(log_file):
        open(log_file, "w").close()

    # Define a sequência de tarefas
    pipeline_tasks = [ExtrairTask(), TransformarTask(), CarregarTask()]

    # Cria e executa o pipeline
    pipeline = Pipeline(tasks=pipeline_tasks)
    pipeline.run()


if __name__ == "__main__":
    main()
