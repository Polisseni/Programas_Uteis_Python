'''Nível: Avançado++
Conceitos: SQLite, SELECT, WHERE, LIKE, funções, menu, tratamento de entrada

Objetivo: adicionar uma função de pesquisa ao sistema anterior, permitindo procurar usuários pelo nome.'''

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

conexao.commit()


def cadastrar():
    nome = input("Nome: ")
    email = input("E-mail: ")

    cursor.execute(
        "INSERT INTO usuarios (nome, email) VALUES (?, ?)",
        (nome, email)
    )

    conexao.commit()

    print("Usuário cadastrado com sucesso!")


def listar():
    cursor.execute("SELECT * FROM usuarios")

    usuarios = cursor.fetchall()

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for usuario in usuarios:
        print(
            f"ID: {usuario[0]} | "
            f"Nome: {usuario[1]} | "
            f"E-mail: {usuario[2]}"
        )


def buscar():
    termo = input("Digite o nome que deseja pesquisar: ")

    cursor.execute(
        "SELECT * FROM usuarios WHERE nome LIKE ?",
        (f"%{termo}%",)
    )

    resultados = cursor.fetchall()

    if not resultados:
        print("Nenhum usuário encontrado.")
        return

    print("\nResultados:")

    for usuario in resultados:
        print(
            f"ID: {usuario[0]} | "
            f"Nome: {usuario[1]} | "
            f"E-mail: {usuario[2]}"
        )


while True:

    print("\n=== SISTEMA DE USUÁRIOS ===")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()

    elif opcao == "2":
        listar()

    elif opcao == "3":
        buscar()

    elif opcao == "4":
        break

    else:
        print("Opção inválida.")


conexao.close()
