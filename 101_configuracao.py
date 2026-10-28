'''Conceitos: os, python-dotenv, variáveis de ambiente, configuração, segurança e separação entre código e ambiente.
Objetivo
Retirar configurações fixas do código, permitindo que o nome do banco, o limite de estoque baixo e o modo de execução sejam configurados externamente.'''

'''101_configuracao/
├── main.py
├── config.py
├── .env
└── .gitignore'''

'''1. Instale a dependência'''

'''pip install python-dotenv'''

'''2. Crie o arquivo .env'''

'''BANCO_DADOS=produtos_config.db
LIMITE_ESTOQUE_BAIXO=10
MODO_DEBUG=false'''


'''3. Crie o arquivo .gitignore'''

'''.env
__pycache__/
*.pyc
*.db
.venv/'''

'''4. Crie config.py'''

import os
from dotenv import load_dotenv

load_dotenv()


def obter_configuracao():
    banco = os.getenv(
        "BANCO_DADOS",
        "produtos_config.db"
    )

    try:
        limite = int(
            os.getenv("LIMITE_ESTOQUE_BAIXO", "10")
        )
    except ValueError as erro:
        raise ValueError(
            "LIMITE_ESTOQUE_BAIXO deve ser um inteiro."
        ) from erro

    if limite < 0:
        raise ValueError(
            "O limite de estoque não pode ser negativo."
        )

    modo_debug = os.getenv(
        "MODO_DEBUG", "false"
    ).strip().lower()

    if modo_debug not in {"true", "false"}:
        raise ValueError(
            "MODO_DEBUG deve ser true ou false."
        )

    return {
        "banco": banco,
        "limite_estoque_baixo": limite,
        "modo_debug": modo_debug == "true"
    }

'''5. Crie main.py'''

import logging
import sqlite3

from config import obter_configuracao


def main():
    try:
        config = obter_configuracao()

        logging.basicConfig(
            level=(
                logging.DEBUG
                if config["modo_debug"]
                else logging.INFO
            ),
            format="%(levelname)s: %(message)s"
        )

        logging.info("Iniciando sistema.")

        with sqlite3.connect(config["banco"]) as conexao:
            conexao.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco REAL NOT NULL CHECK(preco >= 0),
                    estoque INTEGER NOT NULL CHECK(estoque >= 0)
                )
            """)

            cursor = conexao.execute("""
                SELECT COUNT(*)
                FROM produtos
                WHERE estoque <= ?
            """, (config["limite_estoque_baixo"],))

            quantidade = cursor.fetchone()[0]

        print(f"Banco utilizado: {config['banco']}")
        print(
            "Limite de estoque baixo: "
            f"{config['limite_estoque_baixo']}"
        )
        print(
            f"Produtos com estoque baixo: {quantidade}"
        )

        logging.info("Execução concluída.")

    except (ValueError, sqlite3.Error) as erro:
        logging.error("Falha na execução: %s", erro)


if __name__ == "__main__":
    main()

    