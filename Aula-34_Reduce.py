"""
Reduce

Obs: A partir do python3 a função reduce() nao é mais uma função integrada ao python.

Conforme o criador do python Guido van Rossum:"Em todo caso, 99% das vezes um loop for é mais legivel "

Como funciona na pratica
"""

#Vamos usar a função reduce para multiplicar todos os números de uma lista

from functools import reduce

dados = [2,3,4,5,7,11,13,17,19,23,29]

multi = lambda x, y: x* y

res = reduce(multi,dados)

print(res)

#forma com for
res =1
for numeros in dados:
    res *= numeros

print(res)

#Forma com List Comprehension

