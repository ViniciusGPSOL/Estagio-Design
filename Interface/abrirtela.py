from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

import logo_rc

class Janela(QtWidgets.QMainWindow):
     def __init__(self):
          super(Janela, self).__init__()
          uic.loadUi('ui/janela.ui', self)
          self.setFixedSize(777, 712)   

class TelaInicial(QtWidgets.QMainWindow):
     def __init__(self):
          super(TelaInicial, self).__init__()
          uic.loadUi('ui/tela_principal.ui', self)
          self.setFixedSize(777, 712)
          self.setWindowTitle('Tela principal')
          
          self.pushButton.clicked.connect(self.on_pushButton_clicked)
          self.janela = Janela()

     def on_pushButton_clicked(self):
          filepath = str(QFileDialog.getOpenFileName())
          #self.janela.show()

     '''def open_dialog_box(self):
          filepath = str(QFileDialog.getOpenFileName())'''



if __name__ == '__main__':
     import sys
     app = QtWidgets.QApplication(sys.argv)
     window = TelaInicial()
     window.show()
     sys.exit(app.exec_())
