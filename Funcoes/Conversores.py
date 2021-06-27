"""
    Módulo usado para converter as moedas.

    - Kwanza
    - Euro
    - Dolar
    - Reais
    - Libras
"""

from Funcoes.Mensagens import mensagens
from API.api import dados_api
from Funcoes.Conversores_Calculo import convertAOA_EUR, convertAOA_USD, convertAOA_BRL, convertAOA_GBP  # KWANZA
from Funcoes.Conversores_Calculo import convertEUR_AOA, convertEUR_USD, convertEUR_BRL, convertEUR_GBP  # EURO
from Funcoes.Conversores_Calculo import convertUSD_AOA, convertUSD_EUR, convertUSD_BRL, convertUSD_GBP  # DÓLAR
from Funcoes.Conversores_Calculo import convertBRL_AOA, convertBRL_EUR, convertBRL_USD, convertBRL_GBP  # REAIS
from Funcoes.Conversores_Calculo import convertGBP_AOA, convertGPB_EUR, convertGPB_USD, convertGBP_BRL  # LIBRA

dados = dados_api()


def conversor_kwanza():
    mensagens(1)

    escolha = int(input("\nEscolha: "))
    valor = float(input("\nValor Kz: "))

    if escolha == 1:
        print("\n| - - - - - - - - - - - - |"
              "\n|    KWANZA PARA EURO     |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Kz equivalem a {} Euros.".format(valor, convertAOA_EUR(valor, float(dados[5]), float(dados[4]))))

    if escolha == 2:
        print("\n| - - - - - - - - - - - - |"
              "\n|    KWANZA PARA DOLAR    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Kz equivalem a {} Dolares.".format(valor, convertAOA_USD(valor, float(dados[4]))))

    if escolha == 3:
        print("\n| - - - - - - - - - - - - |"
              "\n|    KWANZA PARA REAIS    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Kz equivalem a {} Reais.".format(valor, convertAOA_BRL(valor, float(dados[6]), float(dados[4]))))

    if escolha == 4:
        print("\n| - - - - - - - - - - - - |"
              "\n|    KWANZA PARA LIBRAS   |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Kz equivalem a {} Libras.".format(valor, convertAOA_GBP(valor, float(dados[7]), float(dados[4]))))


def conversor_euro():
    mensagens(2)

    escolha = int(input("\nEscolha: "))
    valor = float(input("\nValor £: "))

    if escolha == 1:
        print("\n| - - - - - - - - - - - - |"
              "\n|    EURO PARA KWANZA     |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Euros equivalem a {} Kz.".format(valor, convertEUR_AOA(valor, float(dados[0]))))

    if escolha == 2:
        print("\n| - - - - - - - - - - - - |"
              "\n|    EURO PARA DOLAR      |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Euros equivalem a {} Dolares.".format(valor, convertEUR_USD(valor, float(dados[1]))))

    if escolha == 3:
        print("\n| - - - - - - - - - - - - |"
              "\n|     EURO PARA REAIS     |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Euros equivalem a {} Reais.".format(valor, convertEUR_BRL(valor, float(dados[2]))))

    if escolha == 4:
        print("\n| - - - - - - - - - - - - |"
              "\n|    EURO PARA LIBRAS     |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Euros equivalem a {} Libras.".format(valor, convertEUR_GBP(valor, float(dados[3]))))


def conversor_dolar():
    mensagens(3)

    escolha = int(input("\nEscolha: "))
    valor = float(input("\nValor USD: "))

    if escolha == 1:
        print("\n| - - - - - - - - - - - - |"
              "\n|    DOLAR PARA KWANZA    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Dolares equivalem a {} Kz.".format(valor, convertUSD_AOA(valor, float(dados[4]))))

    if escolha == 2:
        print("\n| - - - - - - - - - - - - |"
              "\n|    DOLAR PARA EURO      |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Dolares equivalem a {} Euros.".format(valor, convertUSD_EUR(valor, float(dados[5]))))

    if escolha == 3:
        print("\n| - - - - - - - - - - - - |"
              "\n|    DOLAR PARA REAIS     |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Dolares equivalem a {} Reais.".format(valor, convertUSD_BRL(valor, float(dados[6]))))

    if escolha == 4:
        print("\n| - - - - - - - - - - - - |"
              "\n|    DOLAR PARA LIBRAS    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Dolares equivalem a {} Libras.".format(valor, convertUSD_GBP(valor, float(dados[7]))))


def conversor_reais():
    mensagens(4)

    escolha = int(input("\nEscolha: "))
    valor = float(input("\nValor Rs: "))

    if escolha == 1:
        print("\n| - - - - - - - - - - - - |"
              "\n|    REAIS PARA KWANZA    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Reais equivalem a {} Kz.".format(valor, convertBRL_AOA(valor, float(dados[6]), float(dados[4]))))

    if escolha == 2:
        print("\n| - - - - - - - - - - - - |"
              "\n|    REAIS PARA EURO      |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Reais equivalem a {} Euros.".format(valor, convertBRL_EUR(valor, float(dados[8]))))

    if escolha == 3:
        print("\n| - - - - - - - - - - - - |"
              "\n|    REAIS PARA DOLAR     |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Reais equivalem a {} Dolares.".format(valor, convertBRL_USD(valor, float(dados[9]))))

    if escolha == 4:
        print("\n| - - - - - - - - - - - - |"
              "\n|    REAIS PARA LIBRAS    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Reais equivalem a {} Libras.".format(valor, convertBRL_GBP(valor, float(dados[10]))))


def conversor_libras():
    mensagens(5)

    escolha = int(input("Escolha: "))
    valor = float(input("\nValor GBP: "))

    if escolha == 1:
        print("\n| - - - - - - - - - - - - |"
              "\n|    LIBRAS PARA KWANZA   |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Libras equivalem a {} Kz.".format(valor, convertGBP_AOA(valor, float(dados[7]), float(dados[4]))))

    if escolha == 2:
        print("\n| - - - - - - - - - - - - |"
              "\n|    LIBRAS PARA EURO     |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Libras equivalem a {} Euros.".format(valor, convertGPB_EUR(valor, float(dados[11]))))

    if escolha == 3:
        print("\n| - - - - - - - - - - - - |"
              "\n|    LIBRAS PARA DOLAR    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Libras equivalem a {} Dolares.".format(valor, convertGPB_USD(valor, float(dados[12]))))

    if escolha == 4:
        print("\n| - - - - - - - - - - - - |"
              "\n|    LIBRAS PARA Reais    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Euros equivalem a {} Reais.".format(valor, convertGBP_BRL(valor, float(dados[13]))))
