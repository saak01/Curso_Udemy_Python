"""
Filter

filter()-> serve para filtrar dados de uma determinada coleção:


"""
import statistics
dados = [1.3,1.7,0.8,4.1,4.3,-0.1]

#Calculando a mediados dados utilizando a função mean()
media = statistics.mean(dados)
print(media)
# Obs: Assim como a função map(), filter usa dois parametros, sendo eles uma função(lambda pode ser tmb) e um interavel

#Exemplo de Filter:
 
print(list(filter(lambda x: x>media,dados)))

#Uma filtragem com o filter

paises = ['Noruega','Suecia','Dinamarca','','Estolcomo','Cologne','']
print(list(filter(None,paises)))

# A diferença entre map e filter é, na map recebe 2 parametros e retorna um objeto iteravel
#Filter() -> Recebe dois parametros, uma função e um iteravel e retorna um objeto filtrado   apenas com os elementos de acordo com a expressão a ser utilizada

# Filtrar os usuarios que estao inativos no twitter
    
usuarios = [
    {"username": "samuel","tweets":["Eu adoro bolos","Eu adoro pizza"]},
    {"username": "Tonynoh",'tweets':[]},
    {"username": "Litonino",'tweets':[]}
    
    
    
    ]

inativos = list(filter(lambda usuario: len(usuario['tweets'])==0,usuarios))
print(inativos)
print([usu for usu in inativos])