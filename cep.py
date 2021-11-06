import requests
from flask import Flask
import json
print("############")
print("Consulta Cep")
print("############")
print()

app = Flask(__name__)
@app.route('/consultaCep', methods=['GET'])
def consultaCep():
    cep_input = input("Digite o CEP para consulta: ")
    if len(cep_input) != 8:
        print("Quantidade de dígitos inválido!")
        retorno = json.loads('{"Entrada de cep":"Quantidade de dígitos inválido!"}')
        return retorno
        exit()

    request = requests.get(f'http://viacep.com.br/ws/{cep_input}/json/')

    address_data = request.json()

    if 'erro' not in address_data:
        print(request.json())
        print("O ddd do cep é", address_data["ddd"])
        retorno = request.json()
            
    else: 
        retorno = json.loads('{"Entrada de cep":"CEP Inválido"}')
        
    return retorno

# def novaConsulta():
#     print("--------------------------------------")
#     option = int(input("Deseja realizar nova consulta? 1 - Sim. 2 - Não "))
#     if option == 1:
#         retorno = consultaCep()
#     else:
#         print("Saindo..")
#         exit()
#     return retorno
