"""
OBS: Você é responsavel pelas entradas da sua função. Então, trate as.

Quando e onde tratar codigos?

-Toda entrada de um usuario deve ser tratada!
def dividir(a,b):
    try:
        return int(a) / int(b)
    except (ZeroDivisionError,ValueError):
        return "Ocorreu um Erro no seu programa."

        
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
print(dividir(num1,num2))
#A função do usuario é  destruir seu sistema

num = ''
try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Valor incorreto, por favor digite somente o número.")

print(f"O número informado foi: {num}")

Forma ideal de se fazer:

try:
    num = int(input("Informe um número: "))
except ValueError: #O except funciona como um if, deste modo ficaria assim : if valueErro. Entao podemos colocar o else para uma melhor experiencia e um codigo mais limpo.

    print("Valor incorreto, por favor digite somente o número.")
else:
    print(f"O número informado foi: {num}")

# Else -> é executado somente se nao ocorrer um erro.

# Finaly -> O bloco finaly é SEMPRE executado, independente se houve ou não uma excessão.
# O finally e utilizado para fechar ou desalocar recursos. Exemplo: Fechar uma conexão com banco de dados ou arquivo aberto para leitura destes dados.


num = ''
try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Valor incorreto, por favor digite somente o número.")
else:
    print(f"Voce digitou o número: {num}")
print(f"O número informado foi: {num}")

#Exemplo complexo errado!:

def dividir(a,b):
    resultado = a/b
    return round(resultado,2)

try:
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
except ValueError:
    print("O valor precisa ser númerico")
else:
    print(dividir(num1,num2))

#Exemplo correto

def dividir(a,b):
    try:
        return int(a) / int(b)
    except ValueError:
        return "Valor incorreto"
    except ZeroDivisionError:
        return "Não é possivel realizar um divisão por zero"
        
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
print(dividir(num1,num2))

OBS: Toda a entrada deve ser validade e função é responsabilidade minha, então todos os erros devem ser tratados lá.

#Tratamento semi-generico

def dividir(a,b):
    try:
        return int(a) / int(b)
    except (ZeroDivisionError,ValueError):
        return "Ocorreu um Erro no seu programa."

        
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
print(dividir(num1,num2))

"""
