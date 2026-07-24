'''Nível: Intermediário Básico

Conceitos:

Listas
Operador in
Condicionais

Objetivo:
Permitir que o usuário cadastre nomes e depois pesquise se um nome está presente na lista.'''

# Pesquisa um nome em uma lista

nomes = []

print("Cadastre 5 nomes.\n")

for i in range(5):
    nome = input(f"Nome {i + 1}: ")
    nomes.append(nome)

pesquisa = input("\nDigite o nome que deseja procurar: ")

if pesquisa in nomes:
    print(f"{pesquisa} foi encontrado na lista.")
else:
    print(f"{pesquisa} não foi encontrado na lista.")
    