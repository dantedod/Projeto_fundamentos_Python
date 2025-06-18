# src/tasks/transformar.py
import pandas as pd
from src.task import Task
from src.utils.logger import log_task
import os


class TransformarTask(Task):
    def __init__(self):
        super().__init__(name="Transformar")
        self.stage_path = "data/stage.csv"

    @log_task
    def execute(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Aplica transformações nos dados:
        1. Cria a coluna 'dominio_email'.
        2. Converte a coluna 'valor_compra' para numérico.
        3. Remove linhas com valores nulos.
        """
        if data is None:
            raise ValueError(
                "A tarefa de Transformação precisa de dados da etapa anterior."
            )

        df_transformed = data.copy()

        # 1. Extrai o domínio do e-mail
        df_transformed["dominio_email"] = df_transformed["email"].apply(
            lambda x: x.split("@")[1]
        )

        # 2. Converte 'valor_compra' para tipo float, tratando erros
        df_transformed["valor_compra"] = pd.to_numeric(
            df_transformed["valor_compra"], errors="coerce"
        )

        # 3. Remove linhas que possam ter ficado com valor nulo após a conversão
        df_transformed.dropna(subset=["valor_compra"], inplace=True)

        # Salva o resultado intermediário
        os.makedirs(os.path.dirname(self.stage_path), exist_ok=True)
        df_transformed.to_csv(self.stage_path, index=False, sep=";", decimal=",")

        return df_transformed
