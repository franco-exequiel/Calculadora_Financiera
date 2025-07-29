import pandas as pd
from io import BytesIO

class ExportadorService:

    @staticmethod
    def generar_csv(detalle: list) -> BytesIO:
        df = pd.DataFrame(detalle)
        buffer = BytesIO()
        df.to_csv(buffer, index=False)
        buffer.seek(0)
        return buffer

    @staticmethod
    def generar_excel(detalle: list) -> BytesIO:
        df = pd.DataFrame(detalle)
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Cálculo")
        buffer.seek(0)
        return buffer