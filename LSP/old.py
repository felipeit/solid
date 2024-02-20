class PessoaA:
    def se_aprensetar(self):
        print("Olá, sou a pessoa A")

class PessoaB(PessoaA):
    def __init__(self):
        super().__init__()
    
    def se_aprensetar(self):
        print("estou alterando esse metodo")


pessoa = PessoaA()
pessoa.se_aprensetar()

pessoa2 = PessoaB()
pessoa2.se_aprensetar()