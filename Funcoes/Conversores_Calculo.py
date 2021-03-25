""" KWANZA - AOA """


def convertAOA_EUR(valor, EUR, AOA):
    return round(convertAOA_USD(valor, AOA) * EUR, 2)


def convertAOA_USD(valor, AOA):
    return round(valor * (1 / AOA), 2)


def convertAOA_BRL(valor, BRL, AOA):
    return round(convertAOA_USD(valor, AOA) * BRL, 2)


def convertAOA_GBP(valor, GBP, AOA):
    return round(convertAOA_USD(valor, AOA) * GBP, 2)


""" EURO - EUR """


def convertEUR_AOA(valor, EUR, AOA):
    res = (1 / EUR) * valor
    return round(convertUSD_AOA(res, AOA), 2)


def convertEUR_USD(valor, EUR):
    return round(valor * (1 / EUR), 2)


def convertEUR_BRL(valor, BRL, EUR):
    return round(convertEUR_USD(valor, EUR) * BRL, 2)


def convertEUR_GBP(valor, GBP, EUR):
    return round(convertEUR_USD(valor, EUR) * GBP, 2)


""" DÓLAR - USD"""


def convertUSD_AOA(valor, AOA):
    return round(valor * AOA, 2)


def convertUSD_EUR(valor, EUR):
    return round(valor * EUR, 2)


def convertUSD_BRL(valor, BRL):
    return round(valor * BRL, 2)


def convertUSD_GBP(valor, GBP):
    return round(valor * GBP, 2)


""" REAIS - BRL """


def convertBRL_AOA(valor, BRL, AOA):
    """
    INCOMPLETO
    """
    res = (1 / BRL) * valor
    print(res)
    return round(convertAOA_USD(res, AOA), 2)


def convertBRL_EUR(valor, BRL, EUR):
    res = (1 / BRL) * valor
    return round(res * EUR, 2)


def convertBRL_USD(valor, BRL):
    return round(BRL / valor, 2)


def convertBRL_GBP(valor, BRL, GBP):
    res = (1 / BRL) * valor
    return round(res * GBP, 2)


""" LIBRA - GBP """


def convertGBP_AOA(valor, GBP, AOA):
    res = round(((1 / GBP) * valor), 2)
    print(res)
    return round(res * AOA, 2)


def convertGPB_EUR(valor, EUR):
    return round(valor * (1 / EUR), 2)


def convertGPB_USD(valor, USD):
    return round(valor * (1 / USD), 2)


def convertGBP_BRL(valor, GBP, BRL):
    res = (1 / GBP) * valor
    print(res)
    return round(res * BRL, 2)
