'''Objetivo: evoluir a API do exercício 111, implementando operações de atualização com os métodos HTTP PUT e PATCH, validação de dados com Pydantic e persistência no SQLite.'''

'''requirements.txt'''

'''fastapi
uvicorn'''

'''modelos.py'''


from pydantic import BaseModel, Field, ConfigDict


class ProdutoBase(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    preco: float = Field(gt=0)
    estoque: int = Field(ge=0)


class ProdutoCriacao(ProdutoBase):
    pass


class ProdutoAtualizacao(BaseModel):
    nome: str | None = Field(
        default=None, min_length=1, max_length=100
    )
    preco: float | None = Field(default=None, gt=0)
    estoque: int | None = Field(default=None, ge=0)


class ProdutoResposta(ProdutoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

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


def atualizar(produto_id, dados):
    campos_permitidos = {"nome", "preco", "estoque"}

    if not dados or not set(dados).issubset(campos_permitidos):
        raise ValueError("Campos de atualização inválidos.")

    campos = ", ".join(f"{campo} = ?" for campo in dados)
    valores = list(dados.values())

    with conectar() as conexao:
        cursor = conexao.execute(
            f"UPDATE produtos SET {campos} WHERE id = ?",
            (*valores, produto_id)
        )
        return cursor.rowcount > 0


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

from banco import (
    criar_tabela,
    cadastrar,
    listar,
    buscar,
    atualizar,
    excluir
)

from modelos import (
    ProdutoCriacao,
    ProdutoAtualizacao,
    ProdutoResposta
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    criar_tabela()
    yield


app = FastAPI(
    title="API CRUD Completa com SQLite",
    version="1.0.0",
    lifespan=lifespan
)


def obter_produto(produto_id: int):
    produto = buscar(produto_id)

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado."
        )

    return produto


@app.post(
    "/produtos",
    response_model=ProdutoResposta,
    status_code=status.HTTP_201_CREATED
)
def cadastrar_produto(dados: ProdutoCriacao):
    produto_id = cadastrar(
        dados.nome, dados.preco, dados.estoque
    )
    return obter_produto(produto_id)


@app.get("/produtos", response_model=list[ProdutoResposta])
def listar_produtos():
    return listar()


@app.get("/produtos/{produto_id}", response_model=ProdutoResposta)
def buscar_produto(produto_id: int):
    return obter_produto(produto_id)


@app.put("/produtos/{produto_id}", response_model=ProdutoResposta)
def substituir_produto(produto_id: int, dados: ProdutoCriacao):
    obter_produto(produto_id)

    atualizar(produto_id, dados.model_dump())

    return obter_produto(produto_id)


@app.patch("/produtos/{produto_id}", response_model=ProdutoResposta)
def atualizar_parcialmente(
    produto_id: int,
    dados: ProdutoAtualizacao
):
    obter_produto(produto_id)

    alteracoes = dados.model_dump(exclude_unset=True)

    if not alteracoes:
        raise HTTPException(
            status_code=400,
            detail="Nenhum campo informado."
        )

    produto_atual = obter_produto(produto_id)

    dados_completos = {
        **{chave: produto_atual[chave]
           for chave in ("nome", "preco", "estoque")},
        **alteracoes
    }

    produto_validado = ProdutoCriacao.model_validate(
        dados_completos
    )

    atualizar(produto_id, produto_validado.model_dump())

    return obter_produto(produto_id)


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

'''.gitignore'''

'''__pycache__/
*.pyc
*.db
.venv/
.env'''
