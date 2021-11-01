#Conjuntos quando é falado em qualquer linguagem de programação é referenciado a teoria de conjuntos

"""
Em Python os conjuntos são chamados de Sets

-Sets (conjuntos), não possuem valores duplicados,
-Sets (conjuntos), não possuem valores ordenados,
-Elementos não são acessado via indice, ou seja, não são indexados.

#Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com 
a ordenação.

Os Sets(conjutos) são referenciados em python com {} Chaves.

#Diferença entre Sets e Dicionarios
    #Um dicionario tem chave e valor


#Definindo Conjutos 
    #Forma 1
        s = set({1,2,3,4,5,6,7,8,1,3,4,5,6}) #Repare que temos valores repetidos #As repetições não são colocadas
        print(s)
        print(type(s))


    #Forma 2 //Mais comum
        s = {1,2,3,4,5,6,7,8,9}
        print(s)
        print(type(s))

s = {1,2,3,4,5,6,7,8,9}

#Pode ser converter qualquer tipo de dados em Set(Ou seja, Conjunto.)Tupla/String/Lista/

#Podemos verificar determinado elemento dentro de set.

    s = {1,2,3,4,5,6,7,8,9}
    if 3 in s:
        print('Tem 3')
    else:
        print('Não')

#Importante lembrar que, alem de não ter valores duplicados, não temos ordem.
        Exemplo:
            li = [1,3,6,93,1,5,7,8,9]
            print(li)
            s = {1,3,6,93,1,5,7,8,9}
            print(s)


# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets:

    se = {1,'Ola',1.44,32,'Geek'}
    print(se)
    print(type(se))

# Iterar sets
    se = {1,'Ola',1.44,32,'Geek'}
    for todos in se:
    print(todos)

# Uso interessante com sets

# Cadastro de cidades de um estados e seus visitantes informam todo ano de onde ele vieram
        cidades = ['São Paulo','Cuiaba','Goias','Pará','São Paulo','Goias']
        cidades_resumo = set(cidades)
        print(cidades)
        print(cidades_resumo)
        print(len(cidades_resumo))

# Adicionando Conjunto
    s = {1,3,4,5}
    s.add(9)
    print(s)  //Se adicionar um elemento já existe ele ignora e não gera erro.

#Forma1  //Não usa index pois conjunto não é indexado
        #Nenhum valor é retornado

s = {1,3,4,5}
print(s)
s.remove(3)
print(s)

#Forma2
    #Nenhum valor é retornado
s = {1,3,4,5}
print(s)
s.discard(5)
print(s)  //Se o valor não é encontrado não é gerado erro

#Formas de copiar

#Deep Copy

s = {1,3,4,5}
novo = s.copy()
print(novo)

#Shallow Copy

s = {1,3,4,5}
novo = s
print(novo)

#Metodos set

# Clear() remove todos elementos em de um Set

#Metodos Matematicos de Conjuntos:
    #Precisamos juntar todos os estudantes

    #Forma 1 - Utilizando o union()

    estudantes_python = {'Mario','julia','Carlos','David','Juliana'}
    estudantes_java = {'Marlon','juliana','Carla','Darlin'}
    uniao = estudantes_java.union(estudantes_python)
    print(uniao)

    #Forma 2 - Utilizando a Barra reta.

        estudantes_python = {'Mario','julia','Carlos','David','Juliana'}
        estudantes_java = {'Marlon','juliana','Carla','Darlin'}
        uniao = estudantes_python | estudantes_java
        print(uniao)

# Gerar um conjunto de estudantes que estão em ambos os cursos
    Forma 1 - Utilizando o intersection
            
            estudantes_python = {'Mario','julia','Carlos','David','Juliana','Carla','Darlin'}
            estudantes_java = {'Marlon','juliana','Carla','Darlin'}
            ambos = estudantes_java.intersection(estudantes_python)
            print(ambos)

    Forma 2 - Utilizando o E-comercial

        estudantes_python = {'Mario','julia','Carlos','David','Juliana','Carla','Darlin'}
        estudantes_java = {'Marlon','juliana','Carla','Darlin'}
        ambos = estudantes_java & estudantes_python
        print(ambos)

# Estudantes que estão em um curso e nao em outro:

        estudantes_python = {'Mario','julia','Carlos','David','Juliana','Carla','Darlin'}
        estudantes_java = {'Marlon','juliana','Carla','Darlin'}

        sopython = estudantes_java.difference(estudantes_python)
        print(sopython)

# Mesmos metodos usados em listas,tuplas e dic são possiveis aqui:sum,max,min,len
"""

