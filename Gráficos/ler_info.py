#Abrir arquivo.txt e separar cada linha em uma lista. 
arq = open('info_g.txt', 'r')
info = (arq.readlines())
titulo = info[1][4:]
x = info[2][4:]
y = info[3][4:]

#calculo do total
total = 0
for element in info:
	if element[4:5] == '#':
		total += int(element[5:])

#classes para colocar dados nos parâmetros necessários para os respectivos tipos de graficos
class grafico_barras(object):
	def __init__(self, dado_num, dado_info):
		self.dado_num = int((float(dado_num[5:])))
		self.dado_info = dado_info[4:]

	def converter_dados_num(self):
		lista_dados_num.append(self.dado_num)
		coluna = lista_dados_num.index(self.dado_num) + 1
		colunas.append(self.dado_info + ' ' + str(coluna))

class grafico_pizza(object):
	def __init__(self, dado_num, dado_info):
		self.dado_num = int((float(dado_num[5:])))
		self.dado_info = dado_info[4:]

	def converter_dados_num(self):
		lista_dados_num.append(self.dado_num)
		coluna = lista_dados_num.index(self.dado_num) + 1
		porcentagem = str((100*self.dado_num)/total)
		print(porcentagem[:5])
		colunas.append(self.dado_info + ' ' + str(coluna) + '(' + porcentagem[:5] + '%' + ')')
#listas com os dados organizados para o gráfico
lista_dados_num = []
colunas = []