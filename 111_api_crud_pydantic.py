'''Objetivo: ampliar a API anterior para permitir cadastrar, consultar, atualizar e excluir produtos, utilizando modelos Pydantic para validar os dados recebidos.'''

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


'''main.py'''


from fastapi import FastAPI, HTTPException, status

from modelos import (
    ProdutoCriacao,
    ProdutoAtualizacao,
    ProdutoResposta
)

app = FastAPI(title="API CRUD de Produtos")

produtos: dict[int, ProdutoResposta] = {}
proximo_id = 1


@app.post(
    "/produtos",
    response_model=ProdutoResposta,
    status_code=status.HTTP_201_CREATED
)
def cadastrar_produto(dados: ProdutoCriacao):
    global proximo_id

    produto = ProdutoResposta(
        id=proximo_id,
        **dados.model_dump()
    )

    produtos[proximo_id] = produto
    proximo_id += 1

    return produto


@app.get("/produtos", response_model=list[ProdutoResposta])
def listar_produtos():
    return list(produtos.values())


@app.get("/produtos/{produto_id}", response_model=ProdutoResposta)
def buscar_produto(produto_id: int):
    if produto_id not in produtos:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado."
        )

    return produtos[produto_id]


@app.put("/produtos/{produto_id}", response_model=ProdutoResposta)
def atualizar_produto(
    produto_id: int,
    dados: ProdutoAtualizacao
):
    if produto_id not in produtos:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado."
        )

    produto_atual = produtos[produto_id]

    atualizacoes = dados.model_dump(exclude_unset=True)

    produto_atualizado = produto_atual.model_copy(
        update=atualizacoes
    )

    produtos[produto_id] = produto_atualizado

    return produto_atualizado


@app.delete("/produtos/{produto_id}")
def excluir_produto(produto_id: int):
    if produto_id not in produtos:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado."
        )

    del produtos[produto_id]

    return {"mensagem": "Produto excluído com sucesso."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

