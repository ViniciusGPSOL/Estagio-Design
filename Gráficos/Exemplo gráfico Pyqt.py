import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget

class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Dados do gráfico
        """
        xpoints = np.array(['Coluna1', 'Coluna2', 'Coluna3', 'Coluna4'])
        ypoints = np.array([120, 60, 80, 240])
        
        self.ax.bar(xpoints, ypoints)

        self.ax.set(xlabel='Tempo(s)', ylabel='Espaço(m)',
            title='Gráfico Teste')
        """self.ax.grid()"""

class AppGrafico(QWidget)      :
    def __init__(self):
        super().__init__()
        self.resize(1000, 800)

        chart = Canvas(self)

app = QApplication(sys.argv)        
janela = AppGrafico()
janela.show()
sys.exit(app.exec_())
