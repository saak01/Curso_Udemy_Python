"""
Decoradores -> mais no sentido de aprimoramento

O que são decorators?

- Decorator são funções 

- Decorator envolvem outras funções e aprimoram seus comportamentos:

- Decorators também são exemplos de Higher Order Functions;

- Decorators ten uma sintaxe própria, usando "@" (Syntact Sugar)
--------------------------------------------------------------------------------------------------------------------------------------------------

# Decorators como funções (Sintaxe não recomendada ) -> Sem Syntact Sugar ##Forma não pythonica
Exemplos:

def sendo_educado(funcao):
    def sendo():
        print("Foi um prazer Conhecer você")
        funcao()
        print("Tenha um Otimo Dia")
    return sendo()

def saudacao():
    print("Seja Bem Vindo")

teste = sendo_educado(saudacao)

teste()

--------------------------------------------------------------------------------------------------------------------------------------------------
# Decorators com Syntax Sugar -> RECOMENDADA


def seja_educado(funcao):
    def sendo_mesmo():
        print("Foi um prazer conhecer você")
        funcao()
        print("Tenha um excelente dia")
    return sendo_mesmo

@seja_educado  #-> decorator
def apresentado():
    print("Meu nome é João")

#Testando

apresentado()
--------------------------------------------------------------------------------------------------------------------------------------------------
Exemplo: (não é um código opcional)

def checa_login():
    if not request.usuario:
        redurect("http://www.suaempresa.com.br")
    
def home(request):
    return "Pode acessar home"

def services(request)
    return "Pode acessar o serviços"

@chega_login
def admin(request):
    return "pode acessar admin"

"""

