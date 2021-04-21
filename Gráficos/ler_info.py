#Abrir arquivo.txt e separar cada linha em uma lista. 
arq = open('info_g.txt', 'r')
info = (arq.readlines())
titulo = info[1][4:]
x = info[2][4:]
y = info[3][4:]

#classe para colocar dados nos parâmetros necessários
class dados_grafico(object):
	def __init__(self, dado_num, dado_info):
		self.dado_num = int((float(dado_num[5:])))
		self.dado_info = dado_info[4:]

	def converter_dados_num(self):
		lista_dados_num.append(self.dado_num)
		coluna = lista_dados_num.index(self.dado_num) + 1
		colunas.append(self.dado_info + ' ' + str(coluna))

#listas com os dados organizados para o gráfico
lista_dados_num = []
colunas = []