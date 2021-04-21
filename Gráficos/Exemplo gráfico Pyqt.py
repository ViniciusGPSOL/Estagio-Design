import sys
import numpy as np
import matplotlib.pyplot as plt
import ler_info as li
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget

#Abrir arquivo.txt e separar cada linha em uma lista. 
arq = open('info_g.txt', 'r')
info = (arq.readlines())

#define a tela com as escalas e informações do gráfico
class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(7, 4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Dados do gráfico
        """
        xpoints = np.array(li.colunas)
        ypoints = np.array(li.lista_dados_num)
        
        self.ax.bar(xpoints, ypoints)

        self.ax.set(xlabel=li.x, ylabel=li.y,
            title=li.titulo)
        """self.ax.grid()"""

#Define a resolução
class AppGrafico(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1400, 800)

        chart = Canvas(self)

#listas com os dados organizados para o gráfico
#lista_dados_num = []
#colunas = []

#adicionar os dados para as listas de dados do gráfico 
for element in info:
    if element[4:5] == '#':
        element_unico = li.grafico_barras(element, info[2])
        element_unico.converter_dados_num()

app = QApplication(sys.argv)   
janela = AppGrafico()
janela.show()
sys.exit(app.exec_())