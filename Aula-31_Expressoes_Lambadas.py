"""
Utilizando Lambdas

#OBS:  LAMBDA SEMPRE USARA O RETURN!!! NÃO ESQUECER!!!

Conhecidas por expressões Lambdas, ou simplesmente Lambdas são funções sem nome, ou seja funções anonimas


/////////////////////////////////////////////////////////////////////


    #Função em Python

def calcular(x):
    return x * 3 + 1

print(calcular(4))

    #lambda

resultado = lambda x: 3 * x + 1
print(resultado(4))


# Podemos ter expressões lamdas com multiplas entradas/parâmetros.
    
    #Lambda

nome_completo = lambda nome,sobrenome: nome.title().strip()+' '+sobrenome.strip().title()
print(nome_completo('Joao Victor','Alves Costa'))



    #Funções
def retornar_nome(nome,sobrenome):
    return nome.title().strip() + ' ' + sobrenome.strip().title()

print(retornar_nome('João Victor','Alves Costa'))


#Com o for

for sobrenome in autores:
    sobrenome = sobrenome.split(' ')
    print(sobrenome[-1].title())


#Com lambda
print()

autores = ['Leonardo Di Caprio','Angelina Jolie','Robert D. Junior','Brad Pitt']

print(autores)
#Videos estava desatualizado. Tem que colocar o tipo de coleção e passar a ,
sorted(autores,key= lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

#Aplicação
    Geralmente para filtrar dados e ordenação.

"""


