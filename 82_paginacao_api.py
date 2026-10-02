'''Nível: Expert+++++
Conceitos: APIs REST, parâmetros, paginação, limit, skip, listas, loops

Objetivo: criar um programa que consulte uma API em páginas e permita ao usuário navegar pelos resultados.

Vamos utilizar uma API de demonstração que disponibiliza paginação.'''

import requests


URL = "https://dummyjson.com/products"


def buscar_pagina(pagina, limite):
    skip = (pagina - 1) * limite

    parametros = {
        "limit": limite,
        "skip": skip
    }

    try:
        resposta = requests.get(
            URL,
            params=parametros,
            timeout=10
        )

        resposta.raise_for_status()

        return resposta.json()

    except requests.RequestException as erro:
        print(f"Erro ao acessar a API: {erro}")
        return None


def mostrar_produtos(dados):
    produtos = dados.get("products", [])

    if not produtos:
        print("Nenhum produto encontrado.")
        return

    print("\n=== PRODUTOS ===")

    for produto in produtos:
        print(
            f"ID: {produto['id']} | "
            f"{produto['title']} | "
            f"Preço: ${produto['price']}"
        )


def menu():
    pagina = 1
    limite = 5

    while True:

        dados = buscar_pagina(pagina, limite)

        if dados is None:
            break

        mostrar_produtos(dados)

        total = dados["total"]
        pagina_atual = pagina
        ultima_pagina = (total + limite - 1) // limite

        print(
            f"\nPágina {pagina_atual} "
            f"de {ultima_pagina}"
        )

        print("\nN - Próxima página")
        print("A - Página anterior")
        print("S - Sair")

        opcao = input("Escolha: ").strip().lower()

        if opcao == "n":

            if pagina < ultima_pagina:
                pagina += 1
            else:
                print("Você já está na última página.")

        elif opcao == "a":

            if pagina > 1:
                pagina -= 1
            else:
                print("Você já está na primeira página.")

        elif opcao == "s":
            break

        else:
            print("Opção inválida.")


menu()
