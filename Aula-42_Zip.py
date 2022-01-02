"""
Zip 

zip() -> Cria um iteravel (Zip Objetc) que agrega elementos de cada dos iteraveis passados como entrada em pares 

#Exemplos:

lista1 = [1,2,3]
lista2 = [4,5,6]
#Com Lista
print("Lista")
print(list(zip(lista1,lista2)))
#Com Tupla
print("Tupla")
print(tuple(zip(lista1,lista2)))
#Com set
print("Set")
print(set(zip(lista1,lista2)))

#O zip utiliza como tamanho o menor paramentro como iterável. Isso significa que, quando estiver trabalhando com 
iteraveis de valores diferentes, o  "break" sera no menor.
lista1=[1,2,3,4]
lista2=[55,3,4]
lista3=[44,3,4,3,321]
zips = zip(lista1,lista2,lista3)
print(list(zips))
 #Pode-se usar varios tipos de iteraveis com o zip.
        #Revisao: Para descompactar um conjunto de iteraveis é usado o *, deste modo segue o exemplo com o zip:

"""
dados = [(0,1,2), (3,4,5),(6,7,8)]
print(dados)
print(*dados)

#Exemplo mais complexos:

prova1 = [80,91,78]
prova2 = [98,89,53]
alunos = ['Pedro','Maria','Carlos']
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos,prova1,prova2)}
print(final)
 #Podemos utilizar map():

final= zip(alunos,map(lambda nota: max(nota,zip(prova1,prova2))))
print(dict(final))