"""Tarefa de carregamento de dados.

Agrega e salva os dados transformados em um arquivo Parquet
no caminho especificado em `output_path`.
"""

import os

import pandas as pd

from src.task import Task
from src.utils.logger import log_task


class CarregarTask(Task):
    """Classe que realiza a tarefa de carregamento.

    Realiza a agregação e salva os dados transformados em arquivo Parquet.
    """

    def __init__(self):
        """Inicializa a tarefa com o nome e o caminho do arquivo de saída."""
        super().__init__(name="Carregar")
        self.output_path = "data/output.parquet"

    @log_task
    def execute(self, data: pd.DataFrame) -> None:
        """Carrega os dados transformados e salva em arquivo de saída.

        Neste caso, salva um agregado como arquivo Parquet.

        Args:
            data (pd.DataFrame): Dados transformados para serem carregados.

        Raises:
            ValueError: Se os dados de entrada forem None.
        """
        if data is None:
            raise ValueError("Precisa de dados da etapa anterior.")

        # Exemplo de agregação final: total de compras por domínio de e-mail
        agg_data = data.groupby("dominio_email")["valor_compra"].sum().reset_index()

        # Salva o resultado final no formato Parquet
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        agg_data.to_parquet(self.output_path, index=False)
