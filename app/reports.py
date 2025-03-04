import pandas as pd
from datetime import datetime

def generate_report():
    try:
        data = pd.read_csv("data/attacks.csv")
        report_name = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        data.to_csv(f"data/{report_name}", index=False)
        print(f"Reporte generado: {report_name}")
    except FileNotFoundError:
        print("No se encontraron datos para generar el reporte.")