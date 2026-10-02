'''Dificuldade: 🟠 Intermediário+
Conceitos: classes, requests, headers, métodos, encapsulamento, API

Agora vamos dar um passo importante: em vez de escrever toda a lógica de comunicação com a API em cada programa, 
vamos criar uma classe reutilizável.'''

import requests


class ClienteAPI:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token

    def _obter_headers(self):
        headers = {}

        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        return headers

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"

        try:
            resposta = requests.get(
                url,
                headers=self._obter_headers(),
                params=params,
                timeout=10
            )

            resposta.raise_for_status()

            return resposta.json()

        except requests.RequestException as erro:
            print(f"Erro na requisição: {erro}")
            return None

        except ValueError:
            print("A API não retornou um JSON válido.")
            return None


def main():
    cliente = ClienteAPI(
        "https://dummyjson.com"
    )

    dados = cliente.get("/products", {
        "limit": 5
    })

    if dados:
        print("\n=== PRODUTOS ===")

        for produto in dados["products"]:
            print(
                f"{produto['id']} - "
                f"{produto['title']} - "
                f"${produto['price']}"
            )


main()
