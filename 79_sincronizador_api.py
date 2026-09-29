'''Nível: Expert+++
Conceitos: API, SQLite, sincronização, INSERT OR REPLACE, comparação de dados

Objetivo: transformar a importação anterior em um pequeno sistema de sincronização.

O programa deverá:

Buscar usuários na API.
Verificar quantos já existem no banco.
Inserir novos usuários.
Atualizar usuários existentes.
Mostrar um resumo da sincronização.'''

import sqlite3
import requests


URL = "https://jsonplaceholder.typicode.com/users"


def conectar():
    conexao = sqlite3.connect("usuarios.db")

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


def buscar_api():
    try:
        resposta = requests.get(URL, timeout=10)
        resposta.raise_for_status()

        return resposta.json()

    except requests.RequestException as erro:
        print(f"Erro na API: {erro}")
        return []


def sincronizar(conexao, usuarios):
    cursor = conexao.cursor()

    novos = 0
    atualizados = 0

    for usuario in usuarios:

        cursor.execute(
            "SELECT id FROM usuarios WHERE id = ?",
            (usuario["id"],)
        )

        existe = cursor.fetchone()

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

        if existe:
            atualizados += 1
        else:
            novos += 1

    conexao.commit()

    print("\n=== SINCRONIZAÇÃO ===")
    print(f"Novos usuários: {novos}")
    print(f"Usuários atualizados: {atualizados}")
    print(f"Total recebido da API: {len(usuarios)}")


conexao = conectar()

usuarios = buscar_api()

if usuarios:
    sincronizar(conexao, usuarios)

conexao.close()
