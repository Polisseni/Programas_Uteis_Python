'''Nível: Iniciante+

Conceitos:

while
if, elif e else
Biblioteca random'''

import random

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número (1 a 10): "))

    if palpite < numero_secreto:
        print("O número secreto é maior!")

    elif palpite > numero_secreto:
        print("O número secreto é menor!")

print("Parabéns! Você acertou!")
