'''Nível: Expert inicial
Conceitos: SQLite, JOIN, GROUP BY, COUNT, SUM, ORDER BY

Objetivo: gerar um relatório mostrando quantos produtos existem em cada categoria e qual é o valor total armazenado.'''

import sqlite3


conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()


cursor.execute("""
    SELECT
        categorias.nome,
        COUNT(produtos.id) AS quantidade_produtos,
        SUM(produtos.preco * produtos.quantidade) AS valor_total
    FROM categorias
    LEFT JOIN produtos
        ON categorias.id = produtos.categoria_id
    GROUP BY categorias.id
    ORDER BY valor_total DESC
""")


relatorio = cursor.fetchall()


print("\n=== RELATÓRIO DE ESTOQUE ===")

if not relatorio:
    print("Nenhuma categoria cadastrada.")
else:
    for categoria in relatorio:
        nome = categoria[0]
        quantidade = categoria[1]
        valor_total = categoria[2] or 0

        print(f"\nCategoria: {nome}")
        print(f"Quantidade de produtos: {quantidade}")
        print(f"Valor total: R$ {valor_total:.2f}")


conexao.close()
