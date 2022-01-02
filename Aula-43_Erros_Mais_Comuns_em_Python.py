"""
Erros Mais comuns em python:

-SyntaxError:
Ocorre quando existe um erro de sintaxe, exemplo: ao inves de print, foi executado "printf" este comando não é reconhecido pelo python
assim ocasionando um SyntaxError.

-Name error:
Ocorre quando uma variavel ou função não foi definida. Exemplo: 

print(geek)

Exemplo 2:

geek() ->uma função não existente.

-TypeError:
Ocorre quando uma função/operação/ação  é aplicada a um tipo  errado. Exemplo:

print(len(4))

-IndexError:
Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilzando index errado. Exemplo
nome = "joao"
print(nome[9])

-ValueError:
Ocorre quando uma função/operação built-in(integrada) recebe um argumento com tipo correto mas valor inesperado

Exemplo:
float("a")

-KeyError:
Ocorre quando tentamos acessar um dicionario com a chave incorreta.

dicionario = {"a":1}
print(dicionario["6"])

-Attribute Error:
Ocorre quando uma variavel não tem um atributo/função

Exemplo:
tupla= (1,3,5,6)
print(tupla.sort)   #Sort só pode ser usado com tupla, ou seja, a atribuição está errada.


-IndentationError:
Ocorre quando não respeitamos a indentação no python.

def novo():
print("lalala")



"""
dicionario = {"a":1}
print(dicionario["6"])

