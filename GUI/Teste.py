from PyQt6 import uic, QtWidgets
from API.api import dados_api
from ConversoresGUI import EURAOA, EURUSD, EURBRL, EURGBP
from ConversoresGUI import USDAOA, USDEUR, USDBRL, USDGBP
from ConversoresGUI import BRLAOA, BRLEUR, BRLUSD, BRLGBP
from ConversoresGUI import GBPAOA, GBPEUR, GBPUSD, GBPBRL

dados = dados_api()


def converter():
    moedaDe = tela.cmbBoxDe.currentText()
    moedaPara = tela.cmbBoxPara.currentText()

    if moedaDe == "EUR - EURO" and moedaPara == "AOA - KWANZA":
        EURAOA(tela)
    if moedaDe == "EUR - EURO" and moedaPara == "USD - DOLAR":
        EURUSD(tela)
    if moedaDe == "EUR - EURO" and moedaPara == "BRL - REAIS":
        EURBRL(tela)
    if moedaDe == "EUR - EURO" and moedaPara == "GBP - LIBRAS":
        EURGBP(tela)

    if moedaDe == "USD - DOLAR" and moedaPara == "AOA - KWANZA":
        USDAOA(tela)
    if moedaDe == "USD - DOLAR" and moedaPara == "EUR - EURO":
        USDEUR(tela)
    if moedaDe == "USD - DOLAR" and moedaPara == "BRL - REAIS":
        USDBRL(tela)
    if moedaDe == "USD - DOLAR" and moedaPara == "GBP - LIBRAS":
        USDGBP(tela)

    if moedaDe == "BRL - REAIS" and moedaPara == "AOA - KWANZA":
        BRLAOA(tela)
    if moedaDe == "BRL - REAIS" and moedaPara == "EUR - EURO":
        BRLEUR(tela)
    if moedaDe == "BRL - REAIS" and moedaPara == "USD - DOLAR":
        BRLUSD(tela)
    if moedaDe == "BRL - REAIS" and moedaPara == "GBP - LIBRAS":
        BRLGBP(tela)

    if moedaDe == "GBP - LIBRAS" and moedaPara == "AOA - KWANZA":
        GBPAOA(tela)
    if moedaDe == "GBP - LIBRAS" and moedaPara == "EUR - EURO":
        GBPEUR(tela)
    if moedaDe == "GBP - LIBRAS" and moedaPara == "USD - DOLAR":
        GBPUSD(tela)
    if moedaDe == "GBP - LIBRAS" and moedaPara == "BRL - REAIS":
        GBPBRL(tela)


app = QtWidgets.QApplication([])
tela = uic.loadUi("gui.ui")

tela.btnConverter.clicked.connect(converter)

tela.show()
app.exec()
