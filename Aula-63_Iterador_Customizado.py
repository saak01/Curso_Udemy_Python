"""
Escrevendo um iterator

--------------------------------------------------------------------------------------------------------------------------------------------------------------
##Revisando um range
for n in range(1,11):
    print(n)
--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Criando um iterador customizado

class Contador:
    def __init__(self,menor,maior): #Funçoes dentro de classes são chamadas metodos #__init__ é uma função chamada construtor
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

con = Contador(1,61)
it = iter(con)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

for n in Contador(1,61):
    print(n)




"""
