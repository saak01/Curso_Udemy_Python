"""
#*Args

- O parãmetro args utilizado em uma função, coloca os valores exras informados como entrada de tupla.
Então desde já lembre-se que tuplas são imutaveis

- *Args é um parâmetro como outro qualquer, isso significa que você pode chamar de qualquer coisa, desde
que comece com *.:

Mas por convenção, utliziamos *args para definilo.

# Entendendo o args

        def somar_todos(*args):
            return print(args)

        print(somar_todos(1,3,4,5,8))
        print(somar_todos(1,3))
        print(somar_todos(4,4,4))
        print(somar_todos(1,3,5,6))

                #Como foi dito, o *args coloca todos os paramentros de entrada em uma tupla 
                -Assim, podemos usar todos os metodos que é possivel em uma tupla, como: sum(),len(),max(),min(),entre outros.
                -Lembrando que tuplas são IMUTÁVEIS.

def somar_todos(*args):
    return sum(args)

numeros = [1,2,3,4,5,6,7]

#Desempacotador

print(somar_todos(*numeros))

#OBS : O * serve para que informemos ao Python que estamos passando varios argumentos em uma coleção
#(Lista,Tupla,Set,). Desta forma, eke saberá que precisará antes desempacotar

"""

