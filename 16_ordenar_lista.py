'''Nível: Intermediário Básico

Conceitos:

Listas
Método sort()

Objetivo:
Receber 5 números e exibi-los em ordem crescente.'''

# Ordena uma lista de números

numeros = []

for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

numeros.sort()

print("\nLista em ordem crescente:")

for numero in numeros:
    print(numero)
    