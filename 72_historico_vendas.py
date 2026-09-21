'''Nível: Expert+
Conceitos: SQLite, múltiplas tabelas, FOREIGN KEY, JOIN, transações, histórico de dados

Objetivo: evoluir o exercício anterior para que cada venda fique registrada permanentemente em uma tabela vendas, 
além de diminuir o estoque do produto.'''

import sqlite3


conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON")


cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    valor_total REAL NOT NULL,
    data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (produto_id)
        REFERENCES produtos(id)
)
""")

conexao.commit()


def registrar_venda():
    try:
        produto_id = int(input("ID do produto: "))
        quantidade = int(input("Quantidade vendida: "))
    except ValueError:
        print("Digite valores válidos.")
        return

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    cursor.execute("""
        SELECT nome, preco, quantidade
        FROM produtos
        WHERE id = ?
    """, (produto_id,))

    produto = cursor.fetchone()

    if produto is None:
        print("Produto não encontrado.")
        return

    nome, preco, estoque = produto

    if quantidade > estoque:
        print(f"Estoque insuficiente. Disponível: {estoque}.")
        return

    valor_total = preco * quantidade
    novo_estoque = estoque - quantidade

    try:
        cursor.execute("""
            INSERT INTO vendas
            (produto_id, quantidade, valor_total)
            VALUES (?, ?, ?)
        """, (
            produto_id,
            quantidade,
            valor_total
        ))

        cursor.execute("""
            UPDATE produtos
            SET quantidade = ?
            WHERE id = ?
        """, (
            novo_estoque,
            produto_id
        ))

        conexao.commit()

        print("\nVenda registrada com sucesso!")
        print(f"Produto: {nome}")
        print(f"Quantidade: {quantidade}")
        print(f"Valor total: R$ {valor_total:.2f}")
        print(f"Estoque restante: {novo_estoque}")

    except sqlite3.Error as erro:
        conexao.rollback()
        print(f"Erro ao registrar venda: {erro}")


def listar_vendas():
    cursor.execute("""
        SELECT
            vendas.id,
            produtos.nome,
            vendas.quantidade,
            vendas.valor_total,
            vendas.data_venda
        FROM vendas
        JOIN produtos
            ON vendas.produto_id = produtos.id
        ORDER BY vendas.id DESC
    """)

    vendas = cursor.fetchall()

    if not vendas:
        print("\nNenhuma venda registrada.")
        return

    print("\n=== HISTÓRICO DE VENDAS ===")

    for venda in vendas:
        print(
            f"ID: {venda[0]} | "
            f"Produto: {venda[1]} | "
            f"Quantidade: {venda[2]} | "
            f"Valor: R$ {venda[3]:.2f} | "
            f"Data: {venda[4]}"
        )


while True:

    print("\n=== SISTEMA DE VENDAS ===")
    print("1 - Registrar venda")
    print("2 - Histórico de vendas")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        registrar_venda()

    elif opcao == "2":
        listar_vendas()

    elif opcao == "3":
        break

    else:
        print("Opção inválida.")


conexao.close()

print("Programa encerrado.")
