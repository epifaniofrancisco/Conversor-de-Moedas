import sys
from PyQt6 import QtCore, QtGui, QtWidgets



class Main2(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(300, 200)
        self.centralwidget = QtWidgets.QWidget(self)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 84, 260, 32))
        self.setCentralWidget(self.centralwidget)

        self._variable = None  # Variable "privada", de uso interno.

    @property
    def variable(self):
        return self._variable

    @variable.setter
    def variable(self, text):
        self._variable = text
        self.lineEdit.setText(text)


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.boton = QtWidgets.QPushButton(self.centralwidget, text="Aceptar")
        self.boton.setGeometry(QtCore.QRect(370, 280, 88, 34))
        self.lineEdit_0 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_0.setGeometry(QtCore.QRect(210, 240, 411, 32))
        self.setCentralWidget(self.centralwidget)

        self.otra = Main2()
        self.boton.clicked.connect(self.dato)

    def dato(self):
        self.otra.variable = self.lineEdit_0.text()
        self.otra.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    m = Main()
    m.show()
    sys.exit(app.exec())