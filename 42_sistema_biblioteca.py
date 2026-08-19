'''Nível: Intermediário++

Conceitos:

Múltiplas classes
Objetos interagindo
Listas de objetos
Métodos
Condicionais

Objetivo: criar um sistema simples com livros que podem ser emprestados e devolvidos.'''

# Sistema simples de biblioteca utilizando POO


class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f'O livro "{self.titulo}" foi emprestado.')
        else:
            print(f'O livro "{self.titulo}" já está emprestado.')

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f'O livro "{self.titulo}" foi devolvido.')
        else:
            print(f'O livro "{self.titulo}" já está disponível.')

    def exibir(self):
        status = "Disponível" if self.disponivel else "Emprestado"

        print(
            f"{self.titulo} - {self.autor} | {status}"
        )


class Biblioteca:

    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        print("\n===== LIVROS =====")

        for livro in self.livros:
            livro.exibir()


biblioteca = Biblioteca()

livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("1984", "George Orwell")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.listar_livros()

print("\nRealizando empréstimo...")
livro1.emprestar()

biblioteca.listar_livros()

print("\nDevolvendo livro...")
livro1.devolver()

biblioteca.listar_livros()