'''Nível: Expert inicial

Conceitos:

SQLite
FOREIGN KEY
JOIN
INSERT
SELECT
UPDATE
DELETE
múltiplas tabelas
menu interativo

Objetivo: criar um pequeno sistema de estoque utilizando duas tabelas relacionadas: produtos e categorias.'''

import sqlite3


conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON")


cursor.execute("""
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL,
    categoria_id INTEGER NOT NULL,
    FOREIGN KEY (categoria_id)
        REFERENCES categorias(id)
)
""")


conexao.commit()


def cadastrar_categoria():
    nome = input("Nome da categoria: ").strip()

    if not nome:
        print("Nome inválido.")
        return

    try:
        cursor.execute(
            "INSERT INTO categorias (nome) VALUES (?)",
            (nome,)
        )

        conexao.commit()

        print("Categoria cadastrada!")

    except sqlite3.IntegrityError:
        print("Essa categoria já existe.")


def listar_categorias():
    cursor.execute("SELECT * FROM categorias")

    categorias = cursor.fetchall()

    if not categorias:
        print("Nenhuma categoria cadastrada.")
        return

    print("\n=== CATEGORIAS ===")

    for categoria in categorias:
        print(
            f"{categoria[0]} - {categoria[1]}"
        )


def cadastrar_produto():
    nome = input("Nome do produto: ").strip()

    try:
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        categoria_id = int(input("ID da categoria: "))
    except ValueError:
        print("Valor inválido.")
        return

    cursor.execute(
        "SELECT id FROM categorias WHERE id = ?",
        (categoria_id,)
    )

    if cursor.fetchone() is None:
        print("Categoria não encontrada.")
        return

    cursor.execute("""
        INSERT INTO produtos
        (nome, preco, quantidade, categoria_id)
        VALUES (?, ?, ?, ?)
    """, (
        nome,
        preco,
        quantidade,
        categoria_id
    ))

    conexao.commit()

    print("Produto cadastrado!")


def listar_produtos():
    cursor.execute("""
        SELECT
            produtos.id,
            produtos.nome,
            produtos.preco,
            produtos.quantidade,
            categorias.nome
        FROM produtos
        JOIN categorias
            ON produtos.categoria_id = categorias.id
    """)

    produtos = cursor.fetchall()

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\n=== ESTOQUE ===")

    for produto in produtos:
        print(
            f"ID: {produto[0]} | "
            f"Produto: {produto[1]} | "
            f"Preço: R$ {produto[2]:.2f} | "
            f"Quantidade: {produto[3]} | "
            f"Categoria: {produto[4]}"
        )


def atualizar_estoque():
    try:
        produto_id = int(input("ID do produto: "))
        quantidade = int(input("Nova quantidade: "))
    except ValueError:
        print("Valor inválido.")
        return

    cursor.execute("""
        UPDATE produtos
        SET quantidade = ?
        WHERE id = ?
    """, (quantidade, produto_id))

    conexao.commit()

    if cursor.rowcount == 0:
        print("Produto não encontrado.")
    else:
        print("Estoque atualizado!")


while True:

    print("\n" + "=" * 35)
    print("       SISTEMA DE ESTOQUE")
    print("=" * 35)
    print("1 - Cadastrar categoria")
    print("2 - Listar categorias")
    print("3 - Cadastrar produto")
    print("4 - Listar produtos")
    print("5 - Atualizar estoque")
    print("6 - Sair")
    print("=" * 35)

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_categoria()

    elif opcao == "2":
        listar_categorias()

    elif opcao == "3":
        cadastrar_produto()

    elif opcao == "4":
        listar_produtos()

    elif opcao == "5":
        atualizar_estoque()

    elif opcao == "6":
        break

    else:
        print("Opção inválida.")


conexao.close()

print("Programa encerrado.")
