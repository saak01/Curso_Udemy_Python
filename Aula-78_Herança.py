"""
Poo - Herança (inheritance)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
A ideia de herança é a de reaproveitar código. Também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, podemos extender outra classe que passa a herdar os atributos e metodos da classe herdada

Exemplo:

Cliente

    -nome
    -sobrenome
    -cpf
    -renda

Funcionario

    -nome
    -sobrenome
    -cpf
    -matricula
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Forma para herdar:

Quando uma classe herda de outra, classe herdade é conhecida como:
    -Super Classe
    -Classe mãe
    -Classe pai
    -Classe base

Quando uma classe herda de outra, ela é chamada:

    - Sub Classe;
    - Classe Pilha;
    - Classe Especifica

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Forma para herdar:

class Pessoa:
    
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nomecompleto(self):
        return f'{self.__nome} {self.__sobrenome}'

#Cliente Herda de pessoa
class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf,renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

fun1 = Funcionario('Joao Victor','Alves Costa','844231414141','42341')
print(fun1.nomecompleto())
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Sobrescrita de metodo, ocorre quando reescrevemos/reimplemetando um metodo presente na superclasse em classes filhas

Exemplo:






"""


class Pessoa:
    
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nomecompleto(self):
        return f'{self.__nome} {self.__sobrenome}'

#Cliente Herda de pessoa
class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf,renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda
    
class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nomecompleto(self):
        return f'id:{self.__matricula} '


fun1 = Funcionario('Joao Victor','Alves Costa','844231414141','42341')
print(fun1.nomecompleto())