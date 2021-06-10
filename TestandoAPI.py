import requests

api = requests.get('https://www.freeforexapi.com/api/live?pairs=USDAOA,USDEUR')
dados = api.json()

print(dados)