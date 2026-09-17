'''Nível: Expert
Conceitos: SQLite, SELECT, UPDATE, transações, validação, estoque

Objetivo: criar uma função que registre a venda de um produto e diminua automaticamente sua quantidade no estoque.'''

import sqlite3


conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()


def registrar_venda():
    try:
        produto_id = int(input("ID do produto: "))
        quantidade = int(input("Quantidade vendida: "))
    except ValueError:
        print("Digite valores numéricos válidos.")
        return

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    cursor.execute("""
        SELECT nome, quantidade, preco
        FROM produtos
        WHERE id = ?
    """, (produto_id,))

    produto = cursor.fetchone()

    if produto is None:
        print("Produto não encontrado.")
        return

    nome, estoque, preco = produto

    if quantidade > estoque:
        print(
            f"Estoque insuficiente. "
            f"Disponível: {estoque} unidade(s)."
        )
        return

    novo_estoque = estoque - quantidade
    valor_venda = quantidade * preco

    cursor.execute("""
        UPDATE produtos
        SET quantidade = ?
        WHERE id = ?
    """, (novo_estoque, produto_id))

    conexao.commit()

    print("\nVenda registrada!")
    print(f"Produto: {nome}")
    print(f"Quantidade vendida: {quantidade}")
    print(f"Valor da venda: R$ {valor_venda:.2f}")
    print(f"Estoque restante: {novo_estoque}")


registrar_venda()

conexao.close()
