"""
Sorted

Não confundir está expressão com a função encontrada nas listadas chamada : Sort.
Ambas tem a mesma função, ordenar, mas sorted pode ordernar qualquer iteravel

Obs: Sorted() sempre retornara uma lista, com os iteraveis ordenados.
"""
#exemplos

num = [1,5,8,3,222,64,3]
print(num)
#Usando sorted
print(sorted(num))
#Usando sort
num = num.sort()
print(num)