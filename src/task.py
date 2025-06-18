# src/task.py
from abc import ABC, abstractmethod


class Task(ABC):
    """
    Classe base para todas as tarefas. Define a estrutura
    padrão que uma tarefa deve seguir.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def execute(self, data=None):
        """
        Método abstrato que deve ser implementado por todas as subclasses.
        É o ponto de entrada da lógica da tarefa.
        """
        pass
