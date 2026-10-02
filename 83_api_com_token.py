'''Dificuldade: 🟡 Intermediário
Conceitos: requests, headers HTTP, token, funções, tratamento de erros

Objetivo

Aprender a enviar um token de autenticação no cabeçalho (Authorization) de uma requisição HTTP.

Para não depender de uma API que exija cadastro, vamos simular o token usando o endpoint público do HTTPBin.'''

import requests

URL = "https://httpbin.org/bearer"

TOKEN = "meu-token-de-exemplo"

def consultar_api():
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    try:
        resposta = requests.get(URL, headers=headers, timeout=10)
        resposta.raise_for_status()

        dados = resposta.json()

        print("\n=== RESPOSTA DA API ===")
        print(f"Token autorizado: {dados.get('authenticated')}")
        print(f"Token recebido: {dados.get('token')}")

    except requests.RequestException as erro:
        print(f"Erro na requisição: {erro}")
    except ValueError:
        print("A API não retornou um JSON válido.")


consultar_api()
