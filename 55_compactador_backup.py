'''Nível: Avançado+
Conceitos: pathlib, shutil, zipfile, datetime, compactação

Objetivo: transformar uma pasta em um arquivo .zip, criando um backup compactado automaticamente.'''

from pathlib import Path
from datetime import datetime
import shutil


def compactar_pasta(pasta):
    pasta = Path(pasta)

    if not pasta.exists() or not pasta.is_dir():
        print("A pasta informada não existe.")
        return

    data = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    destino = Path("backups") / f"backup_{data}"

    destino.parent.mkdir(parents=True, exist_ok=True)

    arquivo_zip = shutil.make_archive(
        str(destino),
        "zip",
        root_dir=pasta
    )

    print("\nBackup compactado com sucesso!")
    print(f"Arquivo: {arquivo_zip}")


pasta = input("Digite a pasta que deseja compactar: ")

compactar_pasta(pasta)
