from API.api import dados_api
from Funcoes.Conversores_Calculo import convertAOA_EUR, convertAOA_USD, convertAOA_BRL, convertAOA_GBP  # KWANZA
from Funcoes.Conversores_Calculo import convertEUR_AOA, convertEUR_USD, convertEUR_BRL, convertEUR_GBP  # EURO
from Funcoes.Conversores_Calculo import convertUSD_AOA, convertUSD_EUR, convertUSD_BRL, convertUSD_GBP  # DOLAR
from Funcoes.Conversores_Calculo import convertBRL_AOA, convertBRL_EUR, convertBRL_USD, convertBRL_GBP  # REAIS
from Funcoes.Conversores_Calculo import convertGBP_AOA, convertGPB_EUR, convertGPB_USD, convertGBP_BRL  # LIBRAS

dados = dados_api()

""" KWANZA - AOA """


def convertAOAEUR(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertAOA_EUR(valor, float(dados[5]), float(dados[4]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def convertAOAUSD(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertAOA_USD(valor, float(dados[4]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def convertAOABRL(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertAOA_BRL(valor, float(dados[6]), float(dados[4]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def convertAOAGBP(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertAOA_GBP(valor, float(dados[7]), float(dados[4]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


""" EUR - EURO """


def convertEURAOA(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertEUR_AOA(valor, float(dados[0]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def convertEURUSD(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertEUR_USD(valor, float(dados[1]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def convertEURBRL(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertEUR_BRL(valor, float(dados[2]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def convertEURGBP(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertEUR_GBP(valor, float(dados[3]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


""" USD - DOLAR """


def convertUSDAOA(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertUSD_AOA(valor, float(dados[4]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def convertUSDEUR(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertUSD_EUR(valor, float(dados[5]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def convertUSDBRL(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertUSD_BRL(valor, float(dados[6]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def convertUSDGBP(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertUSD_GBP(valor, float(dados[7]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


""" BRL - REAIS """


def convertBRLAOA(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertBRL_AOA(valor, float(dados[6]), float(dados[4]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def convertBRLEUR(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertBRL_EUR(valor, float(dados[8]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def convertBRLUSD(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertBRL_USD(valor, float(dados[9]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def convertBRLGBP(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertBRL_GBP(valor, float(dados[10]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


""" GBP - LIBRAS """


def convertGBPAOA(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertGBP_AOA(valor, float(dados[7]), float(dados[4]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def convertGBPEUR(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertGPB_EUR(valor, float(dados[11]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def convertGBPUSD(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertGPB_USD(valor, float(dados[12]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)


def convertGBPBRL(tela):
    valor = int(tela.txtBoxDe.text())
    conversao = convertGBP_BRL(valor, float(dados[13]))

    total = str(conversao)
    tela.txtBoxPara.setText(total)
