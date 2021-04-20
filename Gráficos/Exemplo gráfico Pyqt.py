import sys
import numpy as np
import matplotlib.pyplot as plt
import ler_info
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget

#Abrir arquivo.txt e separar cada linha em uma lista. 
arq = open('info_g.txt', 'r')
info = (arq.readlines())

#classe para colocar dados nos parâmetros necessários
class dados_grafico(object):
    def __init__(self, dado):
        self.dado = int((float(dado[5:])))

#define a tela com as escalas e informações do gráfico
class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(7, 4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Dados do gráfico
        """
        xpoints = np.array(colunas)
        ypoints = np.array(lista_dados)
        
        self.ax.bar(xpoints, ypoints)

        self.ax.set(xlabel=info[2][4:], ylabel=info[3][4:],
            title=info[1][4:])
        """self.ax.grid()"""

#Define a resolução
class AppGrafico(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1400, 800)

        chart = Canvas(self)

#listas com os dados organizados para o gráfico
lista_dados = []
colunas = []

#Converter e adicionar os dados para as listas de dados do gráfico 
for element in info:
    if element[4:5] == '#':
        dado_convertido = dados_grafico(element)
        lista_dados.append(dado_convertido.dado)
        coluna = lista_dados.index(dado_convertido.dado) + 1
        colunas.append(info[2][4:] + ' ' + str(coluna))

app = QApplication(sys.argv)   
janela = AppGrafico()
janela.show()
sys.exit(app.exec_())


