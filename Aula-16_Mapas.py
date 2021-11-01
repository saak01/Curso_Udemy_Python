#Mapas são conhecido como dicionarios em Python

"""
Interar com loopings

#For
        #Modo pythonico 

        receita = {'jan':'100','fev':'200','mar':'300'}
        for conteudo in receita.keys():
            print(receita[conteudo])

#For com Enumerate

    receita = {'jan':'100','fev':'200','mar':'300'}
    for indice,valor in enumerate(receita):
        print(f'{indice}-{valor}')

#Modo pythonico de acessar valores

    Keys() #Mostra todas as chaves contidas dentro do dicionario
    
        receita = {'jan':'100','fev':'200','mar':'300'}
        for conteudo in receita.keys():
            print(receita)

    Values() #mostra os valores
        
        receita = {'jan':'100','fev':'200','mar':'300'}
        for conteudo in receita.values():
            print(conteudo)

#Desempacotamento de Dicionarios 
    Usasse o metodo itens(). Assim para cada chave e valor 

    receita = {'jan':'100','fev':'200','mar':'300'}

    for cont in receita.items():
        print(cont)

#Podemos usar tambem os metodos len(),sum()#soma todos os valores, max()#define qual é o valor maximo,min() valor minimo

"""
