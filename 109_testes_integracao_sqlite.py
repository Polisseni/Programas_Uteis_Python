'''Objetivo: testar operações reais de um banco SQLite, utilizando bancos temporários para garantir que os testes não alterem os dados de produção.'''

"banco"


import sqlite3
from pathlib import Path


def conectar(caminho: str | Path):
    return sqlite3.connect(caminho)


def criar_tabelas(caminho: str | Path):
    with conectar(caminho) as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL CHECK(preco > 0),
                estoque INTEGER NOT NULL CHECK(estoque >= 0)
            )
        """)


"servicos"


from banco import conectar


def cadastrar_produto(caminho, nome, preco, estoque):
    if not nome.strip():
        raise ValueError("Nome obrigatório.")

    if preco <= 0:
        raise ValueError("Preço inválido.")

    if estoque < 0:
        raise ValueError("Estoque inválido.")

    with conectar(caminho) as conexao:
        cursor = conexao.execute(
            """
            INSERT INTO produtos (nome, preco, estoque)
            VALUES (?, ?, ?)
            """,
            (nome.strip(), preco, estoque)
        )

        return cursor.lastrowid


def buscar_produto(caminho, produto_id):
    with conectar(caminho) as conexao:
        cursor = conexao.execute(
            """
            SELECT id, nome, preco, estoque
            FROM produtos
            WHERE id = ?
            """,
            (produto_id,)
        )

        return cursor.fetchone()


def atualizar_estoque(caminho, produto_id, quantidade):
    if quantidade < 0:
        raise ValueError("Estoque inválido.")

    with conectar(caminho) as conexao:
        cursor = conexao.execute(
            """
            UPDATE produtos
            SET estoque = ?
            WHERE id = ?
            """,
            (quantidade, produto_id)
        )

        return cursor.rowcount > 0


"test_integracao"


import pytest

from banco import criar_tabelas
from servicos import (
    cadastrar_produto,
    buscar_produto,
    atualizar_estoque
)


@pytest.fixture
def banco_teste(tmp_path):
    caminho = tmp_path / "teste.db"
    criar_tabelas(caminho)
    return caminho


def test_cadastrar_e_buscar(banco_teste):
    produto_id = cadastrar_produto(
        banco_teste, "Notebook", 3500.0, 5
    )

    produto = buscar_produto(
        banco_teste, produto_id
    )

    assert produto == (
        produto_id, "Notebook", 3500.0, 5
    )


def test_atualizar_estoque(banco_teste):
    produto_id = cadastrar_produto(
        banco_teste, "Mouse", 80.0, 10
    )

    atualizado = atualizar_estoque(
        banco_teste, produto_id, 25
    )

    produto = buscar_produto(
        banco_teste, produto_id
    )

    assert atualizado is True
    assert produto[3] == 25


def test_preco_invalido(banco_teste):
    with pytest.raises(ValueError):
        cadastrar_produto(
            banco_teste, "Teclado", -50, 10
        )


def test_produto_inexistente(banco_teste):
    produto = buscar_produto(
        banco_teste, 999
    )

    assert produto is None


def test_estoque_negativo(banco_teste):
    produto_id = cadastrar_produto(
        banco_teste, "Monitor", 900.0, 5
    )

    with pytest.raises(ValueError):
        atualizar_estoque(
            banco_teste, produto_id, -1
        )

