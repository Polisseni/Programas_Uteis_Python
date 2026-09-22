''' Nível: Expert+
Conceitos: JOIN, GROUP BY, SUM(), ORDER BY, agregação

Objetivo: descobrir quais produtos tiveram maior quantidade de unidades vendidas.'''

import sqlite3


conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()


cursor.execute("""
    SELECT
        produtos.nome,
        SUM(vendas.quantidade) AS unidades_vendidas,
        SUM(vendas.valor_total) AS faturamento
    FROM vendas
    JOIN produtos
        ON vendas.produto_id = produtos.id
    GROUP BY produtos.id
    ORDER BY unidades_vendidas DESC
""")


produtos = cursor.fetchall()


print("\n=== PRODUTOS MAIS VENDIDOS ===")

if not produtos:
    print("Nenhuma venda registrada.")

else:
    for posicao, produto in enumerate(produtos, start=1):
        nome = produto[0]
        unidades = produto[1]
        faturamento = produto[2]

        print(
            f"{posicao}º - {nome} | "
            f"Unidades: {unidades} | "
            f"Faturamento: R$ {faturamento:.2f}"
        )


conexao.close()
