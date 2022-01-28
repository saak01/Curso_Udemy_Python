"""
Poo-Método Super
------------------------------------------------------------------------------------------------------------------
-O método super, se refere a uma super classe (classe base,classe mae, classe pai.)

#Com o método super podemos fazer acesso a qualquer elemento (atributos, metodos) da classe pai.

"""
class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self,som):
        print(f'O {self.__nome} faz {som}')


class Gato(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca

felix = Gato('Felix', 'Felino', 'Angora')

felix.faz_som('Miau')