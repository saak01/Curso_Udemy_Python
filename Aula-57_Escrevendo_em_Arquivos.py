"""
Escrevendo em arquivos

#OBS: Ao abrir um arquivo para leitura , não podemos realizar a escrita nele. Apenas ler, da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.
#Se o arquivo não existir, o arquivo será criado.
#Se o arquivo existir, todo conteúdo será apagado e re-escrito.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
write()-> Para escrevermos dados em um arquivo, após abrilo utilizamos a função write(), está função recebe uma string como parâmetro.

#Exemplo de escrita - modo: "write"

with open("Aula-54_Texto.txt","w") as arquivo:
    arquivo.write("Escrever em Python é muito fácil -_-") #para escrever usamos a função write().
    arquivo.write("\nPodemos colocar quantas linhas quisermos.")
    arquivo.write("\nEssa é a última linha")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


"""
with open("/home/sak/Área de Trabalho/teste.py","w") as arquivo:  #exemplo de como escrever e criar um arquivo em alguma parte do sistema de arquivos.
    arquivo.write("Salve amigao.")
