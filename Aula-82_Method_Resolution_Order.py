""" 
MOR - LPOO 

-É a ordem de execução dos métodos, ou seja, quem sera executado primeiro.
-----------------------------------------------------------------------------------------------------------------

Em python podemos conferir a ordem de execução dos métodos de tres formas:

1- Via propriedade da classe __mro__

2- Via método mro()

3- Via help 
-----------------------------------------------------------------------------------------------------------------
No caso da classe de exemplo abaixo, a ordem vai ser primeiro o metodo terrestre, pois na ordem ele foi o primeiro.




"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return (f'Eu sou {self.__nome}')

class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return  f'Eu sou {self._Animal__nome} e estou nadando.'

    def cumprimentar(self):
        return f'Eu sou o {self._Animal__nome} do mar'

class Terreste(Animal):
    def __init__(self,nome):
        super().__init__(nome)
    
    def andar(self):
        return f'Eu sou {self._Animal__nome} e estou andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra'

class Pinguim(Terreste,Aquatico):
    def __init__(self, nome):
        super().__init__(nome)

tux = Pinguim('Tux')
print(tux.cumprimentar()) #Por ter ocorrido uma herança multipla, o python escolheu a primeira classe declarada na herança multipla
