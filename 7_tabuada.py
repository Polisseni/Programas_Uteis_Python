'''Nível: Iniciante+

Conceitos:

Laço for
Multiplicação'''

numero = int(input("Digite um número: "))

print(f"\nTabuada do {numero}\n")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
    