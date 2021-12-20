"""

Continuação

# A forma certe de puxar os valores para retorno em qualquer função é dessa forma.
#Usa-se values()
from typing import KeysView


numeros_dict = {"a":1,"b":8,"c":34,"d":3,"e":2,"f":1}
print(max(numeros_dict.values()))#max -> Retorna o maior número da lista
print(min(numeros_dict.values()))#min -> Retorna o maior número da lista

#Faça um programa que receba dois valores e do usuario e mostre o maior valor:
valor1=int(input("Digite o primeiro valor: "))
valor2=int(input("Digite o primeiro valor: "))
print(max(valor1,valor2))

#Max pode ser usado tmb com string
#Exemplo:
print(max("a","b","g","d"))#desta forma o maior sempre o ultima letra do alfabeto composta no iteravel. Neste caso, a letra "G"
print(max("aew","das","cfs","d"))#desta forma o maior sempre o ultima letra do alfabeto composta no iteravel. Neste caso, a letra "das"

# Da mesma forma podemos fazer com float.
print(max(1.14,1.55,2.45))

#min() -> Ira fazer o inverso do max. A função min() sempre ira retornar o menor valor dentro de variaveis ou iteraveis.

nomes = ["Arya", "Samson", "Dora", "Tim", "Ollivander"]

print(max(nomes))#Tim
print(min(nomes))#Arya  #Foi seguido pela ordem alfabetica sendo t o maior numero/mais distante e A sendo o menor
print()
#Para pegar com o maior indice e menor é desta forma
print(min(nomes, key=lambda nome: len(nome)))#Tim
print(max(nomes, key=lambda nome: len(nome)))#Ollivander

"""

#Desafio

musicas = [
{"Titulo":"Thunderstrunk","tocou":3},
{"Titulo":"Seila","tocou":8},
{"Titulo":"Quadro-Doka","tocou":10},
{"Titulo":"Blackout","tocou":1},
{"Titulo":"Mustang Preto","tocou":22},
{"Titulo":"Thing out loud","tocou":12}
]
#Desafio é mostrar somente o titulo da musica:
#Primeiro metodo:
musica1=(max(musicas, key= lambda musica: musica["tocou"]))
musicas2=(min(musicas, key= lambda musica: musica["tocou"]))
print(musica1['Titulo'])
print(musicas2['Titulo'])
#Outra forma mais eficiente é deste modo
print((max(musicas, key= lambda musica: musica["tocou"]))["Titulo"])
print((min(musicas, key= lambda musica: musica["tocou"]))["Titulo"])
# O que acontece neste caso é o seguinte. Apos setar o objeto desejado ele escolhe qual chave mostrar.
print((max(musicas, key= lambda musica: musica["tocou"]))["Titulo"])
print((min(musicas, key= lambda musica: musica["tocou"]))["Titulo"])
print()
#desafio sem usar max e min
max = 0
for music in musicas:
    music["tocou"] > max
    max = music["tocou"]

for music in musicas:
    if music["tocou"] == max:
        print(music['Titulo'])