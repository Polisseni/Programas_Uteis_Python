'''Nível: Intermediário++

Conceitos:

Classes e objetos
Atributos
Métodos
Alteração de atributos
Operações matemáticas

Objetivo: criar uma classe Produto que permita aplicar um percentual de desconto ao preço.'''

# Produto com sistema de desconto utilizando POO

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto

    def exibir_informacoes(self):
        print(f"Produto: {self.nome}")
        print(f"Preço atual: R$ {self.preco:.2f}")


nome = input("Nome do produto: ")
preco = float(input("Preço do produto: R$ "))

produto = Produto(nome, preco)

print("\nProduto cadastrado:")
produto.exibir_informacoes()

percentual = float(input("\nPercentual de desconto: "))

produto.aplicar_desconto(percentual)

print("\nApós o desconto:")
produto.exibir_informacoes()
