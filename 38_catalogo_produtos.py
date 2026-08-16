'''Nível: Intermediário++

Conceitos:

Classes e objetos
Listas de objetos
Métodos
for
Entrada de dados

Objetivo: criar um pequeno catálogo onde o usuário cadastra produtos e, ao final, visualiza todos eles.'''

# Catálogo de produtos utilizando POO

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_informacoes(self):
        print(f"Produto: {self.nome} | Preço: R$ {self.preco:.2f}")


produtos = []

for i in range(3):
    print(f"\nCadastro do produto {i + 1}")

    nome = input("Nome: ")
    preco = float(input("Preço: R$ "))

    produto = Produto(nome, preco)

    produtos.append(produto)


print("\n===== CATÁLOGO =====")

for produto in produtos:
    produto.exibir_informacoes()
    