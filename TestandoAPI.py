import os
import sys

import requests
import socket
import json


def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


def getCurrency():
    if is_connected():

        response = requests.get('https://economia.awesomeapi.com.br/json/last/'
                                'EUR-AOA,EUR-USD,EUR-BRL,EUR-GBP,'
                                'USD-AOA,USD-EUR,USD-BRL,USD-GBP,'
                                'BRL-EUR,BRL-USD,BRL-GBP,'
                                'GBP-EUR,GBP-USD,GBP-BRL')

        dados = response.json()
        with open('data.json', 'w') as outfile:
            json.dump(dados, outfile)
        exchange = [dados["EURAOA"]["bid"], dados["EURUSD"]["bid"]]
        return exchange

    elif not is_connected():
        if os.path.exists("data.json"):
            with open('data.json') as json_file:
                dados = json.load(json_file)
                exchange = [dados["EURAOA"]["bid"], dados["EURUSD"]["bid"]]
                return exchange
        else:
            sys.exit("Connecte a internet para baixar os dados!!!")


dados = getCurrency()

print(dados[0])

