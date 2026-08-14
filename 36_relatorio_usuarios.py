'''Nível: Intermediário++

Conceitos:

CSV
Funções
Listas
Dicionários
Processamento de dados
Geração de arquivos
Formatação de strings

Objetivo: ler os usuários do CSV e gerar automaticamente um arquivo relatorio.txt contendo um resumo dos dados.'''

import csv

ARQUIVO_CSV = "usuarios.csv"
ARQUIVO_RELATORIO = "relatorio.txt"


def gerar_relatorio():
    usuarios = []

    try:
        with open(ARQUIVO_CSV, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for usuario in leitor:
                usuario["idade"] = int(usuario["idade"])
                usuarios.append(usuario)

    except FileNotFoundError:
        print("Arquivo usuarios.csv não encontrado.")
        return

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    idades = [usuario["idade"] for usuario in usuarios]

    media = sum(idades) / len(idades)

    with open(ARQUIVO_RELATORIO, "w", encoding="utf-8") as arquivo:
        arquivo.write("===== RELATÓRIO DE USUÁRIOS =====\n\n")

        arquivo.write(f"Total de usuários: {len(usuarios)}\n")
        arquivo.write(f"Idade média: {media:.2f}\n")
        arquivo.write(f"Maior idade: {max(idades)}\n")
        arquivo.write(f"Menor idade: {min(idades)}\n\n")

        arquivo.write("USUÁRIOS:\n")

        for usuario in usuarios:
            arquivo.write(
                f"- {usuario['nome']} | "
                f"{usuario['idade']} anos | "
                f"{usuario['cidade']}\n"
            )

    print("Relatório criado com sucesso!")


gerar_relatorio()
