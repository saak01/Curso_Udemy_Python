"""
#Listas Aninhadas

- Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:

    - Unidimencional (Arrays,Vetores):
    - Multidimensionais (Matriz):

Em python nís temos as Listas:

numeros =  [1,'b',3.234,True]


listas = [[1,2,3],[4,5,6],[7,8,9]]# Matriz 3 x 3
            #0       #1      #3
# Como fazemos para acessar os dados?


 

#Iterando com loops com uma lista aninhada

for lista in listas:
    for numero in lista:
        print(numero)

# List Comprehension

[[print(valor) for valor in lista]for lista in listas]

"""

# Gerando valores iniciais

print([['*' for i in range (1,4)]for j in range(1,4)])