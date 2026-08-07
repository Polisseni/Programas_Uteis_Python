'''Nível: Intermediário

Conceitos:

Manipulação de arquivos
open()
Modo "w"
with

Objetivo:
Solicitar um texto ao usuário e salvá-lo em um arquivo.'''

# Cria um arquivo de texto

texto = input("Digite um texto: ")

with open("anotacoes.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(texto)

print("Arquivo salvo com sucesso!")
