'''Dificuldade: 🔴 Intermediário avançado
Conceitos: datetime, SQLite, filtros SQL, funções, validação de entradas.
Objetivo
Permitir que o usuário informe uma data inicial e uma data final para consultar as sincronizações realizadas naquele intervalo.
O programa deverá mostrar a quantidade de execuções, o total de produtos processados e a média por execução.'''

import sqlite3
from datetime import datetime

BANCO = "produtos.db"


def validar_data(data):
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def consultar_periodo(data_inicial, data_final):
    conexao = sqlite3.connect(BANCO)
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            COALESCE(SUM(produtos_recebidos), 0),
            COALESCE(SUM(produtos_novos), 0),
            COALESCE(SUM(produtos_atualizados), 0),
            COALESCE(AVG(produtos_recebidos), 0)
        FROM sincronizacoes
        WHERE DATE(data_execucao)
              BETWEEN DATE(?) AND DATE(?)
    """, (data_inicial, data_final))

    resultado = cursor.fetchone()
    conexao.close()

    return resultado


def main():
    print("=== RELATÓRIO POR PERÍODO ===")

    data_inicial = input(
        "Data inicial (AAAA-MM-DD): "
    ).strip()

    data_final = input(
        "Data final (AAAA-MM-DD): "
    ).strip()

    if not validar_data(data_inicial):
        print("Data inicial inválida.")
        return

    if not validar_data(data_final):
        print("Data final inválida.")
        return

    if data_inicial > data_final:
        print("A data inicial deve ser anterior à final.")
        return

    dados = consultar_periodo(
        data_inicial,
        data_final
    )

    print("\n=== RESULTADO ===")
    print(f"Período: {data_inicial} a {data_final}")
    print(f"Execuções: {dados[0]}")
    print(f"Produtos recebidos: {dados[1]}")
    print(f"Produtos novos: {dados[2]}")
    print(f"Produtos atualizados: {dados[3]}")
    print(f"Média por execução: {dados[4]:.2f}")


if __name__ == "__main__":
    main()
    