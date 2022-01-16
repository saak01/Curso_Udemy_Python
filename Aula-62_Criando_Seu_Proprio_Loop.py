"""
Criando sua própria versão de um iterator

"""

def repet(iteravel):
    tamanho = len(iteravel)
    iteravel  = iter(iteravel)
    cont = 0
    while True:
        print(next(iteravel))
        cont += 1
        if cont == tamanho:
            break

lista = [1,2,3,4,5]
repet(lista)