import matplotlib.pyplot as plt
import numpy as np
import ler_info as li

#Abrir arquivo.txt e separar cada linha em uma lista. 
arq = open('info_g.txt', 'r')
info = (arq.readlines())

for element in info:
    if element[4:5] == '#':
        element_unico = li.grafico_pizza(element, info[2])
        element_unico.converter_dados_num()
""" 
Dados do gráfico
"""
y = np.array(li.lista_dados_num)

plt.pie(y, labels = li.colunas)
plt.legend(title = li.titulo)
plt.show() 