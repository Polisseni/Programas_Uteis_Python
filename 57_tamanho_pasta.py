'''Nível: Avançado
Conceitos: pathlib, funções, recursividade de diretórios, estatísticas

Objetivo: calcular quanto espaço todos os arquivos de uma determinada pasta estão ocupando.'''

from pathlib import Path


def calcular_tamanho(pasta):
    caminho = Path(pasta)

    if not caminho.exists() or not caminho.is_dir():
        print("Pasta inválida.")
        return

    total = 0
    quantidade = 0

    for arquivo in caminho.rglob("*"):
        if arquivo.is_file():
            total += arquivo.stat().st_size
            quantidade += 1

    print(f"\nArquivos encontrados: {quantidade}")
    print(f"Espaço utilizado: {total / (1024 ** 2):.2f} MB")


pasta = input("Digite a pasta: ")

calcular_tamanho(pasta)
