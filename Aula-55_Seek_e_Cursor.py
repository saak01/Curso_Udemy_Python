"""
Seek e Cursor
----------------------------------------------------------------------------------------------------------------------------------
seek() -> é utilizada para movimentação do cursor pelo arquivo. Ela recebe um parâmetro que indica o local desejado para o cursor
----------------------------------------------------------------------------------------------------------------------------------
#Movimentando o Cursor pelo arquivo com a função seek()--procurar.

#Exemplo:

arquivo = open("Aula-54_Texto.txt")
print(arquivo.read())
arquivo.seek(0)#Neste caso o 0 é o indice, desta forma o cursor vai voltar para o inicio, assim podendo ler novamente logo abaixo.
print(arquivo.read())
----------------------------------------------------------------------------------------------------------------------------------
readline() -> Função que lê o arquivo linha a linha. readline -> lê linha
#Exemplo:
arquivo = open("Aula-54_Texto.txt")
print(arquivo.readline())
----------------------------------------------------------------------------------------------------------------------------------
#OBS: Tudo que vocẽ faz com um str pode se fazer aqui, exemplo:

arquivo = open("Aula-54_Texto.txt")
arq=arquivo.readline()
print(arq.split(" "))#Relembrando que o split divide a string pelo paramentro indicado e os coloca em uma lista.
----------------------------------------------------------------------------------------------------------------------------------
readlines() -> Cada linha fica dentro de uma lista.
#Exemplo:


arquivo = open("Aula-54_Texto.txt")
arq=arquivo.readlines()
print(len(arq))#podemos ver quantidade de linhas dessa forma.
----------------------------------------------------------------------------------------------------------------------------------
#OBS: Quando abrimos um arquivo usando open(), é criada um conexão entre disco e o nosso programa. Essa conexão é chamada de streaming.
Para finalizar o devemos fechar está conexão. Para isso utilizamos a função close().
----------------------------------------------------------------------------------------------------------------------------------
Passos para trabalhar com arquivo/bd:

1-Abrir o arquivo
2-Trabalhar no arquivo
##usasse closed para ver se o arquivo ainda está aberto
3-Fechar o arquivo

#Exemplo: 

1-arquivo = open("Aula-54_Texto.txt")

2-
arq=arquivo.readlines()
print(len(arq))
print(arquivo.closed)

3-arquivo.close()
----------------------------------------------------------------------------------------------------------------------------------

read()-> pode limitar a quantidade de caractere que pode aparecer, colocando a quantidade de caracteres desejadas como parâmetro:
#Exemplo:

"""


