"""
Entendo Iterators e Itereables


#Iterator - é um objeto de programação que pode ser iterado
          - Um objeto que retorna um dado, sendo um elemento por vez quando função next() é chamada

Exemplo de iterator:

string = "ola" ->iterable
para isso acontecer temos que usar a função iter(string)
it1 = iter(string)-> iterator 
print(next(it1))

-------------------------------------------------------------------------------------------------------------------------
#Iterable
           - Um objeto que ira retorna um iterator quando a função iter() for chamada

#Exemplo de Iterable:
String,tupla,dicionario,lista, conjuntos -> todos os tipos de "conjuntos estudados até agora"

string = "ola"
-------------------------------------------------------------------------------------------------------------------------
Por baixo dos panos, o for faz este processo.

Ele pega um iteravel, transforma em um iterator e depois usa o next()->"proximo em inglês"

"""
string = "ola"
print(next(string[0]))