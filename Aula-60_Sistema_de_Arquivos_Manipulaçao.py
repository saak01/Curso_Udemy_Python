"""
Sistema de Arquivos - Manipulação
-----------------------------------------------------------------------------------------------------------------------------------------
#Descobrindo se arquivo/Dir existe.

import os 

# Paths Relativos
print(os.path.exists("50_testefunçoes.py"))#True
print(os.path.exists("texto.txt"))#False

#Path absolutos

print(os.path.exists(/home/))#True

----------------------------------------------------------------------------------------------------------------------------------------

# Criendo arquivos

#Forma 1:

open("Arquivo.txt,"w").close()
----------------------------------------------------------------------------------------------------------------------------------------
#Forma 2:

with open("Arquivos.txt,"w") as arquivo:
    pass
----------------------------------------------------------------------------------------------------------------------------------------
#Forma 3: #Melhor forma.

import os
#Criando o arquivo

os.mknod("/home/sak/Área de Trabalho/AAarquivo.txt")
#OBS : Criando um arquivo pelo mknod(), se o arquivo já exister teremos um PermissionError
# Para resolver este problema podemos adiciona o parâmetro: 

os.mknod("/home/sak/Área de Trabalho/AAarquivo.txt",exist_ok=True)

#OBS : Este metódo não funciona no Mac os.
----------------------------------------------------------------------------------------------------------------------------------------
#Para criar diretórios:

import os 

os.mkdir("Novo Diretório.")

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos um FileExistsError.
# Para resolver este problema podemos adiciona o parâmetro: 
os.mkdir("Novo Diretório",exist_ok=True)

----------------------------------------------------------------------------------------------------------------------------------------

#Para criar vários diretórios pode ser usado o makedirs()

import os
os.makedirs("templates/geek/university")

# OBS: Se não tivermos permissão  para cirar o diretório teremos um FileExistsError
----------------------------------------------------------------------------------------------------------------------------------------
#Para conter esses erros podemos adicionar o seguinte parâmetro.

import os

os.makedirs("templates/geek/university",exist_ok=True)

----------------------------------------------------------------------------------------------------------------------------------------
#Renomeando arquivos e diretório

import os 

os.rename("templates2","geek3")
            #arquivo    #renomeação

# OBS: Se o diretório não exister teremos um FileNotFoundError

# Se o diretório não estiver vázio teremos um erro.


#Dependendo de onde for o caminho, quando for mudar tem que passar todo o caminho e quando chegar no arquivo, colocar o novo nome

----------------------------------------------------------------------------------------------------------------------------------------
# Como deletar arquivos

OBS: Atenção tome cuidado com os comandos de apagar arquivos, ele não vão para a lixeira.

import os 

os.remove("geek.txt")

#OBS: Se estiver no windows, e o arquivo deletado tiver em uso. Isso vai gerar um erro.
#OBS: Caso o arquivo não exista, teremos o FileNotFoundError.
#OBS: Se informar um diretório ao invés de um arquivo, teremos um IsDirectoryError
----------------------------------------------------------------------------------------------------------------------------------------
# Como remover diretório

os.rmdir("diretório")

#OBS: Se o diretório tiver qualquer conteudo teremos Oserror
#OBS: Se o diretório não existir teremos um FileNOtFoundError

----------------------------------------------------------------------------------------------------------------------------------------
# Removendo uma arvore de diretórios

for arquivo in os.scandir("geek2"):
    if arquivo.is_file():
        os.remove(arquivo.path)
----------------------------------------------------------------------------------------------------------------------------------------
# Podemos remover uma arvore de diretórios

import os

os.removedirs("geek2/mais")

# Se algum dos diretórios estiver com outro diretório o processo para.
----------------------------------------------------------------------------------------------------------------------------------------
OBS:Ao remover arquivos de diretório com python, eles não vão para a lixeira.
----------------------------------------------------------------------------------------------------------------------------------------
#Importando a biblioteca Send2Trash

os.remove("cesta.txt") #Não vai para a lixeira. É  deletado imediatamente.
----------------------------------------------------------------------------------------------------------------------------------------
send2trash()-> Envia arquivos ou diretório para a lixeira  #INTE

Importando send2trash

import os 
from send2trash import send2trash
 
send2trash("arquivo")#Arquivo
send2trash("/arquivo")#Diretório
----------------------------------------------------------------------------------------------------------------------------------------
#Trabalhando com arquivos e diretórios temporários

import os 

import tempfile

with tempfile.TemporaryDirectory() as temp: -> aqui está sendo criado o arquivo tempórario
    print(f"Crie o diretório temporário em (tmp)")
    with open(os.path.join(tmp,'arquivo_tempoario.txt'),'w') as arquivo:
        input()
-------------------------------------------------------------------------------------------------------------
# Criando um Diretório temporário

import os   #INTE

import tempfile

with tempfile.TemporaryDirectory() as temp: #-> aqui está sendo criado o arquivo tempórario
    print(f"Crie o diretório temporário em {temp}")
    with open(os.path.join(temp,'arquivo_tempoario.txt'),'w') as arquivo:
        input()

#OBS: Possivelmente este código não funcione no windows, pois é diferente a forma de trabalho de arquivos temporários no windows.

-------------------------------------------------------------------------------------------------------------
#Criando um arquivo tempórario

import os   #INTE

import tempfile

with tempfile.TemporaryFile() as temp:
    temp.write(b"Geek University") # -> este arquivo só aceita binário, por isso  "b"
    temp.seek(0) # -> Sempre voltar o cursor. NAO ESQUECER.
    print(temp.read())

-------------------------------------------------------------------------------------------------------------

"""

