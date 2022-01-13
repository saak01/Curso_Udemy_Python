"""
Pacotes

Modulo -> É um arquivo Python com várias funções para usar
Pacote -> É um diretorio contendo uma coleção de módulos: 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
OBS: Nas versões 2.x era necessário um pacote ter o sequinte arquivo "__init__", após a versão 3.x não é mas necessário mas ainda usado para evitar incompatibilidades.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Foi criado um diretório "pacotes" para poder fazer os exemplos e testes desta aula.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from pacote import (
    geek1,
    geek2
)
print(geek1.funcao1(1,1))
print(geek2.curso)
print(geek2.funcao2())
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Acessando sub-pacotes 

from pacote.subpacote import geek3 #ou seja, ele ta selecionando o modulo dentro do pacote usando esta linha "pacote.subpacote"
print(geek3.subpa())

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Importando funções especificas de um pacote

from pacote.geek1 import funcao1
print(funcao1(5,2))


"""
