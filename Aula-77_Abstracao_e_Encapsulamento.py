"""
Poo - Abstração e Encapsulamento 

o grande objetivo de poo é encapsular nosso codigo, dentro de um grupo logico e hierarquico utilizando classes.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Relembrando:

Atributos/Metodos privados em python.

Imagina que temos uma classe chamada Pessoas. Contendo um atributo privado chamado __nome e um metodo __falar()

Esse elementos privados so devem/deveria ser acessados dentro da classe. Mas python, 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Importante:
########Abstração: em Poo, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados ou de usuário




"""
class Conta:

    contador = 400

    def __init__(self,titular,saldo,limite):
        self.__id_conta = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite 

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite} ')

#Neste caso, não teria como mudar o valor dos objetos instanciados. Mas se os atributos fossem públicos poderiam ser editados e assim
#Ocasionar problemas de segurança.

#Por isso temos que fazer a abstração de dados, ou seja, mostrar somenente o necessário para o usuario e encapsular a classe (protege-la)
