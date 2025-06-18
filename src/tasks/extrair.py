# src/tasks/extrair.py
import pandas as pd
from faker import Faker
from src.task import Task
from src.utils.logger import log_task
import os


class ExtrairTask(Task):
    def __init__(self):
        super().__init__(name="Extrair")
        self.input_path = "data/input.csv"

    def _generate_data(self, num_rows: int):
        """Gera dados sintéticos para o projeto."""
        print(
            f"Arquivo {self.input_path} não encontrado. Gerando {num_rows} novos registros..."
        )
        fake = Faker("pt_BR")
        data = {
            "id": range(1, num_rows + 1),
            "nome": [fake.name() for _ in range(num_rows)],
            "email": [fake.email() for _ in range(num_rows)],
            "valor_compra": [
                fake.pydecimal(left_digits=4, right_digits=2, positive=True)
                for _ in range(num_rows)
            ],
        }
        df = pd.DataFrame(data)
        os.makedirs(os.path.dirname(self.input_path), exist_ok=True)
        df.to_csv(self.input_path, index=False, sep=";", decimal=",")
        print("Geração de dados concluída.")

    @log_task
    def execute(self, data=None) -> pd.DataFrame:
        """
        Gera e extrai os dados. Se o arquivo não existir, ele é criado com 10.000 linhas.
        Depois, os dados são lidos e retornados.
        """
        # Gera o arquivo de dados se ele não existir
        if not os.path.exists(self.input_path):
            self._generate_data(10000)

        # Extrai os dados do arquivo
        df = pd.read_csv(self.input_path, sep=";", decimal=",")
        return df
