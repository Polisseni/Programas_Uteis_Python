'''Nível: Intermediário

Conceitos:

open()
Modo "r"
Leitura de arquivos
try/except

Objetivo:
Ler e exibir o conteúdo de um arquivo criado anteriormente.'''

# Lê o conteúdo de um arquivo

try:
    with open("anotacoes.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    print("\nConteúdo do arquivo:\n")
    print(conteudo)

except FileNotFoundError:
    print("Arquivo não encontrado.")
    