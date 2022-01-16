"""
Criando sua própria versão de um iterator
-------------------------------------------------------------------------------------------------------------------------------
#Minha versão de um iterável
def repet(iteravel):
    tamanho = len(iteravel)
    iteravel  = iter(iteravel)
    cont = 0
    while True:
        try:
            print(next(iteravel))   NUNCA ESQUECER DE TRATAR OS ERROS!!!!!!!!!!!!!!
            
        except StopIteration:
            break

lista = [1,2,3,4,5]
repet(lista)
-------------------------------------------------------------------------------------------------------------------------------
#Versão do pro

#Minha versão de um iterável
def meufor(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        
        except StopIteration:
            break

-------------------------------------------------------------------------------------------------------------------------------

"""

