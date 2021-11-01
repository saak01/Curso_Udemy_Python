#Order Dict
"""
#Recap: O dicionario não garante uma ordem dentro dele, é pra isso usamos o order dict

Order Dict -> É um dicionario que nos garente a ordeem de uma inserção de elementos. A ordem dos elementos 
não importa para o Dicionario

        from collections import OrderedDict


        dicionario = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, }

        for chave,valor in dicionario.items():
            print(f'{chave}-{valor}')

        

#Entendendo a diferenca

        from collections import OrderedDict


        dicionario1 = {'a':1, 'b':2}
        dicionario2 = {'b':2, 'a':1}
        print(dicionario1)
        print(dicionario2)
        print(dicionario1 == dicionario2) #Ele diz True pois não importa a ordem

        print()

        odict1 = OrderedDict({'a':1,'b':2})
        odict2 = OrderedDict({'b':2,'a':1})
        print(odict1)
        print(odict2)
        print(odict1 == odict2) #False a ordem mudou

        console:

                {'a': 1, 'b': 2}
                {'b': 2, 'a': 1}
                True

                OrderedDict([('a', 1), ('b', 2)])
                OrderedDict([('b', 2), ('a', 1)])
                False

"""
