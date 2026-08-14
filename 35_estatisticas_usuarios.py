'''Nível: Intermediário+

Conceitos:

Leitura de CSV
Listas
sum()
len()
max()
min()
Conversão de tipos

Objetivo: ler os usuários cadastrados e descobrir a idade média, maior e menor idade.'''

import csv

ARQUIVO = "usuarios.csv"

idades = []

try:
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for usuario in leitor:
            idades.append(int(usuario["idade"]))

    if idades:
        media = sum(idades) / len(idades)

        print(f"Quantidade de usuários: {len(idades)}")
        print(f"Idade média: {media:.2f}")
        print(f"Maior idade: {max(idades)}")
        print(f"Menor idade: {min(idades)}")
    else:
        print("Nenhum usuário cadastrado.")

except FileNotFoundError:
    print("Arquivo usuarios.csv não encontrado.")
    