"""
Funções de maior grandeza - Higher Order Functions

O que isso  significa?

- Quando um linguagem de programação suporta HOF, 
indica que podemos ter funções que retornam outras funções como resultado ou mesmo que podemos passar funções como argumento para outras funções, 
e  até vairaveis do tipo funções

OBS: Usamos na aula de funções
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Exemplo:


def somar(a,b):
    return a + b

def diminuir(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def calcular(num1,num2,funcao):
    return funcao(num1,num2)

print(calcular(3,5,somar))
print(calcular(4,2,diminuir))
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Funções alinhadas

-Funções dentro de funções, ou, funções internas.

Exemplo:

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(["Some daqui","Salve rei", "Gosto muito de você"])
    return humor() + pessoa -> Nesse retorno é executado a função interna

print(cumprimento(" Rei"))
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Retornando funções de outras funçoes


from random import choice


def faz_merir():
    def rir():
        return choice(["kkkkkk","haduaghduiagduagd"])
    return rir ->retornando só o função sem ser executada

    #testando

rindo = faz_merir() 
print(rindo())-> Aqui é executada a função
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Inner Fuctions/ podem acessar o escopo de funções externas







------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


"""

from random import choice

def faz_merir(pessoa):
    def dandorisada():
        r = choice(("hahahah","lolo","lili"))
        return (f"{r} {pessoa}") # -> acessando a váriavel externa "pessoa"
    return dandorisada

rindo = faz_merir("Fernanda")
print(rindo())