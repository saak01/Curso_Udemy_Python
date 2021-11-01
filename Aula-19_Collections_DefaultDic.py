"""
    #Default Dict


#Recap dict: Quando não é encontrado a chave requisitada é gerado um Key Error

-Ao criar um dicionario usando o default dict, nos informamos um valor default, podendo utilizar lambda
para isso.Este valor será utilizado sempre que não houver um valor definido. Caso tentamos acessar uma chave
não existente, essa chave criada e o valor defaul sera atribuido.

#Lambada são funções sem nome, que pode ou nao receber parâmetros e retornar valores.

    from typing import DefaultDict


    dicionario = DefaultDict(lambda:0)

    dicionario['Curso'] = 'Programação em Python'

    print(dicionario)

    print(dicionario['Outro'])

    print(dicionario)

        Console:

            defaultdict(<function <lambda> at 0x7f04d63eb160>, {'Curso': 'Programação em Python'})
            0
            defaultdict(<function <lambda> at 0x7f04d63eb160>, {'Curso': 'Programação em Python', 'Outro': 0})



"""
