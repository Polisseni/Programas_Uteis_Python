'''Objetivo: desenvolver uma API capaz de retornar informações em JSON, consultar produtos e receber parâmetros pela URL.'''

'''requirements.txt'''

'''fastapi
uvicorn'''

'''main'''


from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Minha Primeira API",
    description="API REST desenvolvida em Python",
    version="1.0.0"
)

produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3500.00},
    {"id": 2, "nome": "Mouse", "preco": 80.00},
    {"id": 3, "nome": "Teclado", "preco": 150.00}
]


@app.get("/")
def inicio():
    return {
        "mensagem": "Bem-vindo à minha primeira API!",
        "status": "online"
    }


@app.get("/produtos")
def listar_produtos():
    return {
        "quantidade": len(produtos),
        "produtos": produtos
    }


@app.get("/produtos/{produto_id}")
def buscar_produto(produto_id: int):
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto

    raise HTTPException(
        status_code=404,
        detail="Produto não encontrado."
    )


@app.get("/buscar")
def buscar_por_nome(nome: str):
    resultados = [
        produto
        for produto in produtos
        if nome.lower() in produto["nome"].lower()
    ]

    return {
        "resultados": resultados,
        "quantidade": len(resultados)
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
