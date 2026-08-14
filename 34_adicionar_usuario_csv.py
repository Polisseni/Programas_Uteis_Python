'''Nível: Intermediário+

Conceitos:

csv.DictWriter
Modo "a"
Arquivos
Dicionários
Funções

Objetivo: adicionar novos usuários ao arquivo usuarios.csv sem apagar os dados existentes.'''

import csv

ARQUIVO = "usuarios.csv"


def adicionar_usuario():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cidade = input("Cidade: ")

    with open(ARQUIVO, "a", newline="", encoding="utf-8") as arquivo:
        campos = ["nome", "idade", "cidade"]

        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        escritor.writerow({
            "nome": nome,
            "idade": idade,
            "cidade": cidade
        })

    print("\nUsuário adicionado com sucesso!")


adicionar_usuario()
