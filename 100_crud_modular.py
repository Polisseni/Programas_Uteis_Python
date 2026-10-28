'''Conceitos: SQLite, CRUD, módulos, validação, exceções e SQL parametrizado.
Objetivo
Evoluir o exercício 99 para permitir cadastrar, listar, atualizar e excluir produtos. Cada operação ficará separada em uma função, facilitando a manutenção.'''

'''100_sistema_crud/
├── main.py
├── banco.py
└── servicos.py'''

'''1. banco.py'''

import sqlite3

BANCO = "produtos_crud.db"


def conectar():
    conexao = sqlite3.connect(BANCO)
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao


def criar_tabela():
    with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL CHECK(preco >= 0),
                estoque INTEGER NOT NULL CHECK(estoque >= 0)
            )
        """)


'''2. servicos.py'''

from banco import conectar


def validar_produto(nome, preco, estoque):
    if not nome.strip():
        raise ValueError("O nome não pode ficar vazio.")

    if isinstance(preco, bool) or not isinstance(
        preco, (int, float)
    ):
        raise ValueError("Preço inválido.")

    if preco < 0:
        raise ValueError("Preço não pode ser negativo.")

    if isinstance(estoque, bool) or not isinstance(
        estoque, int
    ):
        raise ValueError("Estoque deve ser um inteiro.")

    if estoque < 0:
        raise ValueError("Estoque não pode ser negativo.")


def cadastrar_produto(nome, preco, estoque):
    validar_produto(nome, preco, estoque)

    with conectar() as conexao:
        cursor = conexao.execute("""
            INSERT INTO produtos (nome, preco, estoque)
            VALUES (?, ?, ?)
        """, (nome.strip(), preco, estoque))

        return cursor.lastrowid


def listar_produtos():
    with conectar() as conexao:
        cursor = conexao.execute("""
            SELECT id, nome, preco, estoque
            FROM produtos
            ORDER BY id
        """)

        return cursor.fetchall()


def atualizar_produto(produto_id, nome, preco, estoque):
    validar_produto(nome, preco, estoque)

    with conectar() as conexao:
        cursor = conexao.execute("""
            UPDATE produtos
            SET nome = ?, preco = ?, estoque = ?
            WHERE id = ?
        """, (nome.strip(), preco, estoque, produto_id))

        return cursor.rowcount > 0


def excluir_produto(produto_id):
    with conectar() as conexao:
        cursor = conexao.execute("""
            DELETE FROM produtos
            WHERE id = ?
        """, (produto_id,))

        return cursor.rowcount > 0


'''3. main.py'''

from banco import criar_tabela
from servicos import (
    cadastrar_produto,
    listar_produtos,
    atualizar_produto,
    excluir_produto
)


def exibir_produtos():
    produtos = listar_produtos()

    print("\n=== PRODUTOS ===")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto_id, nome, preco, estoque in produtos:
        print(
            f"ID: {produto_id} | {nome} | "
            f"R$ {preco:.2f} | Estoque: {estoque}"
        )


def ler_id():
    return int(input("ID do produto: "))


def main():
    criar_tabela()

    while True:
        print("\n=== SISTEMA CRUD ===")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("5 - Sair")

        opcao = input("Escolha: ").strip()

        try:
            if opcao == "1":
                nome = input("Nome: ")
                preco = float(input("Preço: R$ "))
                estoque = int(input("Estoque: "))

                produto_id = cadastrar_produto(
                    nome, preco, estoque
                )

                print(f"Produto cadastrado. ID: {produto_id}")

            elif opcao == "2":
                exibir_produtos()

            elif opcao == "3":
                produto_id = ler_id()
                nome = input("Novo nome: ")
                preco = float(input("Novo preço: R$ "))
                estoque = int(input("Novo estoque: "))

                atualizado = atualizar_produto(
                    produto_id, nome, preco, estoque
                )

                print(
                    "Produto atualizado."
                    if atualizado
                    else "Produto não encontrado."
                )

            elif opcao == "4":
                produto_id = ler_id()

                excluido = excluir_produto(produto_id)

                print(
                    "Produto excluído."
                    if excluido
                    else "Produto não encontrado."
                )

            elif opcao == "5":
                print("Programa encerrado.")
                break

            else:
                print("Opção inválida.")

        except ValueError as erro:
            print(f"Entrada inválida: {erro}")


if __name__ == "__main__":
    main()

