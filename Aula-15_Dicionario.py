#Dicionario

"""
OBS: Em algumas linguagem de programação, os  dicionario Python são conhecidos por mapas.

#Dicinario são coleções do tipo chave/valor

print(type({}))

OBS: Sobre dicinario
    - Chave e valor são separados por dois pontos "chave : valor"
    - Tanto chance quanto valor poder ser de qualquer tipo de dado:
    - Podemos misturar tipos de dados:

# Criação de um dicionario

    Forma mais comum:
        paises = {'br' : 'Brasil', 'eua' : 'Estados Unidos', 'py' : 'Paraguai'}
        print(paises)
                #Usasse " :  " dois pontos entre a chave e o valor.

    -Forma menos comum de ser utilizadas:
        paises = dict(br = 'Brasil', eua = 'Estados Unidos', py = 'Paraguay')
            #Usasse " =  " e sem aspas em chave:

# - Acessando elementos
    # Forma 1:
        Acessando via chave, da mesma forma do que a lista e a tupla
            paises = {'br' : 'Brasil', 'eua' : 'Estados Unidos', 'py' : 'Paraguai'}
            print(paises['br'])
            #Acesso em chaves inexistentes é mostrado o "KEY ERROR"


    # Forma 2:
        Acessando via get, FORMA RECOMENDADA.
        paises = {'br' : 'Brasil', 'eua' : 'Estados Unidos', 'py' : 'Paraguai'}
        print(paises.get('br'))
        #Acesso em chaves inextistentes é usado o Tipo None, assim não deixando erro
    
    #Tipo None   #"None" desta forma
        -É conhecido como um tipo que não tem tipo, ou seja, vázio.
        -Utiliza-se None quando queremos inicializar uma váriavel sem tipo, assim só recebendo o titulo do valor final
            Tipo None sempre será False, ou seja, Falso.
    
    Exemplo para sempre ter um valor na lista:
   
    #Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada.
       
        paises = {'br' : 'Brasil', 'eua' : 'Estados Unidos', 'py' : 'Paraguai'}
        print(paises.get('bl','Não encontrado'))

        
    
    #Podemos verificar se determinada chave se encontra no dicionario
        OBS - Só vale para chaves e não para valor

    paises = {'br' : 'Brasil', 'eua' : 'Estados Unidos', 'py' : 'Paraguai'}
    print('br' in paises)
        True

    print('Estados unidos' in paises)
        False

#É interresante usar tuplas para construir as chaves de um dicionario, pos, elas são imutáveis.

#Formas de adicionar elementos em um Dicionario.
        #Forma mais comum
receita = {'jan':445, 'fev': 110, 'mar':334}
print(receita)
    #forma1
receita['abr'] = 350

    #forma2

novo_dados = {'mai':500}
receita.update(novo_dados)
print(receita)

#Atualizando dados em um dicionarios
    #Forma 1
receita['mar']=500
print(receita)

    #Forma 2

receita.update({'mai': 700})
print(receita)

#Conclusão, adicionar ou atualizar dados são usados os  mesmo codigos.
#Em dicionarios NAO pode ter chaves repetidas.

#Remover dados de um dicionario
receita = {'jan':445, 'fev': 110, 'mar':334}
print(receita)    
    #Forma1 MAIS COMUM
receita.pop('mar')
print(receita)
    #Obrigatorio passar a chave, e caso não encontrado é acionado um Key Error
        #Ao remover o objeto o valor é retornado. Igual o da lista.
        


    #Forma2
        #Neste caso o valor não é retornado.
del receita['fev']

#Dicionario é altamente recomendado quando esta trabalhando com tipos de dados onde se fosse indentificar
com indice levaria mais tempo do que o necessario. Assim o dicionario pode ser facilitador para esse
tipo de trabalho mais informativo.

#Metodos de Dicionario
    *clear()    
        Funciona para limpar um dicionario.

#Copiando dicionarios  #Funciona em qualquer sentido
    #Deep copy (Forma 1)
    
    d = {'a':1,'b':2,'c':3}
    novo = d.copy()
    print(d)
    print(novo)

    #Shallow copy
   
    d = {'a':1,'b':2,'c':3}
    novo = d #lembrando que desta forma, os dois dicionarios são alterados pois estão em ligação

#Forma não usual de criar dicts
    e = {}.fromkeys(['nome','email','senha',],'desconhecido')
    #A lista são as chaves, o que está fora da lista são os valores.
        # Só aceitando um valor para os valores e se tentar adicionar mais é gerado um TypeError
        # Só recebe 2 argumentos
            novo = {}.fromkeys(range(1,11),'novo')
            print(novo)


"""
