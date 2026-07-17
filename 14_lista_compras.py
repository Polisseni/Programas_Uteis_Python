'''Nível: Intermediário Básico

Conceitos:

Listas (list)
Laço while
Método append()
Laço for

Objetivo:
Criar uma lista de compras. O usuário poderá adicionar itens até digitar
 "fim". Ao final, todos os itens cadastrados serão exibidos.'''

# Lista de Compras

lista_compras = []

print("Digite os itens da lista de compras.")
print("Digite 'fim' para encerrar.\n")

while True:
    item = input("Item: ")

    if item.lower() == "fim":
        break

    lista_compras.append(item)

print("\nLista de Compras:")

for indice, item in enumerate(lista_compras, start=1):
    print(f"{indice}. {item}")
    