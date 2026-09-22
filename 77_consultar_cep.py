'''Nível: Expert+++
Conceitos: APIs REST, requests, JSON, entrada do usuário, validação e tratamento de erros

Objetivo: receber um CEP e consultar seus dados utilizando a API pública ViaCEP.'''

import requests


def consultar_cep(cep):
    cep = cep.replace("-", "").replace(".", "").strip()

    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=10)

        resposta.raise_for_status()

        dados = resposta.json()

        if dados.get("erro"):
            print("CEP não encontrado.")
            return

        print("\n=== ENDEREÇO ===")
        print(f"CEP: {dados['cep']}")
        print(f"Logradouro: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")
        print(f"DDD: {dados['ddd']}")

    except requests.RequestException as erro:
        print(f"Erro ao consultar o CEP: {erro}")


cep = input("Digite o CEP: ")

consultar_cep(cep)
