'''Nível: Intermediário+

Conceitos:

Leitura de CSV
csv.DictReader
Dicionários
Condicionais
Iteração sobre dados

Objetivo:

Ler o arquivo usuarios.csv criado no exercício anterior e mostrar somente os usuários que possuem 25 anos ou mais.'''

import csv

try:
    with open("usuarios.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        print("Usuários com 25 anos ou mais:\n")

        for usuario in leitor:
            idade = int(usuario["idade"])

            if idade >= 25:
                print(
                    f"Nome: {usuario['nome']} | "
                    f"Idade: {usuario['idade']} | "
                    f"Cidade: {usuario['cidade']}"
                )

except FileNotFoundError:
    print("Arquivo usuarios.csv não encontrado.")
    