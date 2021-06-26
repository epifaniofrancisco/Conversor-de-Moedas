import os
import sys

import requests
import socket
import json


def conectado():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


def pegaAPI():
    response = requests.get('https://economia.awesomeapi.com.br/json/last/'
                            'EUR-AOA,EUR-USD,EUR-BRL,EUR-GBP,'
                            'USD-AOA,USD-EUR,USD-BRL,USD-GBP,'
                            'BRL-EUR,BRL-USD,BRL-GBP,'
                            'GBP-EUR,GBP-USD,GBP-BRL')

    return response.json()


def dadosAPI():
    if conectado():

        dados = pegaAPI()

        with open('data.json', 'w') as outfile:
            json.dump(dados, outfile)
        exchange = [dados["EURAOA"]["bid"], dados["EURUSD"]["bid"], dados["EURBRL"]["bid"], dados["EURGBP"]["bid"],
                    dados["USDAOA"]["bid"], dados["USDEUR"]["bid"], dados["USDBRL"]["bid"], dados["USDGBP"]["bid"],
                    dados["BRLEUR"]["bid"], dados["BRLUSD"]["bid"], dados["BRLGBP"]["bid"], dados["GBPEUR"]["bid"],
                    dados["GBPUSD"]["bid"], dados["GBPBRL"]["bid"]]
        return exchange

    elif not conectado():
        if os.path.exists("data.json"):
            with open('data.json') as json_file:
                dados = json.load(json_file)
                exchange = [dados["EURAOA"]["bid"], dados["EURUSD"]["bid"], dados["EURBRL"]["bid"],
                            dados["EURGBP"]["bid"], dados["USDAOA"]["bid"], dados["USDEUR"]["bid"],
                            dados["USDBRL"]["bid"], dados["USDGBP"]["bid"], dados["BRLEUR"]["bid"],
                            dados["BRLUSD"]["bid"], dados["BRLGBP"]["bid"], dados["GBPEUR"]["bid"],
                            dados["GBPUSD"]["bid"], dados["GBPBRL"]["bid"]]
                return exchange
        else:
            sys.exit("Conecte-se a internet para baixar os dados.")
