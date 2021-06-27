from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from API.api import dados_api
from ConversoresGUI import convertAOAEUR, convertAOAUSD, convertAOABRL, convertAOAGBP
from ConversoresGUI import convertEURAOA, convertEURUSD, convertEURBRL, convertEURGBP
from ConversoresGUI import convertUSDAOA, convertUSDEUR, convertUSDBRL, convertUSDGBP
from ConversoresGUI import convertBRLAOA, convertBRLEUR, convertBRLUSD, convertBRLGBP
from ConversoresGUI import convertGBPAOA, convertGBPEUR, convertGBPUSD, convertGBPBRL

dados = dados_api()


def converter():
    moedaDe = tela.cmbBoxDe.currentText()
    moedaPara = tela.cmbBoxPara.currentText()

    valor = tela.txtBoxDe.text()

    if valor == "":
        QMessageBox.about(tela, "ALERTA", "DIGITE UM NÚMERO PARA CONVERTER.")

    if moedaDe == "AOA - KWANZA" and moedaPara == "EUR - EURO":
        convertAOAEUR(tela)
    if moedaDe == "AOA - KWANZA" and moedaPara == "USD - DOLAR":
        convertAOAUSD(tela)
    if moedaDe == "AOA - KWANZA" and moedaPara == "BRL - REAIS":
        convertAOABRL(tela)
    if moedaDe == "AOA - KWANZA" and moedaPara == "GBP - LIBRAS":
        convertAOAGBP(tela)

    if moedaDe == "EUR - EURO" and moedaPara == "AOA - KWANZA":
        convertEURAOA(tela)
    if moedaDe == "EUR - EURO" and moedaPara == "USD - DOLAR":
        convertEURUSD(tela)
    if moedaDe == "EUR - EURO" and moedaPara == "BRL - REAIS":
        convertEURBRL(tela)
    if moedaDe == "EUR - EURO" and moedaPara == "GBP - LIBRAS":
        convertEURGBP(tela)

    if moedaDe == "USD - DOLAR" and moedaPara == "AOA - KWANZA":
        convertUSDAOA(tela)
    if moedaDe == "USD - DOLAR" and moedaPara == "EUR - EURO":
        convertUSDEUR(tela)
    if moedaDe == "USD - DOLAR" and moedaPara == "BRL - REAIS":
        convertUSDBRL(tela)
    if moedaDe == "USD - DOLAR" and moedaPara == "GBP - LIBRAS":
        convertUSDGBP(tela)

    if moedaDe == "BRL - REAIS" and moedaPara == "AOA - KWANZA":
        convertBRLAOA(tela)
    if moedaDe == "BRL - REAIS" and moedaPara == "EUR - EURO":
        convertBRLEUR(tela)
    if moedaDe == "BRL - REAIS" and moedaPara == "USD - DOLAR":
        convertBRLUSD(tela)
    if moedaDe == "BRL - REAIS" and moedaPara == "GBP - LIBRAS":
        convertBRLGBP(tela)

    if moedaDe == "GBP - LIBRAS" and moedaPara == "AOA - KWANZA":
        convertGBPAOA(tela)
    if moedaDe == "GBP - LIBRAS" and moedaPara == "EUR - EURO":
        convertGBPEUR(tela)
    if moedaDe == "GBP - LIBRAS" and moedaPara == "USD - DOLAR":
        convertGBPUSD(tela)
    if moedaDe == "GBP - LIBRAS" and moedaPara == "BRL - REAIS":
        convertGBPBRL(tela)


app = QtWidgets.QApplication([])
tela = uic.loadUi("gui.ui")

tela.btnConverter.clicked.connect(converter)

tela.show()
app.exec()
