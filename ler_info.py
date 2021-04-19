#Abrir arquivo.txt e separar cada linha em uma lista. 
arq = open('info_g.txt', 'r')
info = (arq.readlines())

#Printar informacoes
print(info[0], info[1], info[2])

#classe para colocar dados nos parâmetros necessários
lista_dados = []
class dados_grafico(object):
	def __init__(self, dado):
		self.dado = int((float(dado[5:])))

for element in info:
	if element[4:5] == '#':
		dado_convertido = dados_grafico(element)
		lista_dados.append(dado_convertido.dado)

print(lista_dados)