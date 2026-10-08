'''Dificuldade: 🔴 Intermediário avançado
Conceitos: logging, arquivos, níveis de log, API, SQLite, tratamento de exceções

Objetivo

Modificar o sincronizador para registrar o que acontece durante sua execução em um arquivo de log.

O programa deverá registrar:

início da sincronização;
quantidade de produtos recebidos;
quantidade de produtos novos;
quantidade de produtos atualizados;
erros ocorridos;
conclusão da sincronização.'''

import sqlite3
import requests
import logging

API_URL = "https://dummyjson.com/products"
BANCO = "produtos.db"


logging.basicConfig(
    filename="sincronizacao.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def conectar():
    return sqlite3.connect(BANCO)


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            categoria TEXT,
            estoque INTEGER,
            avaliacao REAL
        )
    """)

    conexao.commit()
    conexao.close()


def buscar_api():
    try:
        logging.info("Iniciando consulta à API.")

        resposta = requests.get(
            API_URL,
            timeout=10
        )

        resposta.raise_for_status()

        produtos = resposta.json()["products"]

        logging.info(
            f"{len(produtos)} produtos recebidos da API."
        )

        return produtos

    except requests.RequestException as erro:
        logging.error(
            f"Erro ao consultar API: {erro}"
        )

        return []


def obter_ids():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id FROM produtos")

    ids = {linha[0] for linha in cursor.fetchall()}

    conexao.close()

    return ids


def sincronizar(produtos):
    conexao = conectar()
    cursor = conexao.cursor()

    ids_existentes = obter_ids()

    novos = 0
    atualizados = 0

    for produto in produtos:

        if produto["id"] in ids_existentes:
            atualizados += 1
        else:
            novos += 1

        cursor.execute("""
            INSERT OR REPLACE INTO produtos
            (id, nome, preco, categoria, estoque, avaliacao)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            produto["id"],
            produto["title"],
            produto["price"],
            produto["category"],
            produto["stock"],
            produto["rating"]
        ))

    conexao.commit()
    conexao.close()

    logging.info(
        f"Sincronização concluída. "
        f"Novos: {novos} | "
        f"Atualizados: {atualizados}"
    )

    return novos, atualizados


def main():
    logging.info("=== INÍCIO DA EXECUÇÃO ===")

    try:
        criar_tabela()

        produtos = buscar_api()

        if not produtos:
            logging.warning(
                "Nenhum produto foi recebido."
            )
            return

        novos, atualizados = sincronizar(produtos)

        print("Sincronização concluída.")
        print(f"Novos: {novos}")
        print(f"Atualizados: {atualizados}")

    except Exception as erro:
        logging.exception(
            f"Erro inesperado: {erro}"
        )

    finally:
        logging.info("=== FIM DA EXECUÇÃO ===")


main()
