'''Nível: Avançado++
Conceitos: sqlite3, UPDATE, WHERE, funções, validação de ID

Objetivo: adicionar ao sistema a possibilidade de alterar o nome e o e-mail de um usuário já cadastrado.'''

import sqlite3


conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor()


def atualizar_usuario():
    try:
        id_usuario = int(input("Digite o ID do usuário: "))
    except ValueError:
        print("ID inválido.")
        return

    cursor.execute(
        "SELECT * FROM usuarios WHERE id = ?",
        (id_usuario,)
    )

    usuario = cursor.fetchone()

    if usuario is None:
        print("Usuário não encontrado.")
        return

    print(f"\nUsuário atual: {usuario[1]}")
    print(f"E-mail atual: {usuario[2]}")

    novo_nome = input("Novo nome: ")
    novo_email = input("Novo e-mail: ")

    cursor.execute("""
        UPDATE usuarios
        SET nome = ?, email = ?
        WHERE id = ?
    """, (novo_nome, novo_email, id_usuario))

    conexao.commit()

    print("Usuário atualizado com sucesso!")


atualizar_usuario()

conexao.close()
