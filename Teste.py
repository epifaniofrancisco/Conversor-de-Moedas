"""
 ** Autor: Epifânio Francisco
 ** Data: 23/03/2021  Hora: 12:41
 ** Função: Converter moedas.
"""


from Funcoes.Apresentacao import apresentacao
from Funcoes.Conversores import conversor_kwanza, conversor_euro, conversor_dolar, conversor_reais, conversor_libras


while True:
    apresentacao()

    escolha = int(input("Converter para: "))

    if escolha == 1:
        conversor_kwanza()
    if escolha == 2:
        conversor_euro()
    if escolha == 3:
        conversor_dolar()
    if escolha == 4:
        conversor_reais()
    if escolha == 5:
        conversor_libras()

    if escolha == 0:
        break


