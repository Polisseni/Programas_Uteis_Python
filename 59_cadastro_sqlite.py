'''Nível: Avançado+
Conceitos: sqlite3, SELECT, INSERT, funções, menu interativo

Objetivo: transformar o exercício anterior em um pequeno sistema de cadastro.'''

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

    print("Usuário cadastrado!")


def listar():
    cursor.execute("SELECT * FROM usuarios")

    usuarios = cursor.fetchall()

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("\nUsuários:")

    for usuario in usuarios:
        print(
            f"ID: {usuario[0]} | "
            f"Nome: {usuario[1]} | "
            f"E-mail: {usuario[2]}"
        )


while True:

    print("\n=== MENU ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar()

    elif opcao == "2":
        listar()

    elif opcao == "3":
        break

    else:
        print("Opção inválida.")


conexao.close()
print("Programa encerrado.")
