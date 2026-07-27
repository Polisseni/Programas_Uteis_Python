'''Nível: Intermediário Básico

Conceitos:

Listas
append()
remove()
Condicionais (if in)

Objetivo:
Permitir que o usuário cadastre 5 itens em uma lista e remova um deles. Caso o item não exista, exibir uma mensagem informando.'''

# Remove um item da lista

itens = []

print("Cadastre 5 itens.\n")

for i in range(5):
    item = input(f"Item {i + 1}: ")
    itens.append(item)

print("\nLista atual:")
print(itens)

remover = input("\nDigite o item que deseja remover: ")

if remover in itens:
    itens.remove(remover)
    print("\nItem removido com sucesso!")
else:
    print("\nItem não encontrado.")

print("\nLista atualizada:")
print(itens)
