class Livro:
    def __init__(self, titulo, autor, conteudo):
        self.titulo = titulo
        self.autor = autor
        self.conteudo = conteudo

    def detalhes(self):
        return f"{self.titulo} por {self.autor}"

    def salvar(self):
        with open(f"{self.titulo}.txt", 'w') as arquivo:
            arquivo.write(self.conteudo)
