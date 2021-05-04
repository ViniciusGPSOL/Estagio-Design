from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget
import sys
import numpy as np
import matplotlib.pyplot as plt
import logo_rc
'''
class Grafico_barras(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(7, 4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

#Dados do gráfico
        xpoints = np.array(li.colunas)
        ypoints = np.array(li.lista_dados_num)
        
        self.ax.bar(xpoints, ypoints)


        self.ax.set(xlabel=titulo_linha, titulo_coluna, title=li.titulo)
'''

class AppGrafico(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1400, 800)

        
        if tipo_grafico == 'barras':
            print('2721')
            #chart = Grafico_barras(self)

        '''
        elif var == 2:
            chart = Grafico_pizza(self)
        elif var == 3:
            chart = Grafico_horizontal(self)
        elif var == 4:
            chart = Grafico_linha(self)'''
        
class TelaInicial(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaInicial, self).__init__()
        uic.loadUi('ui/tela_principal.ui', self)
        self.setFixedSize(777, 712)
        self.setWindowTitle('Tela principal')
        self.pushButton.clicked.connect(self.open_dialog_box)
          

    def open_dialog_box(self):
        filepath = QFileDialog.getOpenFileName()
        filename = filepath[0]
        with open(filename, "r") as f:
            global info
            info = (f.readlines())
#iformações primeira linha
            global div_linha1
            global div_linha2
            global div_linha3
            global div_linha4
            global div_linha5
            global titulo_grafico
            global tipo_grafico
            global cor_fundo
            global parametros
            global titulo_coluna
            global valores_x
            global titulo_linha
            global lista_valores
            
            div_linha1 = info[0].split(";")
            titulo_grafico = div_linha1[0][3:]
            tipo_grafico = div_linha1[1]
            cor_fundo = div_linha1[2]
#informações segunda linha
            div_linha2 = info[1].split(";")
            parametros = []
            for param in div_linha2:
                if param[:3] == '002':
                    par1 = param[3:]
                    parametros.append(par1)
                else:
                    parx = param
                    parametros.append(parx)
#informações terceira linha
            div_linha3 = info[2].split(";")
            titulo_coluna = div_linha3[0][3:]
#informações quarta linha
            div_linha4 = info[3].split(";")
            titulo_linha = div_linha4[0][3:]
            valores_x = []
            for e in div_linha4:
                if e[3:] != titulo_linha:
                    valores_x.append(e)
                    
#informação quinta linha
            div_linha5 = info[4].split("|")
            lista_valores = []
            t= 0
            while t != len(div_linha5):
                lista_elementos_str = div_linha5[t].split(';')
                lista_elementos =[]
                for val in lista_elementos_str:
                    if val[:3] == '005':
                        first = val[3:]
                        lista_elementos.append(int(first))
                    else:
                        lista_elementos.append(int(val))
                t += 1
                lista_valores.append(lista_elementos)
            self.pushButton.clicked.disconnect(self.open_dialog_box)
            
            janela = AppGrafico()
            janela.show()


if __name__ == '__main__':
     import sys
     app = QtWidgets.QApplication(sys.argv) 
     window = TelaInicial()
     window.show()
     sys.exit(app.exec_())
