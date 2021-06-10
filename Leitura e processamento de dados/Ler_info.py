from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget
import sys
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import logo_rc

class Grafico_pizza(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(7, 4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

#Dados do gráfico

        valores_pizza = []
        total = 0

        for item in lista_valores:
            valores_pizza.append(item[0])
            total += item[0]

        porcentagens = []

        for valor in valores_pizza:
            porcentagem = (valor*100)/total

            simbolo = '%'

            variavel_porcentagem = str(round(porcentagem, 2))
            variavel_completa = str(valor) + '\n' + variavel_porcentagem + '' + simbolo
            
            porcentagens.append(variavel_completa)

            
        
        ypoints = np.array(valores_pizza)
        xpoints = np.array(valores_x)

        
        self.ax.pie(ypoints, labels=porcentagens)
        self.ax.set(title=titulo_grafico)
        self.ax.legend(valores_x, loc='best', bbox_to_anchor=(-0.6, 0.25, 0.5, 0.5))

#Grafico de barras
class Grafico_barras(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(7, 4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

#Dados do gráfico
        xpoints = np.array(valores_x)
        ypoints = np.array(lista_valores)


        cores = []  
        
        x = np.arange(len(xpoints))
        

        ys = [i+x+(i*x)**2 for i in range(len(parametros))]

        colors = cm.rainbow(np.linspace(0, 1, len(ys)))
        for y, c in zip(ys, colors):
            cores.append(c)
        
        
        for sec in x:
            numero_parametros = len(lista_valores[sec])
            widthb = 0.8/numero_parametros
            width = -((numero_parametros * widthb)/2)

            for posicao in range(numero_parametros):
                self.ax.bar(x[sec] + width + (widthb/2), ypoints[sec][posicao] , width = widthb, color=cores[posicao])
                width += widthb

        for g in x:
            for index, value in enumerate(ypoints[g]):
                self.ax.text(index, value,
                         str(value))

        self.ax.set(xlabel=titulo_coluna, ylabel=titulo_linha, title=titulo_grafico)
        self.ax.set_xticks(x)
        self.ax.set_xticklabels(xpoints)
        self.ax.legend(parametros, loc='best', bbox_to_anchor=(0.9, 0.55))

#Grafico de linhas
class Grafico_linha(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(7, 4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

#Dados do gráfico
        rep = 0
        while rep != len(lista_valores):
            xpoints = np.array(valores_x)
            ypoints = np.array(lista_valores[rep])
            self.ax.plot(xpoints, ypoints)
            self.ax.legend(parametros)
            rep+=1
        self.ax.grid(True)
        self.ax.set(xlabel=titulo_coluna, ylabel=titulo_linha, title=titulo_grafico)
        

class AppGrafico(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(titulo_grafico)
        self.resize(1400, 800)
        
        if tipo_grafico == 'barras':
            chart = Grafico_barras(self)
        elif tipo_grafico == 'pizza':
            chart = Grafico_pizza(self)
        elif tipo_grafico == 'linhas':
            chart = Grafico_linha(self)
        
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
                    parx = param.rstrip('\n')
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
                        if re.search('\\b,\\b', first, re.IGNORECASE):                  
                            first = first.replace(",", ".")
                            lista_elementos.append(float(first))
                        else:
                            lista_elementos.append(float(first))
                    else:
                        if re.search('\\b,\\b', val, re.IGNORECASE):                  
                            correcao = val.replace(",", ".")
                            lista_elementos.append(float(correcao))
                        else:
                            lista_elementos.append(float(val))
                t += 1
                lista_valores.append(lista_elementos)

            self.pushButton.clicked.disconnect(self.open_dialog_box)
            self.pushButton.clicked.connect(self.open_dialog_box)
            self.janela = AppGrafico()
            self.janela.showMaximized()
            

if __name__ == '__main__':
     import sys
     app = QtWidgets.QApplication(sys.argv) 
     window = TelaInicial()
     window.show()
     sys.exit(app.exec_())
