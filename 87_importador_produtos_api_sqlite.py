'''Dificuldade: 🟠 Intermediário+
Conceitos: API, requests, SQLite, INSERT, funções, persistência de dados

Objetivo

Buscar produtos de uma API e armazená-los em um banco de dados SQLite.'''

import sqlite3
import requests

API_URL = "https://dummyjson.com/products"
BANCO = "produtos.db"


def criar_tabela():
    conexao = sqlite3.connect(BANCO)
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


def buscar_produtos():
    try:
        resposta = requests.get(API_URL, timeout=10)
        resposta.raise_for_status()

        return resposta.json()["products"]

    except requests.RequestException as erro:
        print(f"Erro ao acessar a API: {erro}")
        return []


def salvar_produtos(produtos):
    conexao = sqlite3.connect(BANCO)
    cursor = conexao.cursor()

    quantidade = 0

    for produto in produtos:
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

        quantidade += 1

    conexao.commit()
    conexao.close()

    return quantidade


def listar_produtos():
    conexao = sqlite3.connect(BANCO)
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, preco, categoria, estoque
        FROM produtos
        ORDER BY id
    """)

    produtos = cursor.fetchall()

    conexao.close()

    print("\n=== PRODUTOS NO BANCO ===")

    for produto in produtos:
        print(
            f"ID: {produto[0]} | "
            f"{produto[1]} | "
            f"${produto[2]} | "
            f"Categoria: {produto[3]} | "
            f"Estoque: {produto[4]}"
        )


def main():
    criar_tabela()

    produtos = buscar_produtos()

    if not produtos:
        print("Nenhum produto foi obtido.")
        return

    quantidade = salvar_produtos(produtos)

    print(f"{quantidade} produtos importados com sucesso.")

    listar_produtos()


main()
