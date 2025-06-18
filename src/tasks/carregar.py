# src/tasks/carregar.py
import pandas as pd
from src.task import Task
from src.utils.logger import log_task
import os


class CarregarTask(Task):
    def __init__(self):
        super().__init__(name="Carregar")
        self.output_path = "data/output.parquet"

    @log_task
    def execute(self, data: pd.DataFrame) -> None:
        """
        Carrega os dados transformados e os salva em um arquivo de saída final.
        Neste caso, salva um agregado como arquivo Parquet.
        """
        if data is None:
            raise ValueError("A tarefa de Carga precisa de dados da etapa anterior.")

        # Exemplo de agregação final: total de compras por domínio de e-mail
        agg_data = data.groupby("dominio_email")["valor_compra"].sum().reset_index()

        # Salva o resultado final no formato Parquet
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        agg_data.to_parquet(self.output_path, index=False)
