'''Nível: Avançado

Conceitos:

os
shutil
Manipulação de arquivos
Diretórios
Extensões
Automação
Condicionais

Objetivo: criar um programa que organize automaticamente os arquivos de uma pasta em subpastas de acordo com suas extensões.'''

import os
import shutil


PASTA_ORIGEM = "downloads"


CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Musicas": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi", ".mkv"]
}


def encontrar_categoria(extensao):
    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria

    return "Outros"


if not os.path.exists(PASTA_ORIGEM):
    os.makedirs(PASTA_ORIGEM)
    print(f"A pasta '{PASTA_ORIGEM}' foi criada.")
    print("Coloque alguns arquivos nela e execute novamente.")

else:
    for arquivo in os.listdir(PASTA_ORIGEM):

        caminho = os.path.join(PASTA_ORIGEM, arquivo)

        if not os.path.isfile(caminho):
            continue

        nome, extensao = os.path.splitext(arquivo)

        extensao = extensao.lower()

        categoria = encontrar_categoria(extensao)

        pasta_destino = os.path.join(PASTA_ORIGEM, categoria)

        os.makedirs(pasta_destino, exist_ok=True)

        destino = os.path.join(pasta_destino, arquivo)

        shutil.move(caminho, destino)

        print(f"Movido: {arquivo} → {categoria}/")

    print("\nOrganização concluída!")
    