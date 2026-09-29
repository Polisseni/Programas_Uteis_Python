'''Nível: Expert+++
Conceitos: requests, JSON, SQLite, INSERT, API REST

Objetivo: buscar usuários de uma API e armazená-los localmente em um banco SQLite.'''

import sqlite3
import requests


URL = "https://jsonplaceholder.typicode.com/users"


def criar_banco():
    conexao = sqlite3.connect("api_usuarios.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            cidade TEXT
        )
    """)

    conexao.commit()

    return conexao


def importar_usuarios(conexao):
    try:
        resposta = requests.get(URL, timeout=10)
        resposta.raise_for_status()

        usuarios = resposta.json()

    except requests.RequestException as erro:
        print(f"Erro ao acessar a API: {erro}")
        return

    cursor = conexao.cursor()

    for usuario in usuarios:
        cursor.execute("""
            INSERT OR REPLACE INTO usuarios
            (id, nome, email, cidade)
            VALUES (?, ?, ?, ?)
        """, (
            usuario["id"],
            usuario["name"],
            usuario["email"],
            usuario["address"]["city"]
        ))

    conexao.commit()

    print(f"{len(usuarios)} usuários importados!")


def listar_usuarios(conexao):
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, email, cidade
        FROM usuarios
        ORDER BY id
    """)

    usuarios = cursor.fetchall()

    print("\n=== USUÁRIOS ===")

    for usuario in usuarios:
        print(
            f"ID: {usuario[0]} | "
            f"Nome: {usuario[1]} | "
            f"E-mail: {usuario[2]} | "
            f"Cidade: {usuario[3]}"
        )


conexao = criar_banco()

importar_usuarios(conexao)

listar_usuarios(conexao)

conexao.close()
