"""
Revisão de Sistema de Arquivos e Navegação
-----------------------------------------------------------------------------------------------------------------
    Sistema de arquivos armazenam dados em arquivos, esses dados podem ser diversos e até mais de um no mesmo lugar como: (foto,video,texto,tabela,grafico,etc)
Geralmente um arquivo é seguido o seguinte padrão para arquivos:

#nomedoarquivo.extensão

#Um exemplo mais claro seria: "arquivo.pdf"

    Este tipo de extensão é somente útil para nos, pois a maquina obtem informações por meio de metadados em um local especifico do arquivo.
A estrutura de diretório é diferente nos sistemas operacionais:

Windows - usa-se: C:/ -> diretório raiz
POSIX(linux,mac): / -> diretório raiz


Path -> Caminho do arquivo até o diretório onde ele está armazenado.

Existe dois tipos de Path:

-Path Absoluto: .. -> move para o diretório anterior


-Path Relativo: . -> para o atual
-------------------------------------------------------------------------------------------------------------------------------------
Para fazer manipulação de arquivo de navegação de arquivos é necessário "os" é necessário importar o "os"


import os
from resource import prlimit

print(os.getcwd()) #getcwd() -> pega o current work directory - diretório de trabalho corrente.
#retorna o caminho absoluto
-------------------------------------------------------------------------------------------------------------------------------------
# Para mudar o diretório, podemos utilizar o chdir() -> change directory
os.chdir(".")
-------------------------------------------------------------------------------------------------------------------------------------
# Podemos checar se um diretório é absoluto ou relativo

#print(os.path.isabs("/home/sak/Documentos/Python/Curso_Udemy_Python")) # Sempre que tiber encaminhamento para a raiz ele ira ser true.
-------------------------------------------------------------------------------------------------------------------------------------

#Se voce, estiver usando windows. Terá que ter cuidado ao verificar diretório

#print(os.path.isabs("C://Users//geek")) 
-------------------------------------------------------------------------------------------------------------------------------------
#Podemos identificar o stistema operacional com o módulo os:

import os
print(os.name)

#Posix = linux ou mac
#Nt= Windows
-------------------------------------------------------------------------------------------------------------------------------------
# Podemos ter mais detalhes no sistema operacional

import os
print(os.uname())
-------------------------------------------------------------------------------------------------------------------------------------
# Podemos mostrar a plataforma tmb

import sys 
print(sys.platform)
-------------------------------------------------------------------------------------------------------------------------------------
# Lista os diretórios

import os 

# Podemos listar os arquivos e diretório com o listdir()

print(os.listdir()) #Lista todos os arquivos dentro do diretório atual. Dentro de uma lista, onde podemos ter manipular com todas as funcionalidades de listas.
-------------------------------------------------------------------------------------------------------------------------------------
# Podemos listar os arquivos e diretório com mais detalhes com scandir()

import os

#print(list(os.scandir())) #-> Gera um iterator, por isso temos que colocar em uma lista

import os

arquivos = list(os.scandir())

print(arquivos)

print(arquivos[0].inode()) #
print(arquivos[0].is_dir()) # É diretório
print(arquivos[0].is_file()) # É diretório
print(arquivos[0].name) # Nome do arquivo
print(arquivos[0].path) #Caminho ate o arquivo
print(arquivos[0].stat()) #Estatisticas do arquivo
-------------------------------------------------------------------------------------------------------------------------------------
#OBS: Quando utilizamos a função scandir(), precisamos fechar similar ao abrir arquivos

import os 

scanner = os.scandir()
arquivos = list(scanner)
print(arquivos[0].inode()) #
print(arquivos[0].is_dir()) # É diretório
print(arquivos[0].is_file()) # É diretório
print(arquivos[0].name) # Nome do arquivo
print(arquivos[0].path) #Caminho ate o arquivo
print(arquivos[0].stat()) #Estatisticas do arquivo
#Fechamento
scanner.close()
-------------------------------------------------------------------------------------------------------------------------------------

"""

