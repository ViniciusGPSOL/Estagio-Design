from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget
import sys
import numpy as np
import matplotlib.pyplot as plt
import ler_info as li
import logo_rc

#define a tela com as escalas e informações do gráfico
class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(7, 4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

#Dados do gráfico
        xpoints = np.array(li.colunas)
        ypoints = np.array(li.lista_dados_num)
        
        self.ax.bar(xpoints, ypoints)

        self.ax.set(xlabel=li.x, ylabel=li.y,
             title=li.titulo)

#Define a resolução
class AppGrafico(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1400, 800)
        chart = Canvas(self)

class Janela(QtWidgets.QMainWindow):
    def __init__(self):
        super(Janela, self).__init__()
        uic.loadUi('ui/janela.ui', self)
        self.setFixedSize(777, 712)
        janela = AppGrafico()
        self.pushButton.clicked.connect(self.open_grafico_barras)
          

    def open_grafico_barras(self):
          #adicionar os dados para as listas de dados do gráfico
        for element in info:
            if element[4:5] == '#':
                element_unico = li.grafico_barras(element, info[2])
                element_unico.converter_dados_num()
            print(element)

        janela.show()
          

class TelaInicial(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaInicial, self).__init__()
        uic.loadUi('ui/tela_principal.ui', self)
        self.setFixedSize(777, 712)
        self.setWindowTitle('Tela principal')
        self.janela = Janela()
          
        self.pushButton.clicked.connect(self.open_dialog_box)
          

    def open_dialog_box(self):
        filepath = QFileDialog.getOpenFileName()
        filename = filepath[0]
        with open(filename, "r") as f:
            global info
            info = (f.readlines())
               
            self.janela.show()
            self.pushButton.clicked.disconnect(self.open_dialog_box)



if __name__ == '__main__':
     import sys
     app = QtWidgets.QApplication(sys.argv) 
     window = TelaInicial()
     window.show()
     sys.exit(app.exec_())
