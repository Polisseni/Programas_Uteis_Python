'''Nível: Intermediário+

Conceitos:

JSON
Biblioteca json
Dicionários
Listas
Arquivos

Objetivo:
Cadastrar usuários e armazená-los em um arquivo JSON.'''

import json
import os

ARQUIVO = "usuarios.json"

if os.path.exists(ARQUIVO):
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        usuarios = json.load(arquivo)
else:
    usuarios = []

nome = input("Nome: ")
idade = int(input("Idade: "))

usuarios.append({
    "nome": nome,
    "idade": idade
})

with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
    json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

print("Usuário cadastrado com sucesso!")
