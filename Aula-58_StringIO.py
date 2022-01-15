"""
STRINGIO

ATENÇÃO : Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão:
-Permissão de leitura -> ler o arquivo
-Permissão de escrita -> escrever no arquivo

StringIO()-> utilizado para ler e criar arquivos em memorias
-----------------------------------------------------------------------------------------------------------------------------------------------
#Primeiro fazemos o import 
from io import StringIO

mensagem = "Esta é apenas um string normal"
#Podemos criar um arquivo em memoria já com uma string vazia ou vazio;
#Escrevendo textos
arquivo = StringIO(mensagem)
print(arquivo.read())
print(arquivo.read())
-----------------------------------------------------------------------------------------------------------------------------------------------
#podemos movimentar o cursor também
mensagem = "Esta é apenas um string normal"
arquivo = StringIO(mensagem)
print(arquivo.read())
print(arquivo.read())-
arquivo.seek(0)
print(arquivo.read())


"""

