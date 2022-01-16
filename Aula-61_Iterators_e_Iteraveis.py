"""
Entendo Iterators e Itereables


#Iterator - é um objeto de programação que pode ser iterado
          - Um objeto que retorna um dado, sendo um elemento por vez quando função next() é chamada

Exemplo de iterator:

string = "ola" ->iterable
print(string[0]) ->iterator
-------------------------------------------------------------------------------------------------------------------------
#Iterable
           - Um objeto que ira retorna um iterator quando a função iter() for chamada

#Exemplo de Iterable:
String,tupla,dicionario,lista, conjuntos -> todos os tipos de "conjuntos estudados até agora"

string = "ola"


"""
string = "ola"
print(next(string[0]))