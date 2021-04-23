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

def limpar_dados():
    li.colunas = []
    li.lista_dados_num = []


class Grafico_linha(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(7, 4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

#Dados do gráfico
        xpoints = np.array(li.colunas)
        ypoints = np.array(li.lista_dados_num)
        
        self.ax.plot(xpoints, ypoints)
        self.ax.grid(True)
        self.ax.set(xlabel=li.x, ylabel=li.y,
             title=li.titulo)

        limpar_dados()

class Grafico_horizontal(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(7, 4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

#Dados do gráfico
        xpoints = np.array(li.colunas)
        ypoints = np.array(li.lista_dados_num)
        
        self.ax.barh(xpoints, ypoints)

        self.ax.set(xlabel=li.x, ylabel=li.y,
             title=li.titulo)

        limpar_dados()

class Grafico_barras(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(7, 4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

#Dados do gráfico
        xpoints = np.array(li.colunas)
        ypoints = np.array(li.lista_dados_num)
        
        self.ax.bar(xpoints, ypoints)

        self.ax.set(xlabel=li.x, ylabel=li.y, title=li.titulo)

        limpar_dados()

class Grafico_pizza(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(7, 4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

#Dados do gráfico
        y = np.array(li.lista_dados_num)
        
        self.ax.pie(y, labels = li.colunas)

        limpar_dados()

#Define a resolução
class AppGrafico(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1400, 800)
        if var == 1:
            chart = Grafico_barras(self)
        elif var == 2:
            chart = Grafico_pizza(self)
        elif var == 3:
            chart = Grafico_horizontal(self)
        elif var == 4:
            chart = Grafico_linha(self)

class Janela(QtWidgets.QMainWindow):
    def __init__(self):
        super(Janela, self).__init__()
        uic.loadUi('ui/janela.ui', self)
        self.setFixedSize(777, 712)
        self.pushButton.clicked.connect(self.open_grafico_barras)
        self.pushButton2.clicked.connect(self.open_grafico_pizza)
        self.pushButton3.clicked.connect(self.open_grafico_horizontal)
        self.pushButton4.clicked.connect(self.open_grafico_linha)
          

    def open_grafico_barras(self):
#adicionar os dados para as listas de dados do gráfico
        for element in info:
            if element[4:5] == '#':
                element_unico = li.grafico_barras(element, info[2])
                element_unico.converter_dados_num()
        global var
        var = 1
        self.janela = AppGrafico()
        self.janela.show()

    def open_grafico_pizza(self):
#adicionar os dados para as listas de dados do gráfico
        for element in info:
            if element[4:5] == '#':
                element_unico = li.grafico_pizza(element, info[2])
                element_unico.converter_dados_num()
        global var
        var = 2

        self.janela = AppGrafico()
        self.janela.show()

    def open_grafico_horizontal(self):
          #adicionar os dados para as listas de dados do gráfico
        for element in info:
            if element[4:5] == '#':
                element_unico = li.grafico_horizontal(element, info[2])
                element_unico.converter_dados_num()
        global var
        var = 3
            
        self.janela = AppGrafico()
        self.janela.show()

    def open_grafico_linha(self):
          #adicionar os dados para as listas de dados do gráfico
        for element in info:
            if element[4:5] == '#':
                element_unico = li.grafico_linha(element, info[2])
                element_unico.converter_dados_num()
        global var
        var = 4
            
        self.janela = AppGrafico()
        self.janela.show()
          

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
