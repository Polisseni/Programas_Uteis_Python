'''Nível: Avançado+++

Conceitos: SQLite, múltiplas tabelas, CREATE TABLE, FOREIGN KEY, relacionamentos

Objetivo: criar um banco com usuários e categorias, relacionando cada usuário a uma categoria.'''

import sqlite3


conexao = sqlite3.connect("sistema.db")

cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON")


cursor.execute("""
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id)
        REFERENCES categorias(id)
)
""")


categorias = [
    ("Administrador",),
    ("Cliente",),
    ("Funcionário",)
]

cursor.executemany(
    "INSERT OR IGNORE INTO categorias (nome) VALUES (?)",
    categorias
)

conexao.commit()


print("Categorias cadastradas:")

cursor.execute("SELECT * FROM categorias")

for categoria in cursor.fetchall():
    print(categoria)


conexao.close()
