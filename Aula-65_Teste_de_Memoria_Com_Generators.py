"""
Teste de Memoria com Generators
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Sequência de Fibonnaci

1,1,2,3,5...

#Função normal - usando listas-400 mb de memoria 
def fib_lista(max):
    nums = []
    a, b = 0,1
    while len(nums) < max:
        a, b = b, a+b
    return nums
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Teste
for n in fib_lista(1000000000000): #
    print(n)

print("eu")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Com generators

def fib_gen(max):
    a, b, contador = 1,0,0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1  #2.5 mb

# Diferente da lista, o generator é gerado 1 a 1, deste modo não consumindo tanta memória.

#Teste
for n in fib_lista(1000000000000): #
    print(n)


"""





