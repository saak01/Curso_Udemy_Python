"""
Teste de velocidade com Expressões geradoras.
----------------------------------------------------------------------------------------------------------------------------------
# Generators

def nums():
    for num in range(1,11):
        yield num

ge1 = nums()

print(next(ge1)) # Generator
----------------------------------------------------------------------------------------------------------------------------------
# Generator Expressiom

ge2 = (num for num in range(1,11))
print(ge2)
print(next(ge2))

----------------------------------------------------------------------------------------------------------------------------------
#Realizando o teste de velocidade 



"""


import time

#Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(10000000)))
gen_tempo = time.time() - gen_inicio
print(gen_tempo)
#List Comprehension

list_inicio = time.time()
print(sum([num for num in range(10000000)]))
list_tempo = time.time() - list_inicio
print(list_tempo)