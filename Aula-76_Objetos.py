"""
Poo-Objetos

Objetos -> São instância de classe. ou seja aós o mapeamento do objeto do mundo real para sua represebtações
computacional, devemos poder cirar quatnos objetos foram necessário. Podemos pensar nos objetos/instancias de uma classe
como variáveis de um tipo definido de classe.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Lampada:

    def __init__(self,cor,voltagem,luminosidade):
        self.cor = cor
        self.voltagem = voltagem
        self.luminosidade = luminosidade
        self.ligada = False

    def ligaroudesliga(self):  #Sempre ligar o self
        if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True

    def chegar_lamapda(self):
        return (f'A lampada está {self.ligada}')

#Instancia
lamp1 = Lampada('cor',110,60)
lamp1.ligaroudesliga()
lamp1.ligaroudesliga()
print(lamp1.chegar_lamapda())
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Podemos criar variaveis e instanciar tambem no objeto Exemplo:


"""
 

class Pessoa:

    def __init__(self,nome,sobrenome,idade):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade

    def mostra_idade(self):
        print(self.__idade)

nome = 'joao'
sobrenome = 'costa'
idade = '20'

p1 = Pessoa(nome, sobrenome, idade)
Pessoa.mostra_idade(p1)