'''Nível: Expert++++

Conceitos:

API REST
JSON
SQLite
CRUD
Sincronização
JOIN/consultas
Menu interativo
Tratamento de erros
Separação em funções

Objetivo: reunir os conceitos anteriores em um pequeno sistema capaz de sincronizar usuários da API e depois pesquisá-los localmente.'''

import sqlite3
import requests


API_URL = "https://jsonplaceholder.typicode.com/users"
BANCO = "usuarios_api.db"


def conectar():
    conexao = sqlite3.connect(BANCO)

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT,
            cidade TEXT
        )
    """)

    conexao.commit()

    return conexao


def sincronizar(conexao):
    try:
        resposta = requests.get(API_URL, timeout=10)
        resposta.raise_for_status()

        usuarios = resposta.json()

    except requests.RequestException as erro:
        print(f"Erro ao acessar a API: {erro}")
        return

    cursor = conexao.cursor()

    for usuario in usuarios:
        cursor.execute("""
            INSERT OR REPLACE INTO usuarios
            (id, nome, email, telefone, cidade)
            VALUES (?, ?, ?, ?, ?)
        """, (
            usuario["id"],
            usuario["name"],
            usuario["email"],
            usuario["phone"],
            usuario["address"]["city"]
        ))

    conexao.commit()

    print(f"{len(usuarios)} usuários sincronizados.")


def listar(conexao):
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, email, cidade
        FROM usuarios
        ORDER BY nome
    """)

    usuarios = cursor.fetchall()

    if not usuarios:
        print("Nenhum usuário encontrado.")
        return

    print("\n=== USUÁRIOS ===")

    for usuario in usuarios:
        print(
            f"ID: {usuario[0]} | "
            f"Nome: {usuario[1]} | "
            f"E-mail: {usuario[2]} | "
            f"Cidade: {usuario[3]}"
        )


def buscar(conexao):
    termo = input("Digite o nome para pesquisar: ").strip()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, email, telefone, cidade
        FROM usuarios
        WHERE nome LIKE ?
        ORDER BY nome
    """, (f"%{termo}%",))

    resultados = cursor.fetchall()

    if not resultados:
        print("Nenhum usuário encontrado.")
        return

    print("\n=== RESULTADOS ===")

    for usuario in resultados:
        print(f"\nID: {usuario[0]}")
        print(f"Nome: {usuario[1]}")
        print(f"E-mail: {usuario[2]}")
        print(f"Telefone: {usuario[3]}")
        print(f"Cidade: {usuario[4]}")


def estatisticas(conexao):
    cursor = conexao.cursor()

    cursor.execute("SELECT COUNT(*) FROM usuarios")

    total = cursor.fetchone()[0]

    cursor.execute("""
        SELECT cidade, COUNT(*)
        FROM usuarios
        GROUP BY cidade
        ORDER BY COUNT(*) DESC
    """)

    cidades = cursor.fetchall()

    print("\n=== ESTATÍSTICAS ===")
    print(f"Total de usuários: {total}")

    print("\nUsuários por cidade:")

    for cidade in cidades:
        print(f"{cidade[0]}: {cidade[1]}")


def menu():
    conexao = conectar()

    while True:

        print("\n" + "=" * 40)
        print("       SISTEMA DE USUÁRIOS")
        print("=" * 40)
        print("1 - Sincronizar com API")
        print("2 - Listar usuários")
        print("3 - Buscar usuário")
        print("4 - Estatísticas")
        print("5 - Sair")
        print("=" * 40)

        opcao = input("Escolha: ")

        if opcao == "1":
            sincronizar(conexao)

        elif opcao == "2":
            listar(conexao)

        elif opcao == "3":
            buscar(conexao)

        elif opcao == "4":
            estatisticas(conexao)

        elif opcao == "5":
            break

        else:
            print("Opção inválida.")

    conexao.close()

    print("Programa encerrado.")


menu()
