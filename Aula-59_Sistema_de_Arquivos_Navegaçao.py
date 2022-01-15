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

"""
import os

print(os.getcwd())