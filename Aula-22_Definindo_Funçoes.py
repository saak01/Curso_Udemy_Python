 #Funções 
"""
-Funções são pequenos trechos de codigo que realizam tarefas especificas;
-Podem ou não receber entrada de dados e retornar uma saida de dados
-São muito uteis para executar procedimentos similares várias vezes.

OBS: Se você escrever uma função que realiza várias tarefas dentro deles,
é bom fazer um revisão para deixar simplificada.

Já utilizamos várias funções como: prin(),sum(),count(),len(),min(),max()

#Exemplos de funcionamento de Funções

    #1-built in são funções integradas no python
    -São funções como: print(),len(),etc

# DRY - Dont Repeat Yourself/Não repita codigo

Em python, a forma geral de definir uma função:

def nome_função(paramentros_utilizados):
    bloco da função

OBS# 
-nome de função sempre com letrasminusculas, e se for composto separado por under line (snake_case)
-parâmetros de entradas são opcionais
-bloco da função é onde o processo da função ocorre e neste bloco pode retornar ou não
-para definir uma função é utilizado "def" e abrir o bloco com ":"

#Definindo a primeira função
    def diz_oi():
    print('oi')
#OBS:
    -Dentro de uma função pode se usar outra função.

diz_oi() #chamada da função

#Atenção!!!! :

    -Para chamar a função é necessário o uso do parenteses: 
    -Nao existe um espaço entre o nome da função e o paranteses.

#Pode se usar for para função
def cantarparabens():
    print("Parabens pra você")          

for i in range(1,11):
    cantarparabens()



"""


