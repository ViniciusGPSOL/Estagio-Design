import sys
import numpy as np
import matplotlib.pyplot as plt
import ler_info as li
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget

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

app = QApplication(sys.argv)   
janela = AppGrafico()
janela.show()
sys.exit(app.exec_())
