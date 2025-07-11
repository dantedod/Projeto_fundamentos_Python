"""Tarefa de extração de dados.

Gera dados sintéticos ou lê dados existentes
do arquivo CSV especificado em `input_path`.
"""

import os
import random

import pandas as pd
from faker import Faker

from src.task import Task
from src.utils.logger import log_task


class ExtrairTask(Task):
    """Classe que implementa a tarefa de extração de dados.

    Essa tarefa gera dados sintéticos caso o arquivo
    de entrada não exista, ou lê os dados existentes do CSV.
    """

    def __init__(self):
        """Inicializa a tarefa com o nome e o caminho do arquivo de entrada."""
        super().__init__(name="Extrair")
        self.input_path = "data/input.csv"

    def _generate_data(self, num_rows: int):
        """Gera dados sintéticos para o projeto."""
        print(f"Arquivo {self.input_path} não encontrado. Gerando {num_rows} novos registros...")
        fake = Faker("pt_BR")

        produtos = [
            "Smartphone",
            "Notebook",
            "TV",
            "Fone de Ouvido",
            "Mouse",
            "Teclado",
            "Monitor",
            "Webcam",
            "Microfone",
            "Impressora Multifuncional",
            "Headset Gamer",
            "Mousepad Gamer",
            "Cadeira Gamer",
            "Caixa de Som Bluetooth",
            "HD Externo",
            "Pen Drive",
            "Cartão de Memória",
            "Carregador Portátil (Power Bank)",
            "Placa de Vídeo (GPU)",
            "Processador (CPU)",
            "Memória RAM",
            "SSD 1TB",
            "SSD 512GB",
            "Placa-Mãe",
            "Fonte de Alimentação (PSU)",
            "Gabinete",
            "Cooler para Processador",
            "Smartwatch",
            "Smartband",
            "Tablet",
            "Leitor de E-book",
            "Assistente Virtual",
            "Roteador Wi-Fi",
            "Repetidor de Sinal",
            "Nobreak (UPS)",
            "Projetor",
            "Cabo HDMI",
            "Cabo USB-C",
            "Adaptador DisplayPort",
            "Filtro de Linha",
        ]

        data = {
            "id": range(1, num_rows + 1),
            "nome": [fake.name() for _ in range(num_rows)],
            "email": [fake.email() for _ in range(num_rows)],
            "valor_compra": [fake.pydecimal(left_digits=4, right_digits=2, positive=True) for _ in range(num_rows)],
            "data_cadastro": [fake.date_this_decade() for _ in range(num_rows)],
            "cidade": [fake.city() for _ in range(num_rows)],
            "produto_comprado": [random.choice(produtos) for _ in range(num_rows)],
        }
        df = pd.DataFrame(data)
        os.makedirs(os.path.dirname(self.input_path), exist_ok=True)
        df.to_csv(self.input_path, index=False, sep=";", decimal=",")
        print("Geração de dados concluída.")

    @log_task
    def execute(self, data=None) -> pd.DataFrame:
        """Gera e extrai os dados.

        Se o arquivo não existir, ele é criado com 10.000 linhas.
        Depois, os dados são lidos e retornados.

        Args:
            data: Não utilizado nesta tarefa.

        Returns:
            pd.DataFrame: Dados extraídos do arquivo CSV.
        """
        if not os.path.exists(self.input_path):
            self._generate_data(10000)

        df = pd.read_csv(self.input_path, sep=";", decimal=",")
        return df
