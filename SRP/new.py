class DetalhesLivro:
    def __init__(self, livro):
        self.livro = livro

    def detalhes(self):
        return f"{self.livro.titulo} por {self.livro.autor}"

class SalvarLivro:
    def __init__(self, livro):
        self.livro = livro

    def salvar(self):
        with open(f"{self.livro.titulo}.txt", 'w') as arquivo:
            arquivo.write(self.livro.conteudo)

class Livro:
    def __init__(self, titulo, autor, conteudo):
        self.titulo = titulo
        self.autor = autor
        self.conteudo = conteudo
        self.detalhes = DetalhesLivro(self)
        self.salvar = SalvarLivro(self)


livro = Livro('Harry Potter: E o principe das reliquias', 'J.K', 'Fantasia')
