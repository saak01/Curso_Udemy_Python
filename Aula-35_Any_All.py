""" 
Any e All


all() -> retorna True se os elementos iteravel são verdadeiros ou ainda o iteralvel estiver vazio
any() -> retorna True se qualquer elemento do iteravel for verdadeiro.
Exemplo de All()


print(all([0,3,4,6,8,9]))
#Neste caso o 0 é considerado como um número falso, deste modo, a resposta é False
print(all([3,4,6,8,9]))#True # Pois Todos os números são verdadeiros
print(all([]))#True # Pois todos os números são verdadeiros

"""
#Outra forma
    #Podemos usar list comprehesion
nomes = ["Carlos","Camila","Cassiano"]

print(all([nome[0] == 'C' for nome in nomes]))
#É uma boa forma de fazer check de dados

#Exemplo de Any()
print(any([0,3,4,6,8,9]))# Como somente um número é falso, a resposta vai ser True.
