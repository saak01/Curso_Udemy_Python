"""
Generators

São similares a List comprehension e Dicti comprehension
Generators é basicamente um Tuple Comprehesion


"""
#Exemplo em list comprehsion

numeros = [1,2,3,4,5,6,7,8]
res = [num + 2 for num in numeros]
print(res)

#Exemplo Generator
    #Diferente do List comprehnsion, Generator não retorna um tupla, mas o objeto retornado é interavel

numeros = (1,2,3,4,5,6,7,8)
res = tuple(num + 2 for num in numeros)
print(tuple(res))
print(3 in res)

#Generator em questão de perfomace o generator é melhor; Deste modo

from sys import getsizeof
#biblioteca para medir espaço alocado na memoria

list_comp = getsizeof([x * 10 for x in range(1,1000)])

list_set = getsizeof({x * 10 for x in range(1,1000)})

list_dict = getsizeof({x: x * 10 for x in range(1,1000)})

gen = getsizeof(x * 10 for x in range(1000))

print("Testes para saber espaço alocado por cado metodo:")
print(list_comp)
print(list_set)
print(list_dict)
print(gen)

#Neste caso, importei uma função da biblioteca sys e usei para mostrar a diferença de memoria usada entre todas as funcionalidades 
#Portando, sempre que possivel usar Generator e List comprehension

#Posso interar no Generator Exempression
    #Sim, da mesma forma igual a expressoes vistas antes, podemos fazer deste modo:
gen = (x * 10 for x in range(1000))
for numeros in gen:
    print(numeros)

#Desta forma tambem

print(tuple(gen))
