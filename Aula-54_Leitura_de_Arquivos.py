"""
-Leitura de Arquivos

Como ler um arquivo em Python.

Para ler o conteúdo de um arquivo em Python, utilizando a função integrada open().
que literalmente significa 'abrir'.
--------------------------------------------------------------------------------------------------------------------------------------------
open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada, que neste caso é o caminho do arquivo 
a ser lido. Essa função retorna um _io.TextIOWapper e é com ele que trabalhamos então.
--------------------------------------------------------------------------------------------------------------------------------------------
Todos os parâmetros do open estão : https://docs.python.org/3/functions.htmlopen
--------------------------------------------------------------------------------------------------------------------------------------------
#Para ler o conteudo de um arquivo é necessário usar a função read()
-Exemplo:

arquivo = open("Aula-54_Texto.txt")
print(arquivo.read())
--------------------------------------------------------------------------------------------------------------------------------------------
#OBS: Python utiliza um recurso para trabalhar com arquivos chamado cursor. Este cursor, funciona com o cursor quando estamos escrevendo.
--------------------------------------------------------------------------------------------------------------------------------------------
#OBS:A função read() lê todo o conteúdo do arquivo.
--------------------------------------------------------------------------------------------------------------------------------------------
read()-> Essa função lê todo o texto, seu return é em string.
--------------------------------------------------------------------------------------------------------------------------------------------




"""
