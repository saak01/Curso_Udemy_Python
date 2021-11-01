"""
#Kwargs

Poderiamos chamar este parâmetros de **xis, mas por convenção chamamos de **Kwargs

Este é só mais um parâmetro, nas diferente do 'args' que coloca os valores extras em uma tupla, o **kwargs
exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionario

# Exemplo 

def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas(carlos = 'Azul', marcelo = 'Verde', Elliot = 'Azul')


# Exemplo -2

def cores_favoritas(**kwargs):
    for nomes,cores in kwargs.items():
        print(f'A pessoa {nomes.title()} gosta da cor {cores} ')

cores_favoritas(carlos = 'Azul', marcelo = 'Verde', Elliot = 'Azul')

# Os paramentros 'args' e 'kwargs' não são obrigatórios.

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek']== 'Python':
        return 'Você recebeu um cumprimento pythonico'
    
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} oi!"
    
    return 'Não sei quem você é...'

print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(lilas='geek'))

#Nas funções podemos ter (NESTA ORDEM):

- Paramentros obrigatorios
- *args
- Parametros default (não obrigatorios)
- **kwargs

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek']== 'Python':
        return 'Você recebeu um cumprimento pythonico'
    
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} oi!"
    
    return 'Não sei quem você é...'

print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(lilas='geek'))
 

#Desempacotamento Lista,Tupla,Conjuntos *

def soma_kwargs(a,b,c):
    print(a+b+c)

lista =  [1,2,3]

tupla = (1,2,3)

conjunto = {1,2,3}

soma_kwargs(*lista)# * serve para desempacotar os elementos.

soma_kwargs(*tupla)# * serve para desempacotar os elementos.

soma_kwargs(*conjunto)# * serve para desempacotar os elementos.

#Desempacotamento **Dicionario
        #OBS: As chaves devem ter o mesmo nome que os parametros

dici = {'a' : 1 , 'b' : 2, 'c':3}
print('Dicionario a quantidade de * muda de 1 para 2')
soma_kwargs(**dici)# * serve para desempacotar os elementos

"""
