'''Dificuldade: 🔴 Intermediário avançado+
Conceitos: SQLite, múltiplas tabelas, relacionamentos, datetime, logs, histórico, consultas SQL

Agora vamos dar mais um passo.

Em vez de guardar o histórico apenas em um arquivo .log, vamos criar uma tabela específica no banco:

sincronizacoes

Cada execução ficará registrada no SQLite.'''

import sqlite3
import requests
from datetime import datetime

API_URL = "https://dummyjson.com/products"
BANCO = "produtos.db"


def conectar():
    return sqlite3.connect(BANCO)


def criar_tabelas():
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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sincronizacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_execucao TEXT NOT NULL,
            produtos_recebidos INTEGER NOT NULL,
            produtos_novos INTEGER NOT NULL,
            produtos_atualizados INTEGER NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


def buscar_produtos():
    try:
        resposta = requests.get(
            API_URL,
            timeout=10
        )

        resposta.raise_for_status()

        return resposta.json()["products"]

    except requests.RequestException as erro:
        print(f"Erro ao consultar API: {erro}")
        return []


def obter_ids_existentes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id FROM produtos")

    ids = {linha[0] for linha in cursor.fetchall()}

    conexao.close()

    return ids


def sincronizar(produtos):
    conexao = conectar()
    cursor = conexao.cursor()

    ids_existentes = obter_ids_existentes()

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

    data_execucao = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute("""
        INSERT INTO sincronizacoes
        (
            data_execucao,
            produtos_recebidos,
            produtos_novos,
            produtos_atualizados
        )
        VALUES (?, ?, ?, ?)
    """, (
        data_execucao,
        len(produtos),
        novos,
        atualizados
    ))

    conexao.commit()
    conexao.close()

    return novos, atualizados


def mostrar_historico():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id,
            data_execucao,
            produtos_recebidos,
            produtos_novos,
            produtos_atualizados
        FROM sincronizacoes
        ORDER BY id DESC
    """)

    registros = cursor.fetchall()

    conexao.close()

    print("\n=== HISTÓRICO DE SINCRONIZAÇÕES ===")

    if not registros:
        print("Nenhuma sincronização registrada.")
        return

    for registro in registros:
        print(
            f"\nID: {registro[0]}"
            f"\nData: {registro[1]}"
            f"\nRecebidos: {registro[2]}"
            f"\nNovos: {registro[3]}"
            f"\nAtualizados: {registro[4]}"
        )


def main():
    criar_tabelas()

    print("=== SINCRONIZADOR DE PRODUTOS ===")

    produtos = buscar_produtos()

    if not produtos:
        return

    novos, atualizados = sincronizar(produtos)

    print("\nSincronização concluída.")
    print(f"Novos: {novos}")
    print(f"Atualizados: {atualizados}")

    mostrar_historico()


main()
