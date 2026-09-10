'''Nível: Avançado+++

Conceitos: SQLite, FOREIGN KEY, JOIN, INSERT, múltiplas tabelas

Objetivo: permitir cadastrar usuários escolhendo uma categoria existente e depois exibir essa categoria na listagem.'''

import sqlite3


conexao = sqlite3.connect("sistema.db")
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON")


def cadastrar_usuario():
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip()

    print("\nCategorias disponíveis:")

    cursor.execute("SELECT id, nome FROM categorias")

    categorias = cursor.fetchall()

    for categoria in categorias:
        print(f"{categoria[0]} - {categoria[1]}")

    try:
        categoria_id = int(input("Escolha a categoria: "))
    except ValueError:
        print("Categoria inválida.")
        return

    cursor.execute(
        "SELECT id FROM categorias WHERE id = ?",
        (categoria_id,)
    )

    if cursor.fetchone() is None:
        print("Categoria não existe.")
        return

    cursor.execute("""
        INSERT INTO usuarios (nome, email, categoria_id)
        VALUES (?, ?, ?)
    """, (nome, email, categoria_id))

    conexao.commit()

    print("Usuário cadastrado!")


def listar_usuarios():
    cursor.execute("""
        SELECT
            usuarios.id,
            usuarios.nome,
            usuarios.email,
            categorias.nome
        FROM usuarios
        JOIN categorias
            ON usuarios.categoria_id = categorias.id
    """)

    usuarios = cursor.fetchall()

    print("\n=== USUÁRIOS ===")

    for usuario in usuarios:
        print(
            f"ID: {usuario[0]} | "
            f"Nome: {usuario[1]} | "
            f"E-mail: {usuario[2]} | "
            f"Categoria: {usuario[3]}"
        )


cadastrar_usuario()

listar_usuarios()

conexao.close()
