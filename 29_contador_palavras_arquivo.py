'''Nível: Intermediário

Conceitos:

Arquivos
Strings
split()
len()

Objetivo:
Contar quantas palavras existem em um arquivo de texto.'''

# Conta as palavras de um arquivo

try:
    with open("anotacoes.txt", "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

    palavras = texto.split()

    print(f"O arquivo possui {len(palavras)} palavras.")

except FileNotFoundError:
    print("Arquivo não encontrado.")
    