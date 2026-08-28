'''Nível: Avançado inicial

Conceitos:

os
os.path.exists()
os.makedirs()
Automação

Objetivo: criar uma pasta chamada backup caso ela ainda não exista.'''

import os

nome_pasta = "backup"

if not os.path.exists(nome_pasta):
    os.makedirs(nome_pasta)
    print("Pasta 'backup' criada com sucesso!")

else:
    print("A pasta 'backup' já existe.")
    