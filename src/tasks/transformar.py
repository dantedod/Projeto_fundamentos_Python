"""Tarefa de transformação de dados.

Aplica transformações nos dados, como criação de novas colunas
e limpeza de valores nulos.
"""

import os

import pandas as pd

from src.task import Task
from src.utils.logger import log_task


class TransformarTask(Task):
    """Classe que implementa a tarefa de transformação de dados.

    Essa tarefa aplica transformações específicas nos dados,
    incluindo a criação de uma nova coluna e limpeza de dados.
    """

    def __init__(self):
        """Inicializa a tarefa de transformação com o nome e o caminho para o arquivo intermediário."""
        super().__init__(name="Transformar")
        self.stage_path = "data/stage.csv"

    @log_task
    def execute(self, data: pd.DataFrame) -> pd.DataFrame:
        """Executa as transformações nos dados.

        As transformações incluem:
        1. Criação da coluna 'dominio_email' a partir do email.
        2. Conversão da coluna 'valor_compra' para tipo numérico.
        3. Remoção de linhas com valores nulos em 'valor_compra'.

        Args:
            data (pd.DataFrame): Dados a serem transformados.

        Raises:
            ValueError: Se os dados de entrada forem None.

        Returns:
            pd.DataFrame: Dados transformados.
        """
        if data is None:
            raise ValueError("A tarefa de Transformação precisa de dados da etapa anterior.")

        df_transformed = data.copy()

        df_transformed["dominio_email"] = df_transformed["email"].apply(lambda x: x.split("@")[1])

        df_transformed["valor_compra"] = pd.to_numeric(df_transformed["valor_compra"], errors="coerce")

        df_transformed.dropna(subset=["valor_compra"], inplace=True)

        os.makedirs(os.path.dirname(self.stage_path), exist_ok=True)
        df_transformed.to_csv(self.stage_path, index=False, sep=";", decimal=",")

        return df_transformed
