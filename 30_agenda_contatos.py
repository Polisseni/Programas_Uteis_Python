'''Nível: Intermediário+

Conceitos:

Arquivos
Funções
Menus
append()

Objetivo:
Cadastrar contatos em um arquivo .txt.'''

# Agenda simples utilizando arquivo texto

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")

    with open("contatos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome} - {telefone}\n")

    print("Contato salvo!\n")


def listar_contatos():
    try:
        with open("contatos.txt", "r", encoding="utf-8") as arquivo:
            print("\nContatos:\n")
            print(arquivo.read())

    except FileNotFoundError:
        print("Nenhum contato cadastrado.\n")


while True:
    print("1 - Adicionar")
    print("2 - Listar")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_contato()

    elif opcao == "2":
        listar_contatos()

    elif opcao == "0":
        break

    else:
        print("Opção inválida.\n")
        