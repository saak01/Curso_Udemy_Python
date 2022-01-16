"""
#REVER#

Geradores-Generators

- Generator são iterators (iteradores)

OBS: O contrarío não é verdadeiro, ou seja, nem todo iterator é um generator

Outras informações:

- Generators podem ser criados com funções geradoras:
- Funções Geradoras Utilizam a palavra reservada yield:
- Generators podem ser criados com exepressão geradora
------------------------------------------------------------------------------------------------------------------------------------------
- Diferença entre funções e  Generators Functions (funções geradoras)
------------------------------------------------------------------------------------------------------------------------------------------
/Funções                        /        Generator Functions
------------------------------------------------------------------------------------------------------------------------------------------
/utilizam return                /             Utilizam yield
------------------------------------------------------------------------------------------------------------------------------------------
/retorna uma vez                /       Podem utilizar yield multiplas vezes
------------------------------------------------------------------------------------------------------------------------------------------
/Quando executada retorna um valor /    Quando executada retorna um generators.  
------------------------------------------------------------------------------------------------------------------------------------------

#Exemplo de Generator Fuction

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador #yield sempre aguardara o proximo next()
        contador = contador +1
#Uma generator Fuction não é um generator. Era gera um generator.
gen = conta_ate(5)
print(next(gen))

gen = list(conta_ate(10))
print(gen)

------------------------------------------------------------------------------------------------------------------------------------------

"""

