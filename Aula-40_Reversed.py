"""

Reversed

OBS: Não confunda com a função reverse que estudamos nas listas!!!
reverse() só funciona com listas.



"""
#No caso de reversed é diferent. Ele funciona com qualquer tipo de interavel, mas seu retorno é um iteravel chamado List Reverse Iterator.
lista = [1,2,3,4,5,6]

res = reversed(lista)

print(type(res))
#Tipo do objeto
print(list(res))
#Conversão do iteravel para outro tipo, neste caso, uma lista.
#podemos fazer de outras formas tambem
    #Exemplo
print("".join(list(reversed("Geek University"))))

    #Outro é com slicing de string.

print("Geek University"[::-1])

#Pode se usar o reversed em loops exemplo:
for n in reversed(range(1,9)):
    print(n)

    #Forma mais pythonica e ideal é outra:
        #No caso essa:
for n in range(9,-1,-1):
    print(n)