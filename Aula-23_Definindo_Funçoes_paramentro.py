#Funções com parâmetro
"""

-Funções que recebem dados para serem processados dentro da mesma. Esses dados são chamados de parâmetros. Os parâmetros são separados por virgula.

->Entrada de dados 
->processamento 
->saida


def quadrado_7():
    return 7 * 7

print(quadrado_7())

    #Refatorando

        def quadrado(num):
            return num*num

        print(quadrado(8))

#Uma função pode receber vários parâmetros #Mas se informar um numero errado de parâmetros é gerado um Type error

    Exemplo:
            def soma(a,b):
            return a + b

        print(soma(1,4))

#-Parâmetros são variaveis são declaradas na definição de uma função
#-Argumentos são dados passados durante a execução

def soma(a,b):#Parametros
    return a + b

# A ordem dos parâmetros importadas

print(soma(1,4)#Argumentos)

# Argumentos nomeados(Keyword Arguments)

        def nome_completo(nome , sobrenome  ):
            return (f'Seu nome completo é {nome} {sobrenome}')

        print(nome_completo('Angelina','Jolie'))
        print(nome_completo(nome='Marques',sobrenome='Marcia'))

////

Parametros padroes podem ser executados caso o paramentronão seja passado:
    #Pode se usar qualquer tipo de dados

    -Permite ser mais flexivel 
    -Evita erros com parâmetros incorretos
    -Permite trabalhar com  exemplos legiveis no codigo.


        Exemplo:

def soma(a=2,b=2):
    return a+b


print(soma())
#resutado é 4

print(soma(1,4))

#resultado é 5

#Deste modo percebece quando é passado o paramentro é possivel deixa-lo com um valor padrão assim resultando em menos erros.
    #Parâmetros default são colocados no final da declaração de parametros

def soma(a,b=2):
    return a+b

#Escopo - Evitar problemas e confusões
        -Variaveis globais


instrutor = 'geek' #Variavel geek

def diz_oi():
    return(f'oi {instrutor}')

print(diz_oi())

        -Variaveis Locais

instrutor = 'geek' 

def diz_oi():
    instrutor = 'Python' #Variavel local, pois faz parte de um escopo. SEMPRE vai ter preferencia
    return(f'oi {instrutor}')

print(diz_oi())

#Cuidado com variaveis globais, variaveis locais sobrepoe as globais sendo assim pode ocasionar o erro "Not defined"

#Podemos ter funções que são declaras dentro de funções e forma especial de escopo de variavel

"""

instrutor = 'geek' #Variavel geek

def diz_oi():
    return(f'oi {instrutor}')

print(diz_oi())


instrutor = 'geek' 

def diz_oi():
    instrutor = 'Python' #Variavel local, pois faz parte de um escopo. SEMPRE vai ter preferencia
    return(f'oi {instrutor}')

print(diz_oi())