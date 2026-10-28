'''Conceitos: módulos, imports, separação de responsabilidades, funções, arquitetura em camadas e SQLite.
Objetivo
Separar o sistema de produtos em arquivos independentes, em vez de manter todas as funcionalidades em um único script.'''

'''99_sistema_produtos/
├── main.py
├── banco.py
├── servicos.py
└── relatorios.py'''

import sqlite3

BANCO = "produtos.db"


def conectar():
    return sqlite3.connect(BANCO)


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

from banco import conectar


def cadastrar_produto(nome, preco, estoque):
    nome = nome.strip()

    if not nome:
        raise ValueError("O nome não pode ficar vazio.")

    if isinstance(preco, bool) or not isinstance(
        preco, (int, float)
    ):
        raise ValueError("Preço inválido.")

    if preco < 0:
        raise ValueError("O preço não pode ser negativo.")

    if isinstance(estoque, bool) or not isinstance(
        estoque, int
    ):
        raise ValueError("Estoque deve ser um inteiro.")

    if estoque < 0:
        raise ValueError("Estoque não pode ser negativo.")

    with conectar() as conexao:
        cursor = conexao.execute("""
            INSERT INTO produtos (nome, preco, estoque)
            VALUES (?, ?, ?)
        """, (nome, preco, estoque))

        return cursor.lastrowid


def listar_produtos():
    with conectar() as conexao:
        cursor = conexao.execute("""
            SELECT id, nome, preco, estoque
            FROM produtos
            ORDER BY nome
        """)

        return cursor.fetchall()

from servicos import listar_produtos


def exibir_produtos():
    produtos = listar_produtos()

    print("\n=== CATÁLOGO DE PRODUTOS ===")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto_id, nome, preco, estoque in produtos:
        print(
            f"ID: {produto_id} | "
            f"{nome} | "
            f"Preço: R$ {preco:.2f} | "
            f"Estoque: {estoque}"
        )

from banco import criar_tabela
from servicos import cadastrar_produto
from relatorios import exibir_produtos


def main():
    criar_tabela()

    while True:
        print("\n=== SISTEMA DE PRODUTOS ===")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            try:
                nome = input("Nome: ")
                preco = float(input("Preço: "))
                estoque = int(input("Quantidade em estoque: "))

                produto_id = cadastrar_produto(
                    nome,
                    preco,
                    estoque
                )

                print(
                    f"Produto cadastrado com ID {produto_id}."
                )

            except ValueError as erro:
                print(f"Entrada inválida: {erro}")

        elif opcao == "2":
            exibir_produtos()

        elif opcao == "3":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()

    