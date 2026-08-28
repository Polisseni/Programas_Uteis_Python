'''Nível: Avançado inicial

Conceitos:

os
os.path
Diretórios
Verificação de arquivos

Objetivo: listar o conteúdo do diretório atual e informar se cada item é um arquivo ou uma pasta.'''

import os

diretorio = os.getcwd()

for item in os.listdir(diretorio):
    caminho = os.path.join(diretorio, item)

    if os.path.isfile(caminho):
        print(f"[ARQUIVO] {item}")

    elif os.path.isdir(caminho):
        print(f"[PASTA]   {item}")
        