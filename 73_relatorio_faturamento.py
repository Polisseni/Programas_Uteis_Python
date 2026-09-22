'''Nível: Expert+
Conceitos: SQLite, SUM(), COUNT(), AVG(), agregações, relatórios

Objetivo: calcular o faturamento total, quantidade de vendas e ticket médio com base no histórico.'''

import sqlite3


conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()


cursor.execute("""
    SELECT
        COUNT(*) AS total_vendas,
        COALESCE(SUM(quantidade), 0) AS unidades_vendidas,
        COALESCE(SUM(valor_total), 0) AS faturamento,
        COALESCE(AVG(valor_total), 0) AS ticket_medio
    FROM vendas
""")


resultado = cursor.fetchone()

total_vendas = resultado[0]
unidades_vendidas = resultado[1]
faturamento = resultado[2]
ticket_medio = resultado[3]


print("\n" + "=" * 40)
print("       RELATÓRIO DE FATURAMENTO")
print("=" * 40)

print(f"Total de vendas: {total_vendas}")
print(f"Unidades vendidas: {unidades_vendidas}")
print(f"Faturamento: R$ {faturamento:.2f}")
print(f"Ticket médio: R$ {ticket_medio:.2f}")

print("=" * 40)


conexao.close()
