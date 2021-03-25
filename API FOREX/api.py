import requests
import json
import os
import sys

from Funcoes.conectado import conexao


def Currency():
    if conexao():
        api = requests.get(
            'https://www.freeforexapi.com/api/live?pairs=USDAOA,USDEUR,USDBRL,USDGBP,EURUSD,EURGBP,GBPUSD')
        dados = api.json()

        with open('dados.json', 'w') as ficheiro:
            json.dump(dados, ficheiro)
        moedas = [dados["rates"]["USDAOA"]["rate"], dados["rates"]["USDEUR"]["rate"], dados["rates"]["USDBRL"]["rate"], dados["rates"]["USDGBP"]["rate"], dados["rates"]["EURUSD"]["rate"], dados["rates"]["EURGBP"]["rate"], dados["rates"]["GBPUSD"]["rate"]]
        return moedas

    elif not conexao():
        if os.path.exists("dados.json"):
            with open('dados.json') as json_file:
                dados = json.load(json_file)
                moedas = [dados["rates"]["USDAOA"]["rate"], dados["rates"]["USDEUR"]["rate"],
                          dados["rates"]["USDBRL"]["rate"],
                          dados["rates"]["USDGBP"]["rate"], dados["rates"]["EURUSD"]["rate"],
                          dados["rates"]["EURGBP"]["rate"],
                          dados["rates"]["GBPUSD"]["rate"]]
            return moedas
        else:
            sys.exit('Ligue-se a Internet para baixar os dados.')

dados = Currency()

print(dados)