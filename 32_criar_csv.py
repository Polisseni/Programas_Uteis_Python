'''Nível: Intermediário+

Conceitos:

Arquivos CSV
Biblioteca csv
Listas
Dicionários
csv.DictWriter'''

import csv

# Dados que serão armazenados no arquivo
usuarios = [
    {"nome": "Ana", "idade": 22, "cidade": "Três Rios"},
    {"nome": "Carlos", "idade": 28, "cidade": "Petrópolis"},
    {"nome": "Maria", "idade": 25, "cidade": "Juiz de Fora"}
]

with open("usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
    campos = ["nome", "idade", "cidade"]

    escritor = csv.DictWriter(arquivo, fieldnames=campos)

    escritor.writeheader()
    escritor.writerows(usuarios)

print("Arquivo CSV criado com sucesso!")
