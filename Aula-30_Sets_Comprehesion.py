"""
Set comprehension 

Exemplos:

"""
numeros = {num for num in range(1,10)}
print(numeros)

# Outros exemplo 

num = {x **2 for x in range(1,10)}

print(num)

#Desafio faça uma alteração nessa estrutra para transformar em  um dicionario:

num = {x:x **2 for x in range(1,10)}
print(num)

# Pra finalizar

letras = {letra for letra in 'Geek University'}
print(letras) #SET e dicionario não tem repetição e no caso do set não tem uma ordenação.