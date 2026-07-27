'''Nível: Intermediário Básico

Conceitos:

Listas
sum()
len()
max()
min()

Objetivo:
Receber 10 números e exibir a soma, a média, o maior e o menor valor.'''

# Estatísticas de uma lista

numeros = []

for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

soma = sum(numeros)
media = soma / len(numeros)

print("\nResultados")
print(f"Soma: {soma}")
print(f"Média: {media:.2f}")
print(f"Maior número: {max(numeros)}")
print(f"Menor número: {min(numeros)}")
