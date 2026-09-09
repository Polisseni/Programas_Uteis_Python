'''Nível: Avançado+++

Conceitos:

SQLite
CRUD
Funções
Menus
INSERT
SELECT
UPDATE
DELETE
Tratamento de erros
Validação de entrada

Objetivo: juntar os exercícios anteriores em um único programa organizado.'''

import sqlite3


BANCO = "usuarios.db"


def conectar():
    return sqlite3.connect(BANCO)


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


def cadastrar():
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip()

    if not nome or not email:
        print("Nome e e-mail são obrigatórios.")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nome, email) VALUES (?, ?)",
        (nome, email)
    )

    conexao.commit()
    conexao.close()

    print("Usuário cadastrado com sucesso!")


def listar():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios")

    usuarios = cursor.fetchall()

    conexao.close()

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("\n=== USUÁRIOS ===")

    for usuario in usuarios:
        print(
            f"ID: {usuario[0]} | "
            f"Nome: {usuario[1]} | "
            f"E-mail: {usuario[2]}"
        )


def buscar():
    termo = input("Digite o nome para pesquisar: ").strip()

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE nome LIKE ?",
        (f"%{termo}%",)
    )

    resultados = cursor.fetchall()

    conexao.close()

    if not resultados:
        print("Nenhum usuário encontrado.")
        return

    print("\n=== RESULTADOS ===")

    for usuario in resultados:
        print(
            f"ID: {usuario[0]} | "
            f"Nome: {usuario[1]} | "
            f"E-mail: {usuario[2]}"
        )


def atualizar():
    try:
        id_usuario = int(input("ID do usuário: "))
    except ValueError:
        print("ID inválido.")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE id = ?",
        (id_usuario,)
    )

    usuario = cursor.fetchone()

    if usuario is None:
        print("Usuário não encontrado.")
        conexao.close()
        return

    novo_nome = input("Novo nome: ").strip()
    novo_email = input("Novo e-mail: ").strip()

    if not novo_nome or not novo_email:
        print("Os campos não podem ficar vazios.")
        conexao.close()
        return

    cursor.execute("""
        UPDATE usuarios
        SET nome = ?, email = ?
        WHERE id = ?
    """, (novo_nome, novo_email, id_usuario))

    conexao.commit()
    conexao.close()

    print("Usuário atualizado com sucesso!")


def excluir():
    try:
        id_usuario = int(input("ID do usuário: "))
    except ValueError:
        print("ID inválido.")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE id = ?",
        (id_usuario,)
    )

    usuario = cursor.fetchone()

    if usuario is None:
        print("Usuário não encontrado.")
        conexao.close()
        return

    print(f"\nUsuário: {usuario[1]}")
    print(f"E-mail: {usuario[2]}")

    confirmacao = input("Deseja realmente excluir? (s/n): ").lower()

    if confirmacao == "s":
        cursor.execute(
            "DELETE FROM usuarios WHERE id = ?",
            (id_usuario,)
        )

        conexao.commit()

        print("Usuário excluído com sucesso!")

    else:
        print("Operação cancelada.")

    conexao.close()


def menu():
    criar_tabela()

    while True:
        print("\n" + "=" * 35)
        print("       SISTEMA DE USUÁRIOS")
        print("=" * 35)
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Buscar usuário")
        print("4 - Atualizar usuário")
        print("5 - Excluir usuário")
        print("6 - Sair")
        print("=" * 35)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()

        elif opcao == "2":
            listar()

        elif opcao == "3":
            buscar()

        elif opcao == "4":
            atualizar()

        elif opcao == "5":
            excluir()

        elif opcao == "6":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


menu()
