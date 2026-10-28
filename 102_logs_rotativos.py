'''Objetivo: registrar eventos e erros do programa em arquivos de log, criando arquivos de backup automaticamente quando o log atingir determinado tamanho.'''


import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

PASTA_LOGS = Path("logs")
PASTA_LOGS.mkdir(exist_ok=True)

arquivo_log = PASTA_LOGS / "sistema.log"

handler = RotatingFileHandler(
    arquivo_log,
    maxBytes=1024,
    backupCount=3,
    encoding="utf-8"
)

formato = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

handler.setFormatter(formato)

logger = logging.getLogger("sistema")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def executar_sistema():
    logger.info("Sistema iniciado.")

    try:
        numero = int(input("Digite um número inteiro: "))
        resultado = 100 / numero

        print(f"Resultado: {resultado}")
        logger.info("Operação concluída com sucesso.")

    except ValueError:
        print("Erro: digite um número inteiro válido.")
        logger.warning("O usuário digitou um valor inválido.")

    except ZeroDivisionError:
        print("Erro: divisão por zero.")
        logger.error("Tentativa de divisão por zero.")

    finally:
        logger.info("Execução finalizada.")

if __name__ == "__main__":
    executar_sistema()
