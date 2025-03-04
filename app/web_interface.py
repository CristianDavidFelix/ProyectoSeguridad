from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    try:
        data = pd.read_csv("data/attacks.csv")
        return render_template("index.html", data=data.to_dict("records"))
    except FileNotFoundError:
        return "No se encontraron datos de ataques."

def run_web_interface():
    app.run(debug=True, host="0.0.0.0", port=5000)