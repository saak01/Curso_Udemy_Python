#Tuplas 

"""

1- Tuplas são representada por parenteses ()

2- Tuplas são imutáveis, ou seja, não podem excluir ou adicionar elementos nela.

# Tuplas são definidas pela virgula e não pelo uso dos parenteses.  

# Não existe método para adição e remoção em tuplas, pois são imutáveis.
    Não tem um modo de alteração.


#Desempacotamento de uma tupla
    Exemplo:
        tupla = ('Geek','Univerisity')
        escola,uni = tupla
        print(escola)
        print(uni)

#Os métodos : max(), len(), min(), sum() podem ser usados em um tupla

#Concatenação de Tuplas:
        tupla = (1,1,3,4,5,1,1)
        tupla2 = (2,3,1,5,6,3,2)
        tupla3 = tupla + tupla2  #TUPLAS SÃO IMUTAVEIS
        print(tupla)
        print(tupla2)
        print(tupla3)

#iterando valor na tupla mesma coisa que a Lista
    tupla = (1,1,3,4,5,1,1)
    for n in tupla:
        print(n)

    print()

    for indice,valor in enumerate(tupla):
        print(f"{indice}-{valor}")

#Slincing é o mesmo da lista
        meses = (1,2,3,4,5,6,7,8,9,10,11,12)
        print(meses[:1])

#Quando utilizar Tuplas
    #-Tuplas são mais rápidas do que lista;
    #-Tuplas deixam o código mais seguro;

#A tupla não tem Shallow copy


""" 
