#ler informações gerais

arq = open('info_g.txt', 'r')

info = (arq.readlines())

print(info[2], info[3])

'''for linha in info:
    print(linha)
'''
