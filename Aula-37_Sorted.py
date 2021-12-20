"""
Sorted

Não confundir está expressão com a função encontrada nas listadas chamada : Sort.
Ambas tem a mesma função, ordenar, mas sorted pode ordernar qualquer iteravel

Obs: Sorted() sempre retornara uma lista, com os iteraveis ordenados.


#exemplos

num = [1,5,8,3,222,64,3]
print(num)
#Usando sorted
print(sorted(num))

#Podemos adicionar parametros na função sorted
    #Parametro Reverse
print(sorted(num,reverse=True))#Função reverse=True faz a ordem ser decrescente.

"""
    #Parametro Key
usuarios=[
{"username":"samuel", "tweets":["Adoro bolos","Adoro pizza"]},
{"username":"carla", "tweets":["Amo gatos"]},
{"username":"jeff", "tweets":[]},
{"username":"bob123", "tweets":[]},
{"username":"doggo", "tweets":["Adoro bolos","meu cachorro é lindo."]},
{"username":"gal", "tweets":[]}
]
#key sempre vai precisar de um objeto, ou seja, algo build-in.
print(sorted(usuarios, key=lambda usuario: usuario['tweets']))
#da pra ser mais especifico ainda. Exemplo: Ordernar com chave o primeiro tweet
print(sorted(usuarios, key=lambda usuario: usuario['tweets']))
#Ultimo exemplo

musicas = [
{"Titulo":"Thunderstrunk","tocou":3},
{"Titulo":"Seila","tocou":8},
{"Titulo":"Quadro-Doka","tocou":10},
{"Titulo":"Blackout","tocou":1}
]
#key pode ser usado por lambda para filtrar lista com dicionarios dentro. Assim ordenandos.
print(sorted(musicas,key=lambda musica: musica['Titulo']))
#Trocando as chaves do dicionario, podemos filtrar.
print(sorted(musicas,key=lambda musica: musica['tocou'],reverse=True))



