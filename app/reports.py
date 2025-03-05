import pandas as pd
import json
import os
from datetime import datetime

REPORTS_DIR = "reports"

def generate_report():
    try:
        # Leer datos de ataques
        df = pd.read_csv("data/attacks.csv")
        
        if df.empty:
            return

        # Crear directorio si no existe
        os.makedirs(REPORTS_DIR, exist_ok=True)

        # Generar nombre de archivo con timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Reporte CSV
        csv_file = f"{REPORTS_DIR}/report_{timestamp}.csv"
        df.to_csv(csv_file, index=False)
        
        # Reporte JSON
        json_file = f"{REPORTS_DIR}/report_{timestamp}.json"
        df.to_json(json_file, orient="records", indent=4)
        
        print(f"Reportes generados: {csv_file}, {json_file}")

    except Exception as e:
        print(f"Error generando reportes: {e}")