"""
Poo - Herança Multipla

Herança Multipla nada mais é do que a possibilidade de uma classe herdar de multiplas calsses, fazendo om que a classe filha herda todos os atributos e metodos da classe herdada
--------------------------------------------------------------------------------------------------------------------------------------

OBS: Existe dusas formas de fazer multipla herança
    - Por Multiderivaçao Direta; #derivação é igual Pessoa(Seres Humanos)

    - Por Multiderivaçao Indireta;
--------------------------------------------------------------------------------------------------------------------------------------

#Exemplo de Multiderivação Direta


class Base1:
    pass


class Base2:
    pass

class Multirevidada(Base1,Base2):
    pass
--------------------------------------------------------------------------------------------------------------------------------------

#Exemplo de Multiderivação


class Base1:
    pass


class Base2(Base1):
    pass

class Base3(Base2):
    pass

class Multirevidada(Base3):
    pass
--------------------------------------------------------------------------------------------------------------------------------------

#Obs: Não importa se a derivação é direta ou indireta a Classe que realiza a herança todos os atributos  e metodos


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
print(tux.nadar())
print(tux.andar())
tatu = Terreste("Tutu")
print(tatu.andar())
print(tatu.cumprimentar())
baleia = Aquatico('Willy')
print(baleia.nadar())
print(baleia.cumprimentar())