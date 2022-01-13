"""
Modulo Random  e o que são os modulos ?

- Em Python nada mais são  do que outros arquivos python

Modulo Random -> Possue várias funções para números pseudo-aleatórios

Existe duas formas de importar um modulo ou função

modo 1:

        #Todas as funções, atributos, classes ficaram disponiveis nessa forma, ou seja, em memoria.

import random # Nessa primeira forma você importa todo o modulo, desta forma precisando especificar a função desejada:(NÃO RECOMENDADO.)
random.choice()

modo 2:

from random import choice   #Desta forma já foi importado a função, então não é necessário o especificar.

#########################################################RELEMBRANDO##############################################################

-Existe um modo de visualizar todas as funções de um modúlo. Exemplo-1:

import random
print(dir(random))

Exemplo 2:

Inicie o python no terminar e só utilize:

import random
dir(random)
---------------------------------------------------------------------------------------------------------------------------------
Para consultar documentação de alguma função dos modulos é simples:
Exemplo(Com o Python3 no Terminal):

import random
help(random.random)

####################################################################################################################################

random -> Gera um pseudo-numero aleatorio entre 0-1

OBS: não confunda as funções com pacotes/modulos

uniform() -> Gerar um pseudo-número aleatorio com limites pré estabelecidos
#Exemplo:

        #Uniform gera um número com muitas casas decimais. Dependendo da escolha é melhor utilizar o "randint"

from random import uniform 
print(uniform(1,10)) -> Lembrando que sempre o ultimo número (nesse caso o "10" não ira ser gerado.)


randint() -> Como o uniofrm, está função gera pseudo-numeros aleatórios com limites pré estabelecidos com parametros.

#Exemplo:


from random import randint
print("Números da Mega Sena")
for numeros in range(1,8):
        print(f"{randint(1,61)}",end=", ")

#OBS: end não deixa quebrar a linha e podemos selecionar o que colocaar entre os espaços

choice() -> Choice é uma função de escolha, dessa forma precisa-se de um iteravel para o choice fazer a seleção.

shuffle() -> Tem a função de embaralhar os dados
#Exemplo:

from random import shuffle
dados =[1,2,3,4,5,6,7,8,9]
shuffle(dados)
print(dados)


"""
