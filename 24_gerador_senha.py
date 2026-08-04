'''Nível: Intermediário

Conceitos:

Funções
Biblioteca random
Biblioteca string
Laço for

Objetivo:
Gerar uma senha aleatória com a quantidade de caracteres escolhida pelo usuário.'''

import random
import string

# Gera uma senha aleatória

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ""

    for _ in range(tamanho):
        senha += random.choice(caracteres)

    return senha


tamanho = int(input("Quantidade de caracteres da senha: "))

print("\nSenha gerada:")
print(gerar_senha(tamanho))
