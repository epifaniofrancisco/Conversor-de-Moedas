"""

Módulo criado para cálculos de conversão.

"""

""" KWANZA - AOA """


def convertAOA_EUR(valor, EUR, USD):
    # EUR: valor de conversão de 1 dólar para euros.
    # USD: valor de conversão de 1 dólar para kwanza.
    return round(convertAOA_USD(valor, USD) * EUR, 4)


def convertAOA_USD(valor, USD):
    # USD é o valor que 1 dólar equivale a kwanzas.
    return round(valor * (1 / USD), 4)


def convertAOA_BRL(valor, BRL, USD):
    # BRL: valor de conversão de 1 dólar para reais.
    # USD: valor de conversão de 1 dólar para kwanza.
    return round(convertAOA_USD(valor, USD) * BRL, 4)


def convertAOA_GBP(valor, GBP, USD):
    # GBP: valor de conversão de 1 dólar para libras.
    # USD: valor de conversão de 1 dólar para kwanza.
    return round(convertAOA_USD(valor, USD) * GBP, 4)


""" EURO - EUR """


def convertEUR_AOA(valor, AOA):
    # AOA: valor da cotaçao de 1 euro para kwanza.
    return round(valor * AOA, 2)


def convertEUR_USD(valor, USD):
    # USD: valor da cotação de 1 euro para dolar.
    return round(valor * USD, 2)


def convertEUR_BRL(valor, BRL):
    # BRL: valor da cotação de 1 euro para reais.
    return round(valor * BRL, 2)


def convertEUR_GBP(valor, GBP):
    # GBP: valor da cotação de 1 euro para libras.
    return round(valor * GBP, 2)


""" DÓLAR - USD"""


def convertUSD_AOA(valor, AOA):
    # AOA: valor da cotação de 1 dolar para kwanza.
    return round(valor * AOA, 2)


def convertUSD_EUR(valor, EUR):
    # EUR: valor da cotação de 1 dolar para euro.
    return round(valor * EUR, 2)


def convertUSD_BRL(valor, BRL):
    # BRL: valor da cotação de 1 dolar para reais.
    return round(valor * BRL, 2)


def convertUSD_GBP(valor, GBP):
    # AOA: valor da cotação de 1 dolar para libras.
    return round(valor * GBP, 2)


""" REAIS - BRL """


def convertBRL_AOA(valor, BRL, AOA):
    # BRL: valor da conversão de 1 dólar para real.
    # AOA: valor da conversão de 1 dólar para kwanza.
    res = round(((1 / BRL) * valor), 4)
    print(res)
    return round(res * AOA, 4)


def convertBRL_EUR(valor, EUR):
    # EUR: valor da cotação de 1 real para euro.
    return round(valor * EUR, 2)


def convertBRL_USD(valor, USD):
    # USD: valor da cotação de 1 real para dolar.
    return round(valor * USD, 2)


def convertBRL_GBP(valor, GBP):
    # GBP: valor da cotaçao de 1 real para libra.
    return round(valor * GBP, 2)


""" LIBRA - GBP """


def convertGBP_AOA(valor, GBP, AOA):
    # GBP: valor da conversão de 1 dólar para libra.
    # AOA: valor da conversão de 1 dólar para kwanza.
    res = round(((1 / GBP) * valor), 4)
    print(res)
    return round(res * AOA, 2)


def convertGPB_EUR(valor, EUR):
    # EUR: valor da cotação de 1 libra para euro.
    return round(valor * EUR, 2)


def convertGPB_USD(valor, USD):
    # USD: valor da cotação de 1 libra para dolar.
    return round(valor * USD, 2)


def convertGBP_BRL(valor, BRL):
    # BRL: valor da cotação de 1 libra para reais.
    return round(valor * BRL, 2)
