'''Dificuldade: 🔴 Intermediário avançado+
Conceitos: SQLite, agregações SQL, estatística descritiva, funções, classificação de dados.
Objetivo
Criar um relatório que analise os produtos armazenados no banco, calculando:
- quantidade total de produtos;
- preço médio;
- menor e maior preço;
- valor total estimado do estoque;
- quantidade de produtos com estoque baixo;
- distribuição de produtos por categoria.'''

import sqlite3

BANCO = "produtos.db"
LIMITE_ESTOQUE_BAIXO = 10


def conectar():
    return sqlite3.connect(BANCO)


def obter_indicadores():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            COALESCE(AVG(preco), 0),
            COALESCE(MIN(preco), 0),
            COALESCE(MAX(preco), 0),
            COALESCE(SUM(preco * estoque), 0),
            COALESCE(SUM(
                CASE
                    WHEN estoque <= ? THEN 1
                    ELSE 0
                END
            ), 0)
        FROM produtos
    """, (LIMITE_ESTOQUE_BAIXO,))

    resultado = cursor.fetchone()
    conexao.close()

    return resultado


def obter_categorias():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            categoria,
            COUNT(*) AS quantidade,
            ROUND(AVG(preco), 2) AS preco_medio
        FROM produtos
        GROUP BY categoria
        ORDER BY quantidade DESC, categoria ASC
    """)

    categorias = cursor.fetchall()
    conexao.close()

    return categorias


def exibir_relatorio():
    dados = obter_indicadores()

    print("\n=== INDICADORES GERAIS ===")
    print(f"Total de produtos: {dados[0]}")
    print(f"Preço médio: ${dados[1]:.2f}")
    print(f"Menor preço: ${dados[2]:.2f}")
    print(f"Maior preço: ${dados[3]:.2f}")
    print(f"Valor estimado do estoque: ${dados[4]:.2f}")
    print(
        f"Produtos com estoque baixo "
        f"(até {LIMITE_ESTOQUE_BAIXO} unidades): {dados[5]}"
    )

    categorias = obter_categorias()

    print("\n=== ANÁLISE POR CATEGORIA ===")

    if not categorias:
        print("Nenhum produto cadastrado.")
        return

    for categoria, quantidade, preco_medio in categorias:
        print(
            f"{categoria}: "
            f"{quantidade} produtos | "
            f"Preço médio: ${preco_medio:.2f}"
        )


if __name__ == "__main__":
    exibir_relatorio()
    