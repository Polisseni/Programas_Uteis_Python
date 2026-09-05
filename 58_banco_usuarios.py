'''Nível: Avançado+
Conceitos: sqlite3, banco de dados, SQL, CREATE TABLE, INSERT

Objetivo: criar um banco de dados SQLite e cadastrar usuários.'''

import sqlite3


conexao = sqlite3.connect("usuarios.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

nome = input("Nome: ")
email = input("E-mail: ")

cursor.execute(
    "INSERT INTO usuarios (nome, email) VALUES (?, ?)",
    (nome, email)
)

conexao.commit()

print("\nUsuário cadastrado com sucesso!")

conexao.close()
