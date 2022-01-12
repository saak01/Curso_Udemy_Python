"""
Utilizamos o bloco try/expect para tratar erros que podem ocorrer no codigo. Previnindo paradas no programa e mensagens de erro ao usuario.

try - em portugues é tente.

expect - o que deve ser feito se der errado. 


#Exemplo 1 : Tratando um erro generico

try:
    joao()
except:
    print("Deu errado irmao")

OBS: Esta forma generica de tratamento de erro, não é a melhor forma. O ideial é sempre tratar de forma especifica.

#Exemplo 2 : Tratando erros de uma forma especifica.

try: 
    geek()
except NameError:
    print("Você está utilizando uma função inexistente")

"""

#Exemplo 3 : Tratando erros de uma forma especifica.

try: 
    geek()
except NameError as err:
    print(f"A aplicação gerou um  erro {err}")

#Desta forma podemos nomear o erro e saber mais detalhadamente o que aconteceu




