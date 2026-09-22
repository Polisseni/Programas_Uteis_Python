'''Nível: Expert++
Conceitos: SQLite, DATE(), GROUP BY, SUM(), filtros por período, agregação

Objetivo: permitir que o usuário informe uma data inicial e uma data final e gerar o faturamento daquele período.'''

import sqlite3


conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()


data_inicial = input(
    "Data inicial (AAAA-MM-DD): "
).strip()

data_final = input(
    "Data final (AAAA-MM-DD): "
).strip()


cursor.execute("""
    SELECT
        COUNT(*) AS total_vendas,
        COALESCE(SUM(quantidade), 0) AS unidades,
        COALESCE(SUM(valor_total), 0) AS faturamento
    FROM vendas
    WHERE DATE(data_venda)
    BETWEEN DATE(?) AND DATE(?)
""", (
    data_inicial,
    data_final
))


resultado = cursor.fetchone()

total_vendas = resultado[0]
unidades = resultado[1]
faturamento = resultado[2]


print("\n" + "=" * 45)
print("       RELATÓRIO POR PERÍODO")
print("=" * 45)

print(f"Período: {data_inicial} até {data_final}")
print(f"Total de vendas: {total_vendas}")
print(f"Unidades vendidas: {unidades}")
print(f"Faturamento: R$ {faturamento:.2f}")

print("=" * 45)


conexao.close()
