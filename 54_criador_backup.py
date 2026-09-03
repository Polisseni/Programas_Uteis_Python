'''Nível: Avançado
Conceitos: pathlib, shutil, datetime, cópia de arquivos, criação de diretórios

Objetivo: criar um programa que copie todos os arquivos de uma pasta para uma pasta de backup, criando uma pasta com a data e hora do backup.'''

from pathlib import Path
from datetime import datetime
import shutil


def criar_backup(origem):
    origem = Path(origem)

    if not origem.exists() or not origem.is_dir():
        print("A pasta informada não existe.")
        return

    data = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    destino = Path("backups") / f"backup_{data}"

    destino.mkdir(parents=True, exist_ok=True)

    arquivos = 0

    for arquivo in origem.rglob("*"):
        if arquivo.is_file():
            caminho_destino = destino / arquivo.relative_to(origem)
            caminho_destino.parent.mkdir(parents=True, exist_ok=True)

            shutil.copy2(arquivo, caminho_destino)
            arquivos += 1

    print(f"\nBackup concluído!")
    print(f"Arquivos copiados: {arquivos}")
    print(f"Local: {destino}")


pasta = input("Digite a pasta que deseja fazer backup: ")

criar_backup(pasta)
