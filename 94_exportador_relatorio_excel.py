'''Conceitos: SQLite, Pandas, Excel, openpyxl, tratamento de erros.
Objetivo
Consultar os produtos do banco SQLite e exportar os dados para uma planilha Excel, incluindo uma segunda aba com indicadores gerais.'''

import sqlite3
import pandas as pd

BANCO = "produtos.db"
ARQUIVO_SAIDA = "relatorio_produtos.xlsx"


def carregar_produtos():
    with sqlite3.connect(BANCO) as conexao:
        consulta = """
            SELECT
                id,
                nome,
                preco,
                categoria,
                estoque,
                avaliacao
            FROM produtos
            ORDER BY categoria, nome
        """

        return pd.read_sql_query(consulta, conexao)


def gerar_indicadores(df):
    if df.empty:
        return pd.DataFrame({
            "Indicador": ["Total de produtos"],
            "Valor": [0]
        })

    indicadores = {
        "Total de produtos": len(df),
        "Preço médio": round(df["preco"].mean(), 2),
        "Maior preço": round(df["preco"].max(), 2),
        "Menor preço": round(df["preco"].min(), 2),
        "Unidades em estoque": int(df["estoque"].sum()),
        "Valor estimado do estoque": round(
            (df["preco"] * df["estoque"]).sum(), 2
        )
    }

    return pd.DataFrame(
        indicadores.items(),
        columns=["Indicador", "Valor"]
    )


def exportar_excel(produtos, indicadores):
    with pd.ExcelWriter(
        ARQUIVO_SAIDA,
        engine="openpyxl"
    ) as escritor:
        produtos.to_excel(
            escritor,
            sheet_name="Produtos",
            index=False
        )

        indicadores.to_excel(
            escritor,
            sheet_name="Indicadores",
            index=False
        )


def main():
    try:
        produtos = carregar_produtos()

        if produtos.empty:
            print("Nenhum produto encontrado no banco.")
            return

        indicadores = gerar_indicadores(produtos)
        exportar_excel(produtos, indicadores)

        print(f"Relatório gerado: {ARQUIVO_SAIDA}")
        print(f"Produtos exportados: {len(produtos)}")

    except (sqlite3.Error, OSError, ValueError) as erro:
        print(f"Erro ao gerar relatório: {erro}")


if __name__ == "__main__":
    main()
    