"""
Poo-Atributos
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Atributos representam as caracteristicas do objeto. Ou seja, pelos atributos nos conseguimos representar computacionalmente os estados de um objeto.

Em Python dividimos os atributos em  3 grupos:
    -> Atributos de instância/objeto
        -São declarados dentro do método construtor

    -> Atributos de Classe
    
    -> Atributos dinâmicos


OBS: Método construtor é um método especial para a construção do objeto.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Atributo publico e Privado

#Em python, por convenção ficou estabelecido que, todo atributo é público.
#Ou seja, pode ser acessado em todo projeto.
#Caso queiramos um atributo privado, ou seja, deve ser acessado/utilizado somentena classe declarada. É utilizado o __  inicio do nome.
#Isso é conhecido também como Name Mangling

class Lampada:

    def __init__(self,voltagem,cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class Produto:
    def __init__(self,nome,descricao,valor): #metodos são funcoes dentro de classes.
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

# Atributos Privados Name Manglin/Forma correta


class Acesso:
    
    def __init__(self,email,senha):
        self.email = email #.__ é para privado
        self.__senha = senha

#OBS: lembre-se que isso é apenas um conveção, ou seja, o linguagem python nao vai impedir que faça,os acesso aos atributos sinalizados como privados fora da classe.

user = Acesso('usergmail.com','1234')
print(user.__senha) #Atribute Error
print(dir(user))

print(user._Acesso__senha) #Temos acesso, mas não deveriamos fazer este acesso.
-Isto é (name mangling)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Forma certa de acessar atributos em classes.

class Acesso:
    
    def __init__(self,email,senha):
        self.email = email #.__ é para privado
        self.__senha = senha

    def mostrasenha():
        print(self.__senha)
    
user = Acesso('usergmail.com','1234')
Acesso.mostrasenha()
class Acesso:
    
    def __init__(self,email,senha):
        self.email = email #.__ é para privado
        self.senha = senha

user1 = Acesso('User1','senha')
user2 = Acesso('User2','senha33')
print(user1.email)
print(user2.email)
print(user1.senha)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Oque significa atributos de instâncias?

#Significa, que ao criar instâncias de uma classe, todas as instâncias terão estes atributos


#Atributos de Classe

class Produto:
    def __init__(self,nome,descricao,valor): #metodos são funcoes dentro de classes.
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

#Atributos de classe, são atributos que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre todas as instância da classe
#Ou seja, ao inves de cada instância da classe ter seus próprios valores como é o caso dos atributos de instância, com os atributos de classe todas as instâncias terão o mesmo valor para este atributo.

#Refatorar a classe produto

class Produto:

    imposto = 1.05 #Atributo de classe/  meio que um atributo padrão.
    contador = 0#Atributo de classe/  meio que um atributo padrão.

    def __init__(self, produto, tipo , valor):
        self.id = Produto.contador + 1
        self.produto = produto
        self.tipo = tipo
        self.valor = (valor*Produto.imposto)
        Produto.contador = self.id #Atributo de classe/  meio que um atributo padrão.

p1 = Produto('play4','videogame',2300)
print(p1.valor) #Acesso possivel, mas incorreto de um atributo de classe

#OBS: Não precisamo criar um instância de uma classe para fazer um acesso a um atributo de classe

#Em java, os atributos de classe são chamados de : atributos estatico
--------------------------------------------------------------------------------------------------------------------------------------------------
#Atributo dinâmico
-  O Atributo dinamico sera exclusivo da instância que o criou

Criando atributos em tempo de execução


p2.peso('5g')
--------------------------------------------------------------------------------------------------------------------------------------------------
#Deletando atributos dinamicos


del p2.peso







"""
