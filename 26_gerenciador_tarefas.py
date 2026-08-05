'''Nível: Intermediário

Conceitos:

Listas
Funções
Laço while
Menus
Organização do código

Objetivo:
Criar um pequeno sistema que permita adicionar, listar e remover tarefas.'''

# Gerenciador simples de tarefas

tarefas = []


def adicionar():
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!\n")


def listar():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
        return

    print("\nLista de tarefas:")

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"{indice}. {tarefa}")

    print()


def remover():
    listar()

    if tarefas:
        indice = int(input("Número da tarefa que deseja remover: ")) - 1

        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            print("Tarefa removida!\n")
        else:
            print("Número inválido.\n")


while True:
    print("===== MENU =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar()

    elif opcao == "2":
        listar()

    elif opcao == "3":
        remover()

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.\n")
        