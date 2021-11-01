#Listas
"""
As listas são a mesma coisa que arrays em outras linguagens, a difereça é que no python não é necessário
tamanho fixo.Ou seja, é dinâmico.

Lista são representada por conchetes "[]"

#sort()
o metodo sort() foi explicado.
Sort serve para ordenar itens dentro de uma lista, sendo eles string ou numeros

#count()
conta elementos em uma lista

#append()
Adiciona qualquer item em uma lista.
Só podendo adicionar um elemento por vez.
para colocar vários
    -Exista varios jeitos de colocar itens dentro de uma lista
    1 - colocando um append com outra lista dentro, e colocando todos itens desejados lá
    
        print(lista1)
        lista1.append([33,45,6,788,9])
         print(lista1)

    2 - extend()
    usando o metodo extend(), onde conseguimos colocar todos os itens e o metodo faz o trabalho
    de adicionar um por vez, assim mantendo só uma lista.
    print(lista1)
    ###NÂO esqueça de nas duas formas colocar os conchetes para ainda ser um argumento para a função.
    
    lista1.extend([1,3,4,6,8,98,75,4,])
    print(lista1)

#Insert
    O insert é usado para adicionar valores em uma lista também, mas recebe dois parametros para isso. 
    o indice que é desejado colocar o valor, e o valor em si. Ex:

        lista1.insert(2,44)

    NÃO É UMA SUBSTITUIÇÃO, O VALOR QUE ESTAVA NESTE INDICE IRA PRA DIREITA(OU SEJA, SERA O PROXIMO INDICE)

#Juntar todas as listas em uma 
    É possivel de uma forma bem simples, deste modo:
        
        lista6 = lista1 + lista5
        print(lista6)

    Ou metodo extend() funciona muito bem tambem, vai do usuario escolher qual usar.

#Podemos facilmente inverter uma lista, existe duas formas para fazer esse tipo coisa:
    
    1°Primeiro metodo
        USANDO reverse()
        lista1.reverse()
    
    2°Primeiro metodo
        Fatiamento de lista:
        lista1[::-1]

#Copiar uma lista
   
    lista7 = lista1.copy()
    print(lista7)

#Tamanho tem numa lista basta usar o metodo len()
    
    print(len(lista1))

#Excluir o ultimo elemento de uma lista
    Não somente remove o ultimo numero como tambem retorna na função (return).
    Usando o metodo pop()
        
        lista1.pop()

    #podemos remover o elemento pelo seu indice tambem com o pop:
        
        lista1.pop(2)

#Podemos repetir elementos de uma lista da seguinte forma:
nova = lista1 *3

#split()
    separa os elementos da lista pelo espaço que tem entre eles.

#Iterando listas
    #Utilizando o for
    soma = 1
    for elementos in lista1:
        print(elementos)
        soma += elementos
    print(soma)

#fazendo acesso de elemento de forma indexada
    cores = ["amarelo","azul","laranja","vermelho","preto","cinza"]
    print(cores[1])
    azul
#fazendo acesso de elemento de forma indexada
    cores = ["amarelo","azul","laranja","vermelho","preto","cinza"]
    print(cores[-1])
    cinza
##Revisão
cores = ["amarelo","azul","laranja","vermelho","preto","cinza"]
#forma com for
for elementos in cores:
    print(elementos)
print()
#forma com wihle
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice +=1

#gerar indice em um for
for indice,elemenots in enumerate(cores):
    print(f"{indice}-{elemenots}")

#Listas aceitam repetições

#encontrar indice em uma lista:
    para descobrir é  usado o metodo  index():
    print(lista1.index(55))
    
    #retorna o elemento do primeiro elemento encontrado

    #pode tambem fazer buscas com um range definido
    print(lista1.index(55,1))
    Buscando o numero 55, a partir do index 1
    #tmb com um valor inicial e final
    print(lista1.index(55,1,9)

#Revisão de Slice ou Fatiamento 

string[inicio:fim:passo]

#Para somar itens em uma lista use o metodo sum()
    #so pode ser usado em elementos tipo inteiro ou float  
        
        print(sum(lista1))

#Para saber o maior numero em uma lista use o metodo max()
    
    print(max(lista1))

#Para saber o minimo numero de uma lista use o metodo min()
    
    print(min(lista1))

#Transformar uma lista em tupla 
    tupla = tuple(lista1)

Copiando uma lista para outra (Shallow Copy e Deep Copy)

#1 forma Deep copy

    lista = [1,3,5,6,8,5,3,2,6]
    nova = lista.copy()
    nova.append(4)

#Usando o copy as listas se tornam idenpendentes uma das outras, sendo assim um elemento adicionado
ou alterado em qualquer umas das listas não altera a outra, isso se chama Deep Copy

#2 forma Shalloww Copy
    
    lista = [1,3,5,6,8,5,3,2,6]
    nova = lista

#Esse tipo de lista quando é alterado um valor em alguma lista, ocorre a mudança de valor em ambas. Isso
# se chama Shallow Copy    


"""


lista1 = [1, 44, 55, 32, 51, 66, 11, 44, 31,1,1,1,1]

lista2 = ['G', 'e', 'e', 'k', 'u', 'i']

lista3 = []

lista4 = list(range(10))

lista5 = list('Geek University')

lista6 = lista1 + lista2

cores = ["amarelo","azul","laranja","vermelho","preto","cinza"]

print(sum(lista1))