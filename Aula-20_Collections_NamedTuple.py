"""
    #NameTuple

#Importando 

from collections import namedtuple

#Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro','idade raca nome')

#Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro','idade,raca,nome')

#Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro',['idade','raca','nome'])

ray = cachorro(idade=1,raca='Pinther',nome='Levandowisck')

print(ray)

from collections import namedtuple

cachorro = namedtuple('cachorro',['idade','raca','nome'])

ray = cachorro(idade=1,raca='Pinther',nome='Levandowisck')

print(ray)

#Selecionando dados forma 1

print(ray[0])

#Selecionando dados forma 2 #Forma Pythonica

print(ray.idade)




"""

