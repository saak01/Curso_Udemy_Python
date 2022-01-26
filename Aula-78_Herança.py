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
    def __init__(self, nome, sobrenome, cpf, funcionario):
        super().__init__(nome, sobrenome, cpf)
        self.__funcionario = funcionario