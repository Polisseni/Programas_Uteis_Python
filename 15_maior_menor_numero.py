'''Nível: Intermediário Básico

Conceitos:

Listas
append()
max()
min()

Objetivo:
Solicitar que o usuário informe 5 números e, ao final, exibir o maior e o menor valor informado.'''

# Encontra o maior e o menor número de uma lista

numeros = []

for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

print(f"\nMaior número: {max(numeros)}")
print(f"Menor número: {min(numeros)}")
