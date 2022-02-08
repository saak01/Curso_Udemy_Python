"""
Polimorfismo - Poo
----------------------------------------------------------------------------------------------------------------------------------
Poli -> muitas
morfis -> formas

- Objetos que podem se comportar de formas diferentes.
----------------------------------------------------------------------------------------------------------------------------------
Quando ocorre uma reimplementação de um metodo presente na classe pai em uma classe filha, estamos fazendo um overriding(sobrescrita), sobrescrita é a melhor representação de polimorfismo.
"""

class Animal():
    def __init__(self,nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar')#

    def comer(self):
        print(f'{self.__nome} está comendo.')

class Cachorro(Animal):

    def __init__(self,nome):
        super().__init__(nome)

    def falar(self):
        return(f'{self._Animal__nome} fala : au...au..')

class Rato(Animal):

    def __init__(self,nome):
        super().__init__(nome)


dog = Cachorro("Rex")

print(dog.falar())