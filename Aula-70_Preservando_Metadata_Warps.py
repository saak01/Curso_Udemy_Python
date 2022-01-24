"""
Preservando metadas

metaddados -> São dados intrisecos em arquivos

wraps -> são funções que envolvem elementos com diversas finalidades
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Problema com meta-datas





"""
#Quando é usado o decorator, o doc pode vir a dar a documentação do decorator ao inves da  documentação certa da função
#Para resolver isso importamos o wraps. Exemplo:
from functools import wraps

def ver_log(funcao):
    @wraps(funcao)#wraps funciona como um decorator, por isso foi passado a função como parâmetro novamente. 
    def logar(*args,**kwargs):
        """ Eu sou uma função dentro de logar"""
        print(f"Voce está chamando a função {funcao.__name__}")
        print(f"Aqui é a documentação: {funcao.__doc__}")             
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a,b):
    """ soma numeros"""
    return a + b

print(soma.__doc__)

