"""
Escrevendo em arquivos

#OBS: Ao abrir um arquivo para leitura , não podemos realizar a escrita nele. Apenas ler, da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Exemplo de escrita - modo: "write"

with open("Aula-54_Texto.txt","w") as arquivo:
    arquivo.write("Escrever em Python é muito fácil -_-") #para escrever usamos a função write().
    arquivo.write("\nPodemos colocar quantas linhas quisermos.")
    arquivo.write("\nEssa é a última linha")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


"""

