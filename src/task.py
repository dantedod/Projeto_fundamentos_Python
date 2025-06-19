# src/task.py
"""
Módulo que define a classe base Task para tarefas do pipeline.

Esta classe abstrata serve como base para todas as tarefas do pipeline,
definindo a estrutura padrão que uma tarefa deve seguir.
"""

from abc import ABC, abstractmethod


class Task(ABC):
    """
    Classe base para todas as tarefas.

    Define a estrutura padrão que uma tarefa deve seguir.
    """

    def __init__(self, name: str):
        """
        Inicializa a tarefa com um nome.

        Args:
            name (str): Nome da tarefa.
        """
        self.name = name

    @abstractmethod
    def execute(self, data=None):
        """
        Método abstrato que deve ser implementado por todas as subclasses.

        Este método é o ponto de entrada da lógica da tarefa.

        Args:
            data: Dados de entrada para a tarefa.

        Returns:
            Dados processados pela tarefa.
        """
        pass
