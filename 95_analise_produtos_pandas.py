'''Conceitos: Pandas, DataFrame, groupby(), filtros, ordenação, estatística descritiva.
Objetivo
Construir um analisador que identifique as categorias com maior valor em estoque, os produtos mais caros e os produtos que precisam de reposição.'''

import sqlite3
import pandas as pd

BANCO = "produtos.db"
LIMITE_ESTOQUE_BAIXO = 10


def carregar_dados():
    with sqlite3.connect(BANCO) as conexao:
        consulta = """
            SELECT id, nome, preco, categoria, estoque, avaliacao
            FROM produtos
        """

        return pd.read_sql_query(consulta, conexao)


def analisar_categorias(df):
    resultado = (
        df.groupby("categoria")
        .agg(
            quantidade_produtos=("id", "count"),
            preco_medio=("preco", "mean"),
            unidades_estoque=("estoque", "sum"),
            valor_estoque=("valor_estoque", "sum")
        )
        .sort_values("valor_estoque", ascending=False)
    )

    return resultado.round(2)


def analisar_estoque_baixo(df):
    return (
        df[df["estoque"] <= LIMITE_ESTOQUE_BAIXO]
        .sort_values(["estoque", "nome"])
    )


def main():
    try:
        df = carregar_dados()

        if df.empty:
            print("Nenhum produto cadastrado.")
            return

        # Cria uma coluna calculada.
        df["valor_estoque"] = df["preco"] * df["estoque"]

        print("\n=== 5 PRODUTOS MAIS CAROS ===")
        print(
            df.nlargest(5, "preco")[
                ["nome", "categoria", "preco"]
            ].to_string(index=False)
        )

        print("\n=== CATEGORIAS POR VALOR EM ESTOQUE ===")
        print(analisar_categorias(df).to_string())

        print("\n=== PRODUTOS COM ESTOQUE BAIXO ===")
        baixo = analisar_estoque_baixo(df)

        if baixo.empty:
            print("Nenhum produto precisa de atenção.")
        else:
            print(
                baixo[
                    ["nome", "estoque", "preco"]
                ].to_string(index=False)
            )

        print("\n=== RESUMO ESTATÍSTICO ===")
        print(
            df[["preco", "estoque", "avaliacao"]]
            .describe()
            .round(2)
        )

    except (sqlite3.Error, OSError, ValueError, KeyError) as erro:
        print(f"Erro durante a análise: {erro}")


if __name__ == "__main__":
    main()
    