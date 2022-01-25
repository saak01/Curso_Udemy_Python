""" 
-Metodos -> Representam os comportamento do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema.

Em Pythoon dividimos os método. em 2 grupos: Métodos de instância e Métodos de Classe
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Métodos de Instância

# O metodo dunder init (__init__ ) é um metodo mespecial chamado de construtor sua função e construir o objeto a partir da classe

#OBS: Todo elemento em python que tenha double underline é chamado de dunder;

#Os metodos dunder são chamados de metodos mágicos.

#Atenção, por mais que podemos usar dunder para criação de métodos, não é aconselhado!

#Metodos são escritos em minisculo e palavras compostas são separadas com underline.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Lampada:

    def __init__(self,cor,voltagem,luminosidade):
        self.cor = cor
        self.voltagem = voltagem
        self.luminosidade = luminosidade


class ContaCorrente:
    
    contador = 4999

    def __init__(self, limite, saldo):

        self.__numero = ContaCorrente.contador +1
        self.__limite = limite 
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:
    
    contador = 0

    def __init__(self, nome, categoria, valor):
        self.__id = Produto.contador +1
        self.__nome = nome
        self.__categoria = categoria
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcetagem): #Metodo de instancia
        ""Retorna o valor de um produto com desconto""
        return (self.__valor * (100-porcetagem))/100

#Método de instanciam pois temo que instanciar o objeto.

p1 = Produto('Play4','Video_game',3000) -> Instanciamento do objeto
print(p1.desconto(20))
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Outra forma


class Produto:
    
    contador = 0

    def __init__(self, nome, categoria, valor):
        self.__id = Produto.contador +1
        self.__nome = nome
        self.__categoria = categoria
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcetagem): #Metodo de instancia
        ""Retorna o valor de um produto com desconto""
        return  (self.__valor * (100-porcetagem))/100



p1 = Produto('Play4','Video_game',3000) 
print(Produto.desconto(p1,20))


#Metodos de classe 

class Usuario:

    contador = 0

    @classmethod
    def conta_usuario(cls):#recebe o cls como parâmetro ao inves self.
        print(f'Temos {cls.contador} usuário no sistema')

    def __init__(self, nome, sobrenome):
        self.id = Usuario.contador + 1
        self.nome = nome
        self.sobrenome = sobrenome
        Usuario.contador = self.id


user1 = Usuario("Joao",'Costa')
Usuario.conta_usuario() #Forma Correta
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Quando usar os metodos de instancia e classe:

#Métodos de instancia
-Criamos metodos de instancia quando precisamos fazer acesso a atributos de instancias

#Métodos de Classe
-Método de classe em python são conhecido em outras linguagem como métodos estaticos.


"""
