'''Nível: Expert++++
Conceitos: requests, parâmetros HTTP, JSON, params, APIs REST

Objetivo: permitir que o usuário informe um ID e buscar somente os dados correspondentes na API.'''

import requests


URL = "https://jsonplaceholder.typicode.com/users"


def buscar_usuario(id_usuario):
    parametros = {
        "id": id_usuario
    }

    try:
        resposta = requests.get(
            URL,
            params=parametros,
            timeout=10
        )

        resposta.raise_for_status()

        usuarios = resposta.json()

        if not usuarios:
            print("Usuário não encontrado.")
            return

        usuario = usuarios[0]

        print("\n=== USUÁRIO ===")
        print(f"ID: {usuario['id']}")
        print(f"Nome: {usuario['name']}")
        print(f"E-mail: {usuario['email']}")
        print(f"Telefone: {usuario['phone']}")
        print(f"Cidade: {usuario['address']['city']}")

    except requests.RequestException as erro:
        print(f"Erro ao consultar a API: {erro}")


try:
    id_usuario = int(input("Digite o ID do usuário: "))

    if id_usuario <= 0:
        print("O ID deve ser maior que zero.")
    else:
        buscar_usuario(id_usuario)

except ValueError:
    print("Digite um ID numérico.")
    