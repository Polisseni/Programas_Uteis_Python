'''Nível: Intermediário++

Conceitos:

Classes
Objetos
Atributos
Métodos
__init__()

Objetivo: criar uma classe Produto capaz de armazenar nome e preço e exibir essas informações.'''

# Cadastro simples de produtos utilizando POO

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_informacoes(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")


nome = input("Nome do produto: ")
preco = float(input("Preço do produto: R$ "))

produto = Produto(nome, preco)

print("\nInformações do produto:")
produto.exibir_informacoes()
