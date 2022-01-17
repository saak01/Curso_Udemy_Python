"""
Decorators com diferent assinaturas

Exemplo:

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return (f"Ola, eu sou o {nome} ")

@gritar
def ordernar(principal, acompanhamento):
    return f"Olá eu gostária de {principal}, acompanhado de {acompanhamento} por favor."

#print(saudacao("Angelina"))
-----------------------------------------------------------------------------------------------------------------------------
#Erro com parâmetros:

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return (f"Ola, eu sou o {nome} ")

@gritar
def ordernar(principal, acompanhamento):
    return f"Olá eu gostária de {principal}, acompanhado de {acompanhamento} por favor."

#Problema com Parâmetro
#Para resolver,utilizamos um padrão de projeto chamado decorator pattern

print(ordernar("Picanha","Batata Frita"))

-----------------------------------------------------------------------------------------------------------------------------

Refatorando com Decorators Patterns

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args,**kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return (f"Ola, eu sou o {nome}")

@gritar
def ordernar(principal, acompanhamento):
    return f"Olá eu gostária de {principal}, acompanhado de {acompanhamento} por favor."

print(ordernar("picanha","batata"))
-----------------------------------------------------------------------------------------------------------------------------
A assinatura de uma função é representada pelo seu retorno e parâmetro  de entrada

assinatura da função ordenar: ordernar,principal
-----------------------------------------------------------------------------------------------------------------------------
Obs: Vale lembrar que podemos utilizar parâmetro nomeados


-----------------------------------------------------------------------------------------------------------------------------
#OBS Vale lembrar que podemos usar parâmetros noemados/defaults

def ordernar(principal= 'Batata Frita', acompanhamento= 'Picanha'):
-----------------------------------------------------------------------------------------------------------------------------
#Podemos ter decorators com parâmetros de entrada

exemplo:


def verifi_primeiro_argumeto(valor):
    def interna(funcao):
        def outra(*args,**kwargs):
            if args and args[0] != valor:
                return f"Valor incorreto, Primeiro valor do argumento precisa ser {valor}"
            return funcao(*args,**kwargs)
        return outra
    return interna

@verifi_primeiro_argumeto("pizza")
def comida_favorita(*args):
    print(args)

@verifi_primeiro_argumeto
def soma_dez(num1, num2):
    return num1 + num2

print(comida_favorita("pizza","pepino"))


"""


