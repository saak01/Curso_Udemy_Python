"""
POO - Propriedade - Proprities

#Metodos get-pegar, sets-setar/colocar
---------------------------------------------------------------------------------------------------------------
class Conta:
    
    contador = 0

    def __init__(self,titular,saldo,limites):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limites = limites

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self,valor):
        self.__saldo += valor

    def sacar(self,valor):
        self.__saldo -= valor

    def transferir(self,valor,destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self,limite):
        return self.__saldo = limite

cont1 = Conta('Joao Victor Alves Costa',3000,3000)
print(cont1.get_saldo())
cont1.set_saldo(999999)
print(cont1.get_saldo())
---------------------------------------------------------------------------------------------------------------------------
-Criando as Propriedades


#Usamos decorators para criar as propriedades, desta forma : @property
#RELEMBRARRRRRRRRRRRRRRRRRRRRRRRRRRRR/ IMPORTANTEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
class Conta:
    
    contador = 0

    def __init__(self,titular,saldo,limites):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limites = limites

    @property   #A propriedade já é um setter.
    def saldo(self):
        return self.__saldo
    
    @saldo.setter #Como já existe um generator, deste modo fazemos o setter com base nesta property
    def saldo(self,novo_saldo):
        self.__saldo = novo_saldo

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self,valor):
        self.__saldo += valor

    def sacar(self,valor):
        self.__saldo -= valor

    def transferir(self,valor,destino):
        self.__saldo -= valor
        destino.__saldo += valor


cont1 = Conta('Joao Victor Alves Costa',3000,3000)
print(cont1.saldo)
cont1.saldo = 90000
print(cont1.saldo)

"""
