"""
Debugando  com PDB

PDB ->  Python Debugger

Bug ->  Inseto

Exemplo de praticas ruins

#OBS debugar codigo utilizando o print() para debugar pe uma pratica ruim.

def dividir(a,b):
    print(f"a={a},b={b}")
    try:
        return int(a) / int(b)
    except (ZeroDivisionError,ValueError):
        return "Ocorreu um Erro no seu programa."

        
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
print(dividir(num1,num2))


import pdb

nome = "Angelina"
pdb.set_trace()
sobrenome = "Jolie"
completo = nome + " " + sobrenome
print(completo)
"""

#Existe forma mais profissionais oara se fazer esse debug

#Exemplo com PDB

#Para utilizar o pdb precisamos da biblioteca pdb. Para assim, deste modo podemos usar o set_trace()

#COMANDOS basicos PARA PDB:
# "L" para listar onde estamos no codigo. list
# "N" para passar para proxima linha. next
# "P" imprime variavel. print
# "C" Finaliza o Debug
#  Para saber valor de variavel apenas digitar a variavel no pdb
#  Quando voce digita l, onde esta a setinha, ate a linha anterior esta executada. Deste modo pode-se 
#  Quando é necessario colocar dois comandos na mesma linhas utilizamos ";"

#Para uma melhor usabilidade ó pdb é usado  da seguinte maneira.

#Exemplo 3- a partir do python 3.7 o pdb foi implementado como uma função  built-in(função integrada), deste modo não é necessário usar import
nome = "Angelina"
breakpoint()
sobrenome = "Jolie"
completo = nome + " " + sobrenome   ########MODO RECOMENDADO##########
print(completo)