'''Nível: Expert inicial+
Conceitos: SQLite, JOIN, csv, DictWriter, consultas SQL e exportação de dados

Objetivo: consultar os produtos do estoque e salvar um relatório em um arquivo CSV.'''

import sqlite3
import csv


conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()


cursor.execute("""
    SELECT
        produtos.id,
        produtos.nome AS produto,
        produtos.preco,
        produtos.quantidade,
        categorias.nome AS categoria
    FROM produtos
    JOIN categorias
        ON produtos.categoria_id = categorias.id
    ORDER BY produtos.nome
""")


produtos = cursor.fetchall()

with open(
    "relatorio_estoque.csv",
    "w",
    newline="",
    encoding="utf-8"
) as arquivo:

    escritor = csv.writer(arquivo)

    escritor.writerow([
        "ID",
        "Produto",
        "Preço",
        "Quantidade",
        "Categoria"
    ])

    for produto in produtos:
        escritor.writerow(produto)


conexao.close()

print("Relatório exportado com sucesso!")
print("Arquivo criado: relatorio_estoque.csv")
