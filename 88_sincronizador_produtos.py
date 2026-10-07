'''Dificuldade: 🔴 Intermediário avançado
Conceitos: API, SQLite, sincronização, INSERT OR REPLACE, comparação de dados, atualização

Objetivo

Evoluir o exercício anterior para criar um sincronizador.

A ideia é:

consultar os produtos da API;
verificar quais produtos já estão no banco;
inserir produtos novos;
atualizar produtos existentes;
informar quantos registros foram inseridos ou atualizados.'''

import sqlite3
import requests

API_URL = "https://dummyjson.com/products"
BANCO = "produtos.db"


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
        resposta = requests.get(API_URL, timeout=10)
        resposta.raise_for_status()

        return resposta.json()["products"]

    except requests.RequestException as erro:
        print(f"Erro na API: {erro}")
        return []


def obter_produtos_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id FROM produtos")

    ids = {linha[0] for linha in cursor.fetchall()}

    conexao.close()

    return ids


def sincronizar(produtos):
    conexao = conectar()
    cursor = conexao.cursor()

    ids_existentes = obter_produtos_banco()

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

    return novos, atualizados


def main():
    print("=== SINCRONIZADOR DE PRODUTOS ===")

    criar_tabela()

    print("\nConsultando API...")

    produtos = buscar_api()

    if not produtos:
        print("Não foi possível obter os produtos.")
        return

    novos, atualizados = sincronizar(produtos)

    print("\n=== RESULTADO ===")
    print(f"Produtos novos: {novos}")
    print(f"Produtos atualizados: {atualizados}")
    print(f"Total processado: {len(produtos)}")


main()
