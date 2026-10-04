'''Dificuldade: 🟠 Intermediário+
Conceitos: API, parâmetros, funções, menus, tratamento de erros, filtragem de dados

Objetivo

Construir um pequeno sistema de terminal que permita ao usuário:

listar produtos;
pesquisar produtos pelo nome;
visualizar detalhes de um produto;
encerrar o programa.'''

import requests

BASE_URL = "https://dummyjson.com/products"


def buscar_produtos():
    try:
        resposta = requests.get(BASE_URL, timeout=10)
        resposta.raise_for_status()
        return resposta.json()["products"]

    except requests.RequestException as erro:
        print(f"Erro ao acessar a API: {erro}")
        return []


def pesquisar_produtos(produtos, termo):
    termo = termo.lower()

    resultados = [
        produto
        for produto in produtos
        if termo in produto["title"].lower()
    ]

    return resultados


def mostrar_produtos(produtos):
    if not produtos:
        print("\nNenhum produto encontrado.")
        return

    print("\n=== PRODUTOS ===")

    for produto in produtos:
        print(
            f"ID: {produto['id']} | "
            f"{produto['title']} | "
            f"Preço: ${produto['price']}"
        )


def mostrar_detalhes(produtos, produto_id):
    for produto in produtos:
        if produto["id"] == produto_id:
            print("\n=== DETALHES DO PRODUTO ===")
            print(f"ID: {produto['id']}")
            print(f"Nome: {produto['title']}")
            print(f"Preço: ${produto['price']}")
            print(f"Categoria: {produto['category']}")
            print(f"Estoque: {produto['stock']}")
            print(f"Avaliação: {produto['rating']}")
            print(f"Descrição: {produto['description']}")
            return

    print("\nProduto não encontrado.")


def menu(produtos):
    while True:
        print("\n=== SISTEMA DE PRODUTOS ===")
        print("1 - Listar produtos")
        print("2 - Pesquisar produto")
        print("3 - Ver detalhes")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            mostrar_produtos(produtos)

        elif opcao == "2":
            termo = input("Digite o nome do produto: ").strip()

            resultados = pesquisar_produtos(
                produtos,
                termo
            )

            mostrar_produtos(resultados)

        elif opcao == "3":
            try:
                produto_id = int(
                    input("Digite o ID do produto: ")
                )

                mostrar_detalhes(
                    produtos,
                    produto_id
                )

            except ValueError:
                print("Digite um ID numérico válido.")

        elif opcao == "4":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


def main():
    produtos = buscar_produtos()

    if not produtos:
        return

    menu(produtos)


main()
