'''Nível: Intermediário++

Conceitos:

Classes
Objetos
Métodos
Controle de estoque
Validação de dados

Objetivo: criar um produto que permita adicionar e remover unidades do estoque.'''

# Sistema simples de estoque utilizando POO

class Produto:

    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.quantidade += quantidade
            print("Produtos adicionados ao estoque.")
        else:
            print("A quantidade deve ser positiva.")

    def remover_estoque(self, quantidade):
        if quantidade <= 0:
            print("A quantidade deve ser positiva.")
        elif quantidade > self.quantidade:
            print("Quantidade insuficiente no estoque.")
        else:
            self.quantidade -= quantidade
            print("Produtos removidos do estoque.")

    def consultar_estoque(self):
        print(f"\nProduto: {self.nome}")
        print(f"Quantidade disponível: {self.quantidade}")


nome = input("Nome do produto: ")
quantidade = int(input("Quantidade inicial: "))

produto = Produto(nome, quantidade)

produto.consultar_estoque()

entrada = int(input("\nQuantidade para adicionar: "))
produto.adicionar_estoque(entrada)

produto.consultar_estoque()

saida = int(input("\nQuantidade para remover: "))
produto.remover_estoque(saida)

produto.consultar_estoque()
