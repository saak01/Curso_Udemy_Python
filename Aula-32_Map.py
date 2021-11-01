"""
Map

- Com o map fazemos mapeamento de valores para função.


"""

import math

def area(r):
    """ Calcula a área de um circulo com raio 'r' """
    return math.pi * (r ** 2)

print(area(2))

#1- #Forma comum  para passar  vários parâmetros
    #Com o for
raios =  [2,4,5,6,7,8,9,9]
for r in raios:
    print(f'{area(r)}')

#Forma map

#2- # Map é uma função  que  recebe dois parâmetros : o primeiro função, Segundo é um iteravel/coleção de elementos
print('Map')
ra=map(area,raios)
print(list(ra))

#3- # Forma com lambda:
print('lambada')
lista=(list(map(lambda r:math.pi*(r**2),raios)))
print(lista)
print('List comprenshion')
#List compreshion /Imprime o resultado e coloca numa  lista, ou seja, Melhor  só usar o map nesse caso.
print([ar for ar in lista])

#Map
    #Para fixar
#- O map  faz a seguinte tarefa, ele pega a função(pode se usar lambda, na verdade é o mais recomendado) como parametro e a coleção de dados desejada um interavel, assim é criado um objeto que pode ser colocado em um tipo de coleção nova