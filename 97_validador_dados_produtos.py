'''Conceitos: Pandas, validação, valores ausentes, duplicatas, regras de negócio e relatórios.
Objetivo
Criar um programa que analise os dados de produtos e identifique registros inconsistentes antes de utilizá-los em relatórios.

O sistema verificará:
- IDs duplicados;
- nomes vazios;
- preços negativos;
- estoque negativo;
- avaliações fora do intervalo de 0 a 5;
- valores ausentes em campos importantes.'''

import sqlite3
import pandas as pd

BANCO = "produtos.db"


def carregar_dados():
    with sqlite3.connect(BANCO) as conexao:
        return pd.read_sql_query(
            """
            SELECT id, nome, preco, categoria, estoque, avaliacao
            FROM produtos
            """,
            conexao
        )


def validar_dados(df):
    problemas = []

    for indice, produto in df.iterrows():
        erros = []

        if pd.isna(produto["id"]):
            erros.append("ID ausente")

        if pd.isna(produto["nome"]) or not str(
            produto["nome"]
        ).strip():
            erros.append("Nome vazio")

        if pd.isna(produto["preco"]):
            erros.append("Preço ausente")
        elif produto["preco"] < 0:
            erros.append("Preço negativo")

        if pd.isna(produto["estoque"]):
            erros.append("Estoque ausente")
        elif produto["estoque"] < 0:
            erros.append("Estoque negativo")

        if pd.isna(produto["avaliacao"]):
            erros.append("Avaliação ausente")
        elif not 0 <= produto["avaliacao"] <= 5:
            erros.append("Avaliação fora do intervalo de 0 a 5")

        if pd.isna(produto["categoria"]) or not str(
            produto["categoria"]
        ).strip():
            erros.append("Categoria ausente")

        if erros:
            problemas.append({
                "linha": indice + 1,
                "produto": produto.get("nome", ""),
                "problemas": "; ".join(erros)
            })

    ids_duplicados = df[
        df["id"].duplicated(keep=False)
    ]

    for _, produto in ids_duplicados.iterrows():
        problemas.append({
            "linha": produto.name + 1,
            "produto": produto.get("nome", ""),
            "problemas": "ID duplicado"
        })

    return pd.DataFrame(
        problemas,
        columns=["linha", "produto", "problemas"]
    )


def main():
    try:
        df = carregar_dados()

        if df.empty:
            print("Nenhum produto encontrado.")
            return

        problemas = validar_dados(df)

        print("\n=== RELATÓRIO DE VALIDAÇÃO ===")
        print(f"Registros analisados: {len(df)}")
        print(f"Registros com problemas: {problemas['linha'].nunique() if not problemas.empty else 0}")

        if problemas.empty:
            print("Nenhum problema encontrado.")
        else:
            print(problemas.to_string(index=False))
            problemas.to_csv(
                "problemas_produtos.csv",
                index=False,
                encoding="utf-8-sig"
            )
            print("\nRelatório salvo em problemas_produtos.csv")

    except (sqlite3.Error, OSError, ValueError, KeyError) as erro:
        print(f"Erro durante a validação: {erro}")


if __name__ == "__main__":
    main()
    