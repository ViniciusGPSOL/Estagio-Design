from PyQt5 import QtCore, QtGui, QtWidgets, uic

import logo_rc

class Janela(QtWidgets.QMainWindow):
     def __init__(self):
        super(TelaInicial, self).__init__()
        uic.loadUi('ui/janela.ui', self)
        self.setFixedSize(777, 712)   

class TelaInicial(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaInicial, self).__init__()
        uic.loadUi('ui/tela_principal.ui', self)
        self.setFixedSize(777, 712)
        self.setWindowTitle('Tela principal')

 



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = TelaInicial()
    window.show()
    sys.exit(app.exec_())
