"""
List Comprehension

-Utilizando List Comprehension nos podemos gerar listas com dados processados a partir de outro iteravel

# Sintaxe de List Comprehension  #Faz alteração de dados em uma lista sem tira-las de um lista.

[dado for dado in iteravel] #iteravel é uma COLEÇAO DE DADOS

#Exemplos

numeros = [1,2,3,4,5,6,7,8]

res = [numero * 10 for numero in numeros]
print(res)



Para enteder melhor o que esta acontecendo devemos dividir a expressçao em duas partes:

- A primeira parte: for numero in numeros

- Segunda parte: numero *10

#   List Comprehesion vs Loop


#   Loop

numeros = [1,2,3,4,5]
numerosdobrados = []
for num in numeros:
    numerosdobrados.append(num*2)

print(numeros)
print (numerosdobrados)

# List Comprehension

numeros = [1,2,3,4,5]
numerosdobrados = [num * 2 for num in  numeros]
print(numeros)
print(numerosdobrados)


# Outros Exemplos 

# 1 

nome = 'Geek University'

print([letras.upper() for letras in nome])

#2

amigos = ['maria','marcos','mario','ana','adalberto', 'Junior']
print([ amigo.title()  for amigo in amigos])

#3

print([ num*2 for num in range(1,10)])

Aula 2-----

Nos podemmos adicionar estrututars condicionaris logicas as nossas List Comprehension

numeros = [1,2,3,4,5]
pares = [pares for pares in numeros if not pares % 2]#
#Todo número 0 para o python é False, quando colocamos o not o False vira true e ele guarda o número

impares = [impares for impares in numeros if impares% 2]

print(impares)
print(pares)

"""
