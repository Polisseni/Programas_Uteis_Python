'''Nível: Expert
Conceitos: SQLite, COUNT, SUM, AVG, MIN, MAX, funções e relatórios

Objetivo: criar um painel no terminal com indicadores gerais do estoque.'''

import sqlite3


conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()


cursor.execute("""
    SELECT
        COUNT(*) AS total_produtos,
        COALESCE(SUM(quantidade), 0) AS total_unidades,
        COALESCE(SUM(preco * quantidade), 0) AS valor_estoque,
        COALESCE(AVG(preco), 0) AS preco_medio,
        COALESCE(MIN(preco), 0) AS menor_preco,
        COALESCE(MAX(preco), 0) AS maior_preco
    FROM produtos
""")


indicadores = cursor.fetchone()

total_produtos = indicadores[0]
total_unidades = indicadores[1]
valor_estoque = indicadores[2]
preco_medio = indicadores[3]
menor_preco = indicadores[4]
maior_preco = indicadores[5]


cursor.execute("""
    SELECT COUNT(*)
    FROM produtos
    WHERE quantidade < 5
""")

produtos_estoque_baixo = cursor.fetchone()[0]


print("\n" + "=" * 45)
print("          DASHBOARD DE ESTOQUE")
print("=" * 45)

print(f"Total de produtos cadastrados: {total_produtos}")
print(f"Total de unidades armazenadas: {total_unidades}")
print(f"Valor total do estoque: R$ {valor_estoque:.2f}")
print(f"Preço médio dos produtos: R$ {preco_medio:.2f}")
print(f"Menor preço cadastrado: R$ {menor_preco:.2f}")
print(f"Maior preço cadastrado: R$ {maior_preco:.2f}")
print(f"Produtos com estoque baixo: {produtos_estoque_baixo}")

print("=" * 45)


conexao.close()
