"""

Continuação


"""

# A forma certe de puxar os valores para retorno em qualquer função é dessa forma.
#Usa-se values()
numeros_dict = {"a":1,"b":8,"c":34,"d":3,"e":2,"f":1}
print(max(numeros_dict.values()))#max -> Retorna o maior número da lista
print(min(numeros_dict.values()))#min -> Retorna o maior número da lista

#Faça um programa que receba dois valores e do usuario e mostre o maior valor:
valor1=int(input("Digite o primeiro valor: "))
valor2=int(input("Digite o primeiro valor: "))
print(max(valor1,valor2))

#Max pode ser usado tmb com string
#Exemplo:
print(max("a","b","g","d"))#desta forma o maior sempre o ultima letra do alfabeto composta no iteravel. Neste caso, a letra "G"
print(max("aew","das","cfs","d"))#desta forma o maior sempre o ultima letra do alfabeto composta no iteravel. Neste caso, a letra "das"

# Da mesma forma podemos fazer com float.
print(max(1.14,1.55,2.45))

#min() -> Ira fazer o inverso do max. A função min() sempre ira retornar o menor valor dentro de variaveis ou iteraveis.