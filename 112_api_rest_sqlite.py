'''Objetivo: integrar uma API REST a um banco de dados SQLite, permitindo que os produtos permaneçam cadastrados mesmo após reiniciar o servidor.'''

'''requirements.txt'''

'''fastapi
uvicorn'''

'''modelos.py'''


from pydantic import BaseModel, Field


class ProdutoCriacao(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    preco: float = Field(gt=0)
    estoque: int = Field(ge=0)


class ProdutoResposta(ProdutoCriacao):
    id: int


'''banco.py'''


import sqlite3
from pathlib import Path

BANCO = Path(__file__).with_name("produtos.db")


def conectar():
    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela():
    with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL CHECK(preco > 0),
                estoque INTEGER NOT NULL CHECK(estoque >= 0)
            )
        """)


def cadastrar(nome, preco, estoque):
    with conectar() as conexao:
        cursor = conexao.execute(
            """
            INSERT INTO produtos (nome, preco, estoque)
            VALUES (?, ?, ?)
            """,
            (nome, preco, estoque)
        )

        return cursor.lastrowid


def listar():
    with conectar() as conexao:
        registros = conexao.execute(
            "SELECT * FROM produtos ORDER BY id"
        ).fetchall()

        return [dict(registro) for registro in registros]


def buscar(produto_id):
    with conectar() as conexao:
        registro = conexao.execute(
            "SELECT * FROM produtos WHERE id = ?",
            (produto_id,)
        ).fetchone()

        return dict(registro) if registro else None


def excluir(produto_id):
    with conectar() as conexao:
        cursor = conexao.execute(
            "DELETE FROM produtos WHERE id = ?",
            (produto_id,)
        )

        return cursor.rowcount > 0


'''main.py'''


from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, status

from banco import criar_tabela, cadastrar, listar, buscar, excluir
from modelos import ProdutoCriacao, ProdutoResposta


@asynccontextmanager
async def lifespan(app: FastAPI):
    criar_tabela()
    yield


app = FastAPI(
    title="API REST com SQLite",
    version="1.0.0",
    lifespan=lifespan
)


@app.post(
    "/produtos",
    response_model=ProdutoResposta,
    status_code=status.HTTP_201_CREATED
)
def cadastrar_produto(dados: ProdutoCriacao):
    produto_id = cadastrar(
        dados.nome,
        dados.preco,
        dados.estoque
    )

    return buscar(produto_id)


@app.get("/produtos", response_model=list[ProdutoResposta])
def listar_produtos():
    return listar()


@app.get("/produtos/{produto_id}", response_model=ProdutoResposta)
def buscar_produto(produto_id: int):
    produto = buscar(produto_id)

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado."
        )

    return produto


@app.delete("/produtos/{produto_id}")
def excluir_produto(produto_id: int):
    if not excluir(produto_id):
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado."
        )

    return {"mensagem": "Produto excluído com sucesso."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
