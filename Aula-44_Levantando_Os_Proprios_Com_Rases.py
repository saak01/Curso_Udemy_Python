"""

Levantando os proprios erros com rases

raise -> Lança exceções

-raise não é uma função, é uma palavra reservada, como def entre outras
Pense no raise como semdo útil para que possamos criar nossas proprias exceções e mensagens de erro.

forma geralmente usada é: 
raise TipoDeError("Mensagem do erro")

Exemplo:
raise ValueError("Valor Incorreto")

Exemplo mais realista:

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError("Texto digitado incorretamente")
    if type(cor) is not str:
        raise TypeError("Cor digitado incorretamente")
    print(f"O texto {texto} vai ser pintado com a cor {cor}")

colore("Geek",3)

"""
