'''Nível: Avançado

Conceitos:

pathlib
Path
Percorrer diretórios
Verificação de arquivos
Extensões

Objetivo: criar um programa que procure todos os arquivos de uma determinada extensão dentro de uma pasta.'''

from pathlib import Path


def localizar_arquivos(pasta, extensao):
    caminho = Path(pasta)

    if not caminho.exists():
        print("A pasta informada não existe.")
        return

    arquivos = list(caminho.rglob(f"*{extensao}"))

    if not arquivos:
        print(f"Nenhum arquivo {extensao} encontrado.")
        return

    print(f"\nArquivos {extensao} encontrados:\n")

    for arquivo in arquivos:
        print(arquivo)


pasta = input("Digite o caminho da pasta: ")
extensao = input("Digite a extensão que deseja procurar (ex: .pdf): ")

localizar_arquivos(pasta, extensao)
