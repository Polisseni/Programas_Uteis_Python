'''Dificuldade: 🔴 Intermediário avançado
Conceitos: SQLite, agregações SQL, COUNT, SUM, AVG, MAX, MIN, relatórios e tratamento de dados.

Objetivo

Evoluir o exercício 90 para um sistema que analisa o histórico de sincronizações e apresenta indicadores como:

total de sincronizações realizadas;

quantidade total de produtos processados;

quantidade de produtos novos e atualizados;

média de produtos processados por execução;

sincronização com maior volume de produtos.'''

import sqlite3

BANCO = "produtos.db"


def conectar():
    return sqlite3.connect(BANCO)


def obter_estatisticas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            COALESCE(SUM(produtos_recebidos), 0),
            COALESCE(SUM(produtos_novos), 0),
            COALESCE(SUM(produtos_atualizados), 0),
            COALESCE(AVG(produtos_recebidos), 0),
            COALESCE(MAX(produtos_recebidos), 0)
        FROM sincronizacoes
    """)

    resultado = cursor.fetchone()
    conexao.close()

    return resultado


def obter_maior_sincronizacao():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id,
            data_execucao,
            produtos_recebidos
        FROM sincronizacoes
        ORDER BY produtos_recebidos DESC, id ASC
        LIMIT 1
    """)

    resultado = cursor.fetchone()
    conexao.close()

    return resultado


def exibir_relatorio():
    dados = obter_estatisticas()

    total_execucoes = dados[0]
    total_recebidos = dados[1]
    total_novos = dados[2]
    total_atualizados = dados[3]
    media_recebidos = dados[4]
    maximo_recebidos = dados[5]

    print("\n=== RELATÓRIO DE SINCRONIZAÇÕES ===")

    print(f"Execuções realizadas: {total_execucoes}")
    print(f"Produtos recebidos: {total_recebidos}")
    print(f"Produtos novos: {total_novos}")
    print(f"Produtos atualizados: {total_atualizados}")
    print(f"Média por execução: {media_recebidos:.2f}")
    print(f"Maior volume em uma execução: {maximo_recebidos}")

    maior = obter_maior_sincronizacao()

    if maior:
        print("\n=== MAIOR SINCRONIZAÇÃO ===")
        print(f"Execução: {maior[0]}")
        print(f"Data: {maior[1]}")
        print(f"Produtos recebidos: {maior[2]}")


def main():
    exibir_relatorio()


if __name__ == "__main__":
    main()
    