"""Tarefa de carregamento de dados.

Agrega e salva os dados transformados em um arquivo Parquet
no caminho especificado em `output_path`.
"""

import locale
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

        Neste caso, salva um agregado por ano, cidade e produto
        como arquivo Parquet, com valores monetários formatados como BRL.

        Args:
            data (pd.DataFrame): Dados transformados para serem carregados.

        Raises:
            ValueError: Se os dados de entrada forem None.
        """
        if data is None:
            raise ValueError("Precisa de dados da etapa anterior.")

        print("Iniciando agregação detalhada dos dados...")

        agg_data = (
            data.groupby(["ano_cadastro", "cidade", "produto_comprado"])
            .agg(
                valor_total=("valor_compra", "sum"), valor_medio=("valor_compra", "mean"), total_vendas=("id", "count")
            )
            .reset_index()
        )

        agg_data["valor_total"] = agg_data["valor_total"].round(2)
        agg_data["valor_medio"] = agg_data["valor_medio"].round(2)

        try:
            locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")
        except locale.Error:
            print("Locale 'pt_BR.UTF-8' não encontrado. Usando locale padrão do sistema.")
            try:
                locale.setlocale(locale.LC_MONETARY, "Portuguese_Brazil.1252")
            except locale.Error:
                print("Não foi possível configurar um locale para Português (BRL).")

        agg_data["valor_total"] = agg_data["valor_total"].apply(lambda x: locale.currency(x, grouping=True))
        agg_data["valor_medio"] = agg_data["valor_medio"].apply(lambda x: locale.currency(x, grouping=True))

        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        agg_data.to_parquet(self.output_path, index=False)

        print(f"Arquivo de saída salvo em: {self.output_path}")
