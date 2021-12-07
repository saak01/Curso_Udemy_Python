"""
Filter


import statistics #biblioteca com dados estatisticos

#Dados calculados de algum sensor 
dados = [1.3,2.7, 0.8, 4.1, 4.3, -0.1]

#Calculando a media dos dados utilizados a função mean()
media = statistics.mean(dados)

# Como a função map, a filter recebe dois parametros. Sendo eles, uma função e um iteravel
#Resolução 1
res = filter(lambda x:x>media, dados)
            #função            #iteraveis, ou seja, dados.
print(list(res))

paises = ["", "Argetina", "Japao", "Brasil", "Chile", "Colombia", "Argeria"]
res = filter(None,paises)
            #none é uma função, deste modo filtrando os vazios
print(list(res))

# Outra forma de resolução
paises = ["", "Argetina", "Japao", "Brasil", "Chile", "Colombia", "Argeria"]
res = filter(lambda pais: len(pais)>0,paises)
print(list(res))

#Resolução 3

paises = ["", "Argetina", "Japao", "Brasil", "Chile", "Colombia", "Argeria"]
res = filter(lambda pais: pais != "", paises)
print(list(res))
"""

#Diferença entre map e filter é: 
#map: retorna um objeto mapeando a função para cada objeto do iteravel
#filter: retorna um objeto filtrado apenas com os elementos de acordo com a função
#este filtro ocorre por meio booleano, ou seja, True or False, Deste modo filtrando os iteraveis.

#Exemplo mais complexo
#forma 1
usuarios=[
{"username":"samuel", "tweets":["Adoro bolos","Adoro pizza"]},
{"username":"carla", "tweets":["Amo gatos"]},
{"username":"jeff", "tweets":[]},
{"username":"bob123", "tweets":[]},
{"username":"doggo", "tweets":["Adoro bolos","meu cachorro é lindo."]},
{"username":"gal", "tweets":[]}
]

#inativos = list(filter(lambda usuario: len(usuario['tweets'])==0,usuarios))

#print(inativos)

#forma 2

inativos = list(filter(lambda usuario: not usuario['tweets'],usuarios))
print(inativos)
##MEGA IMPORTANTE LEMBRAR
### not é uma especie de negação, neste caso do exercicios ele esta negando os tweets.

amigos = ["julia",'Caio','Jessyka','Joao']
amigos

#Como combinar filter e map

nomes = ["Vanessa","Ana","Maria"]

lista = list(map(lambda nome: f"Sua instrutora é {nome}",filter(lambda nome:  len(nome)<=5,nomes)))
print(lista)