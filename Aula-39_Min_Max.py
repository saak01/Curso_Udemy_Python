"""
 Min e Max

max() -> Retorna valor em um iteravel ou a maior de dois ou mais elemento 

#Exemplos

"""
#Min e max funcionam em qualquer tipo de iteravel
numeros = [1,8,34,3,2,1]
print(max(numeros))#max -> Retorna o maior número da lista
print(min(numeros))#min -> Retorna o menor número da lista
#Tuplas
numeros_tuplas = (1,8,34,3,2,1)
print(max(numeros_tuplas))#max -> Retorna o maior número da lista
print(min(numeros_tuplas))#min -> Retorna o menor número da lista
#Conjunto
numeros_conjunto = {1,8,34,3,2,1}
print(max(numeros_conjunto))#max -> Retorna o maior número da lista
print(min(numeros_conjunto))#min -> Retorna o maior número da lista
#Dicionario
numeros_dict = {"a":1,"b":8,"c":34,"d":3,"e":2,"f":1}
print(max(numeros_dict))#max -> Retorna o maior número da lista
print(min(numeros_dict))#min -> Retorna o maior número da lista
#No caso do dicionario temos que setar o que desejamos, se não ele mostrar a chave com o maior valor,
#deste modo o certo é:  #values valor:
print(max(numeros_dict.values()))#max -> Retorna o maior número da lista
print(min(numeros_dict.values()))#min -> Retorna o maior número da lista

