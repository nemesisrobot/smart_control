from flask import Flask , request , jsonify
from services.carro_luxo import *
from services.carro_popular import *
from services.fabrica_carros import *

app = Flask(__name__)


#base de dados
base = []

@app.route('/')
def index():
    return '<h1><center>Sistema de cadastro de carros</center></h1> <br> <h3>Total de casso >> {}</h3>'.format(len(base))


@app.route('/carros', methods=['GET'])
def pegar_todos_carros():
    return jsonify({'carros':base})


@app.route('/carros', methods=['POST'])
def cadastrar_carro():

    dados = request.get_json()
    carro = Fabrica()
    carro = carro.aluga(int(dados['tipo']))

    payload = {}
    payload['nome'] = dados['nome']
    payload['Valor'] = carro.valor_aluguel_carro()
    payload['potencia'] = carro.potencia_carro()
    payload['data'] = dados['data']
    base.append(payload)

    return jsonify({'message':'Car add!!!'})


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)