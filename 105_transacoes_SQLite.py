'''Objetivo: garantir que operações envolvendo várias alterações no banco de dados sejam concluídas por inteiro ou desfeitas em caso de erro.

Por exemplo, ao vender um produto, o sistema precisa registrar a venda e diminuir o estoque. Se uma das operações falhar, nenhuma alteração deve ser mantida.'''

'banco.py'


import sqlite3


BANCO = "loja.db"


def criar_tabelas():
    with sqlite3.connect(BANCO) as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL CHECK(preco > 0),
                estoque INTEGER NOT NULL CHECK(estoque >= 0)
            )
        """)

        conexao.execute("""
            CREATE TABLE IF NOT EXISTS vendas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                produto_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL,
                total REAL NOT NULL,
                FOREIGN KEY (produto_id) REFERENCES produtos(id)
            )
        """)

        conexao.execute(
            "PRAGMA foreign_keys = ON"
        )


def cadastrar_produto(nome, preco, estoque):
    with sqlite3.connect(BANCO) as conexao:
        conexao.execute(
            """
            INSERT INTO produtos (nome, preco, estoque)
            VALUES (?, ?, ?)
            """,
            (nome, preco, estoque)
        )


def registrar_venda(produto_id, quantidade):
    if quantidade <= 0:
        raise ValueError("A quantidade deve ser positiva.")

    conexao = sqlite3.connect(BANCO)

    try:
        conexao.execute("PRAGMA foreign_keys = ON")

        with conexao:
            cursor = conexao.execute(
                """
                SELECT preco, estoque
                FROM produtos
                WHERE id = ?
                """,
                (produto_id,)
            )

            produto = cursor.fetchone()

            if produto is None:
                raise ValueError("Produto não encontrado.")

            preco, estoque = produto

            if estoque < quantidade:
                raise ValueError("Estoque insuficiente.")

            total = preco * quantidade

            conexao.execute(
                """
                UPDATE produtos
                SET estoque = estoque - ?
                WHERE id = ?
                """,
                (quantidade, produto_id)
            )

            conexao.execute(
                """
                INSERT INTO vendas
                (produto_id, quantidade, total)
                VALUES (?, ?, ?)
                """,
                (produto_id, quantidade, total)
            )

        return total

    finally:
        conexao.close()

'main.py'


from banco import (
    criar_tabelas,
    cadastrar_produto,
    registrar_venda
)


def main():
    criar_tabelas()

    print("1 - Cadastrar produto")
    print("2 - Registrar venda")

    opcao = input("Escolha uma opção: ")

    try:
        if opcao == "1":
            nome = input("Nome: ")
            preco = float(input("Preço: R$ "))
            estoque = int(input("Estoque inicial: "))

            cadastrar_produto(nome, preco, estoque)
            print("Produto cadastrado!")

        elif opcao == "2":
            produto_id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade vendida: "))

            total = registrar_venda(
                produto_id,
                quantidade
            )

            print(f"Venda registrada: R$ {total:.2f}")

        else:
            print("Opção inválida.")

    except (ValueError, TypeError) as erro:
        print(f"Erro: {erro}")

    except Exception as erro:
        print(f"Falha inesperada: {erro}")


if __name__ == "__main__":
    main()
