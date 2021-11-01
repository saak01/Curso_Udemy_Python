#Entrada de dados
'''
----input()→ TODOS OS DADOS VINDO DO INPUT VEM EM STRING
E uma string é tudo que estiver entre aspas(simples,duplas e tripla)

Entrada usada no python 2.x
nome = input('Digite seu nome: ')
idade = input(str('Digite sua idade:'))
#Saida de dados
print('bem vindo(a)%s você tem %s anos'%(nome,idade))

#Entrada usada no python 3.x (forma antiga)
print('Bem vindo (a){0}, sua idade é {1}'.format(nome, idade))

#Entrada mais atual
print(f'Bem vindo(a){nome}, sua idade é {idade}.')
usando o 'f' na frente.

A vantagem do mais atual é poder usar o 'cast', Cast é a conversão de un tipo de dado para outro. Exemplo: de INT para STR
'''