"""
Métodos Mágicos - Poo

-Metodos mágicos são todos os métodos que usar dunder __ .

__repr__ -> repr(representação) é a representação do objeto. Geralmente, essa representação é feita para desenvolvedores, não para usuários finais:

class Livro: 

    def __init__(self,titulo,autor,paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas 
    def __repr__(self):
        return self.titulo


livro1 = Livro("Python Rocks", "Geek University",400)
livro2 = Livro("Python Artificial", "Geek University",300)

print(livro1)
print(livro2)
-----------------------------------------------------------------------------------------------------------------------------------------------------------
__str__ -> Tem a mesma função que reper, mas por hierarquia o str é executado, deste modo é o mais ideal para usuários finais.

class Livro: 

    def __init__(self,titulo,autor,paginas): 
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas 
    def __str__(self):
        return self.titulo


livro1 = Livro("Python Rocks", "Geek University",400)
livro2 = Livro("Python Artificial", "Geek University",300)

print(livro1)
print(livro2)
-----------------------------------------------------------------------------------------------------------------------------------------------------------
__len__ -> Indica o tamanho do objeto desejado.



class Livro: 

    def __init__(self,titulo,autor,paginas): 
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas 
    
    def __str__(self):
        return self.titulo
    
    def __len__(self):
        return self.paginas

livro1 = Livro("Python Rocks", "Geek University",400)
livro2 = Livro("Python Artificial", "Geek University",300)

print(len(livro1))
-----------------------------------------------------------------------------------------------------------------------------------------------------------
__del__


"""

class Livro: 

    def __init__(self,titulo,autor,paginas): 
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas 
    
    def __str__(self):
        return self.titulo
    
    def __len__(self):
        return self.paginas

    def __del__(self):
        print(f'Um objeto do tipo livro foi deletado da memoria')


livro1 = Livro("Python Rocks", "Geek University",400)


del livro1