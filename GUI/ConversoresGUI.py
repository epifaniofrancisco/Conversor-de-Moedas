from API.api import dados_api
from Funcoes.Conversores_Calculo import convertEUR_AOA, convertEUR_USD, convertEUR_BRL, convertEUR_GBP  # EURO
from Funcoes.Conversores_Calculo import convertUSD_AOA, convertUSD_EUR, convertUSD_BRL, convertUSD_GBP  # DOLAR
from Funcoes.Conversores_Calculo import convertBRL_AOA, convertBRL_EUR, convertBRL_USD, convertBRL_GBP  # REAIS
from Funcoes.Conversores_Calculo import convertGBP_AOA, convertGPB_EUR, convertGPB_USD, convertGBP_BRL  # LIBRAS


dados = dados_api()

""" EUR - EURO """


def EURAOA(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertEUR_AOA(valor, float(dados[0]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def EURUSD(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertEUR_USD(valor, float(dados[1]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def EURBRL(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertEUR_USD(valor, float(dados[2]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def EURGBP(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertEUR_GBP(valor, float(dados[3]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


""" USD - DOLAR """


def USDAOA(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertUSD_AOA(valor, float(dados[4]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def USDEUR(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertUSD_EUR(valor, float(dados[5]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def USDBRL(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertUSD_BRL(valor, float(dados[6]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def USDGBP(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertUSD_GBP(valor, float(dados[7]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def BRLAOA(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertBRL_AOA(valor, float(dados[6]), dados[4])

    total = str(conversao)
    tela.txtBoxPara.setText(total)


""" BRL - REAIS """


def BRLEUR(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertBRL_EUR(valor, float(dados[8]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def BRLUSD(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertBRL_USD(valor, float(dados[9]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def BRLGBP(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertBRL_GBP(valor, float(dados[10]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


""" GBP - LIBRAS """


def GBPAOA(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertGBP_AOA(valor, float(dados[7]), float(dados[4]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def GBPEUR(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertGPB_EUR(valor, float(dados[11]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def GBPUSD(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertGPB_USD(valor, float(dados[12]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def GBPBRL(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertGBP_BRL(valor, float(dados[13]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)