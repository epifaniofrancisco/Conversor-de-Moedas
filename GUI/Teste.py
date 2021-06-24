from PyQt6 import uic, QtWidgets

from Funcoes.Conversores_Calculo import convertAOA_USD, convertAOA_EUR


def converter():
    moeda = tela.cmbBoxDe.currentText()
    moedaPara = tela.cmbBoxPara.currentText()

    if moeda == "AOA - KWANZA" and moedaPara == "USD - DOLAR":
        valor = int(tela.txtBoxDe.text())
        conv = convertAOA_USD(valor, 650.186)

        total = str(conv)
        tela.txtBoxPara.setText(total)
        print(total)
    elif moeda == "AOA - KWANZA" and moedaPara == "EUR - EURO":
        valor = int(tela.txtBoxDe.text())
        conv = convertAOA_EUR(valor, 100, 650.186)

        total = str(conv)
        tela.txtBoxPara.setText(total)
        print(total)


app = QtWidgets.QApplication([])
tela = uic.loadUi("gui.ui")

tela.btnConverter.clicked.connect(converter)

tela.show()
app.exec()