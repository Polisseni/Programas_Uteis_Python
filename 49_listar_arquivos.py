'''Nível: Avançado inicial

Conceitos:

Biblioteca os
Diretórios
os.listdir()
Laços for

Objetivo: listar todos os arquivos e pastas existentes no diretório atual.'''

import os

# Obtém o diretório atual
diretorio = os.getcwd()

print(f"Conteúdo de: {diretorio}\n")

for item in os.listdir(diretorio):
    print(item)
    