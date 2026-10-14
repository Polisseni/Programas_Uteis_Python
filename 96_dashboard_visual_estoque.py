'''Conceitos: Matplotlib, Pandas, visualização de dados, gráficos de barras, subplots e exportação de imagens.
Objetivo
Evoluir o analisador anterior para gerar um dashboard visual com três gráficos:
1. Valor estimado do estoque por categoria.
2. Os dez produtos com maior valor em estoque.
3. Quantidade de produtos com estoque baixo e estoque adequado.'''

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

BANCO = "produtos.db"
LIMITE_ESTOQUE_BAIXO = 10


def carregar_dados():
    with sqlite3.connect(BANCO) as conexao:
        consulta = """
            SELECT id, nome, preco, categoria, estoque
            FROM produtos
        """

        return pd.read_sql_query(consulta, conexao)


def preparar_dados(df):
    df = df.copy()

    df["categoria"] = (
        df["categoria"].fillna("Sem categoria")
    )

    df["valor_estoque"] = df["preco"] * df["estoque"]

    df["situacao"] = df["estoque"].apply(
        lambda quantidade:
            "Estoque baixo"
            if quantidade <= LIMITE_ESTOQUE_BAIXO
            else "Estoque adequado"
    )

    return df


def gerar_dashboard(df):
    valor_por_categoria = (
        df.groupby("categoria")["valor_estoque"]
        .sum()
        .sort_values(ascending=False)
    )

    dez_maiores = (
        df.nlargest(10, "valor_estoque")
        .sort_values("valor_estoque")
    )

    contagem_estoque = (
        df["situacao"]
        .value_counts()
        .reindex(
            ["Estoque baixo", "Estoque adequado"],
            fill_value=0
        )
    )

    fig, eixos = plt.subplots(1, 3, figsize=(17, 6))

    valor_por_categoria.plot(
        kind="bar",
        ax=eixos[0]
    )
    eixos[0].set_title("Valor em estoque por categoria")
    eixos[0].set_xlabel("Categoria")
    eixos[0].set_ylabel("Valor estimado")
    eixos[0].tick_params(axis="x", rotation=60)

    eixos[1].barh(
        dez_maiores["nome"],
        dez_maiores["valor_estoque"]
    )
    eixos[1].set_title("10 maiores valores em estoque")
    eixos[1].set_xlabel("Valor estimado")
    eixos[1].tick_params(axis="y", labelsize=8)

    contagem_estoque.plot(
        kind="bar",
        ax=eixos[2]
    )
    eixos[2].set_title("Situação do estoque")
    eixos[2].set_xlabel("Classificação")
    eixos[2].set_ylabel("Quantidade de produtos")
    eixos[2].tick_params(axis="x", rotation=20)

    fig.suptitle("Dashboard de Análise de Estoque")
    fig.tight_layout()

    fig.savefig(
        "dashboard_estoque.png",
        dpi=150,
        bbox_inches="tight"
    )

    plt.show()
    plt.close(fig)


def main():
    try:
        df = carregar_dados()

        if df.empty:
            print("Nenhum produto encontrado no banco.")
            return

        df = preparar_dados(df)
        gerar_dashboard(df)

        print("Dashboard salvo em dashboard_estoque.png")

    except (sqlite3.Error, OSError, ValueError, KeyError) as erro:
        print(f"Erro ao gerar dashboard: {erro}")


if __name__ == "__main__":
    main()
    