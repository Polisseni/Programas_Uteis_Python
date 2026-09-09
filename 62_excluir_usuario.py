'''Nível: Avançado++
Conceitos: sqlite3, DELETE, WHERE, SELECT, confirmação de operação

Objetivo: permitir que o usuário seja excluído do banco de dados, mas somente após uma confirmação.'''

import sqlite3


conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor()


def excluir_usuario():
    try:
        id_usuario = int(input("Digite o ID do usuário que deseja excluir: "))
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

    print("\nUsuário encontrado:")
    print(f"Nome: {usuario[1]}")
    print(f"E-mail: {usuario[2]}")

    confirmacao = input(
        "\nTem certeza que deseja excluir? (s/n): "
    ).lower()

    if confirmacao == "s":
        cursor.execute(
            "DELETE FROM usuarios WHERE id = ?",
            (id_usuario,)
        )

        conexao.commit()

        print("Usuário excluído com sucesso!")

    else:
        print("Operação cancelada.")


excluir_usuario()

conexao.close()
