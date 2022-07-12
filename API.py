import pandas as pd
import json
from flask import Flask, jsonify


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def homepage():
  return "API está no ar<p>Para acessar a API adicione na url: /pegardados</p>"

@app.route('/pegardados')
def pegardados():
  df = pd.read_parquet('./Dados de Logistica.parquet')
  result = df.to_json(orient="records")
  parsed = json.loads(result)
  resposta = {'dados': parsed}
  return jsonify(resposta)

if __name__ == "__main__":
    app.run(debug=True)