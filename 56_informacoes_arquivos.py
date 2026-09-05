'''Nível: Avançado
Conceitos: pathlib, tamanho de arquivos, stat(), conversão de unidades

Objetivo: criar um programa que percorra uma pasta e mostre o nome e o tamanho de cada arquivo.'''

from pathlib import Path


def tamanho_formatado(tamanho):
    if tamanho < 1024:
        return f"{tamanho} B"

    if tamanho < 1024 ** 2:
        return f"{tamanho / 1024:.2f} KB"

    if tamanho < 1024 ** 3:
        return f"{tamanho / (1024 ** 2):.2f} MB"

    return f"{tamanho / (1024 ** 3):.2f} GB"


def listar_arquivos(pasta):
    caminho = Path(pasta)

    if not caminho.exists() or not caminho.is_dir():
        print("Pasta inválida.")
        return

    arquivos = [arquivo for arquivo in caminho.rglob("*") if arquivo.is_file()]

    if not arquivos:
        print("Nenhum arquivo encontrado.")
        return

    print("\nArquivos encontrados:\n")

    for arquivo in arquivos:
        tamanho = arquivo.stat().st_size

        print(f"Nome: {arquivo.name}")
        print(f"Tamanho: {tamanho_formatado(tamanho)}")
        print(f"Caminho: {arquivo}")
        print("-" * 40)


pasta = input("Digite a pasta: ")

listar_arquivos(pasta)
