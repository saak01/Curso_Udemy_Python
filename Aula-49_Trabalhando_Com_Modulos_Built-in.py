"""
Trabalhando com Modulos Builtn (modulos integrados.)
#Quando instalamos o python todas esses modulos vem juntos, mas o import é necessário para não sobrecarregar o sistema.


#Utilizando alias"as", apelidos para funções/modulos
    # -Exemplo:

import random as rdm
print(rdm.random())
----------------------------------------------------------------------------------------------------------------------------------
#Pode -se também, importar várias funções usando "*", em outras palavras, todo o módulo.

-Exemplo:

from random import *
print(randint(1,10))
----------------------------------------------------------------------------------------------------------------------------------
#Apelidando funções. Segue o mesmo padrão da renomeação dos modulos com o alias "as".

from random import randint as rdmi
print(rdmi(1,10))

#Com várias funções:

from random import randint as rdmi, random as rdm
print(rdmi(1,10))
----------------------------------------------------------------------------------------------------------------------------------
#Quando é necessário usar várias funções de um módulo, usa-se tuplas para uma melhor organização

from random import(
    random,
    randint,
    shuffle,
    choice
)
#############FORMA PYTHONICA######################################################################################################
----------------------------------------------------------------------------------------------------------------------------------







----------------------------------------------------------------------------------------------------------------------------------




"""

