'''Nível: Expert++
Conceitos: requests, HTTP, JSON, API, tratamento de erros

Objetivo: consultar uma API pública e exibir informações retornadas em formato JSON.'''

'''Instale a biblioteca antes:
pip install requests'''

import requests


url = "https://jsonplaceholder.typicode.com/users"

try:
    resposta = requests.get(url, timeout=10)

    resposta.raise_for_status()

    usuarios = resposta.json()

    print("\n=== USUÁRIOS ===")

    for usuario in usuarios:
        print(f"ID: {usuario['id']}")
        print(f"Nome: {usuario['name']}")
        print(f"E-mail: {usuario['email']}")
        print("-" * 30)

except requests.RequestException as erro:
    print(f"Erro ao acessar a API: {erro}")
    