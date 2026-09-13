'''Nível: Expert inicial+
Conceitos: SQLite, WHERE, JOIN, filtros, parâmetros SQL, funções

Objetivo: permitir que o usuário informe um limite mínimo de estoque e listar todos os produtos cuja quantidade esteja abaixo desse valor.'''

import sqlite3


conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()


def listar_estoque_baixo():
    try:
        limite = int(input("Mostrar produtos com quantidade abaixo de: "))
    except ValueError:
        print("Digite um número válido.")
        return

    cursor.execute("""
        SELECT
            produtos.id,
            produtos.nome,
            produtos.quantidade,
            categorias.nome
        FROM produtos
        JOIN categorias
            ON produtos.categoria_id = categorias.id
        WHERE produtos.quantidade < ?
        ORDER BY produtos.quantidade ASC
    """, (limite,))

    produtos = cursor.fetchall()

    if not produtos:
        print("\nNenhum produto com estoque baixo.")
        return

    print("\n=== PRODUTOS COM ESTOQUE BAIXO ===")

    for produto in produtos:
        print(
            f"ID: {produto[0]} | "
            f"Produto: {produto[1]} | "
            f"Quantidade: {produto[2]} | "
            f"Categoria: {produto[3]}"
        )


listar_estoque_baixo()

conexao.close()
