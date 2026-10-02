'''Dificuldade: 🟡 Intermediário+
Conceitos: os, variáveis de ambiente, segurança de credenciais, requests

Objetivo

No exercício anterior, o token estava diretamente no código:

TOKEN = "meu-token-de-exemplo"

Isso é uma prática ruim para projetos reais, principalmente quando o código vai para o GitHub.

Agora vamos obter o token através de uma variável de ambiente.'''

import os
import requests

URL = "https://httpbin.org/bearer"

TOKEN = os.getenv("API_TOKEN")

def consultar_api():
    if not TOKEN:
        print("Erro: a variável API_TOKEN não foi configurada.")
        return

    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    try:
        resposta = requests.get(
            URL,
            headers=headers,
            timeout=10
        )

        resposta.raise_for_status()

        dados = resposta.json()

        print("\n=== RESPOSTA DA API ===")
        print(f"Autenticado: {dados.get('authenticated')}")

    except requests.RequestException as erro:
        print(f"Erro na requisição: {erro}")
    except ValueError:
        print("A API não retornou um JSON válido.")


consultar_api()
