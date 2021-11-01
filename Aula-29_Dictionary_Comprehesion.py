"""
Dictionary Comprehension

Pense no seguinte 

Se quisermos crirar uma lista fazemos:

lista = [1,2,3,4]

Se quisermmos criar um dicionario:

dicionario = {'a': 1 , 'b':2, 'c':3, 'd':4}

# Sintaxy

{chave:valor for valor in iteravel}

Exemplos:

numero = {'a': 1 , 'b':2, 'c':3, 'd':4}

quadrado = {chave:valor **2 for chave, valor in numero.items()}

print(quadrado)

Exemplo 2

chaves = 'abcde'
valores = [1,2,3,4,5]
                            #Pense sempre por aqui!!!!!!
res = {chaves[i]:valores[i] for i in range(0, len(chaves))}

print(res)

Exemplo com logica condicional

lista = [1,2,3,4]

res = {num:'par' if num % 2 == 0 else 'impar' for num in lista}

print(res)
"""

