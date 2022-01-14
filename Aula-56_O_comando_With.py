"""
With -> O bloco with é utilizado para criar um conteudo de trabalho  onde os recursos utilizados são fechados após o bloco: 
#Seguindo a forma ideal para trabalhar com este tipo de conexão:

1-Abrir o arquivo
2-Trabalhar no arquivo
##usasse closed para ver se o arquivo ainda está aberto
3-Fechar o arquivo

#Exemplo:
with open("Aula-54_Texto.txt") as arquivo:                  ####Forma Pythonica.########
arquivo.readlines()
print(len(arquivo))#podemos ver quantidade de linhas dessa forma.
----------------------------------------------------------------------------------------------------------------------------------


"""
with open("Aula-54_Texto.txt") as arquivo: #O próprio with fecha o arquivo, desta forma removendo o  streaming.
    arquivo.readlines()
    print(len(arquivo))#podemos ver quantidade de linhas dessa forma.