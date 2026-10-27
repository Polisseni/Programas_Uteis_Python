'''Conceitos: testes unitários, pytest, funções puras, casos-limite e asserções.
Objetivo
Aprender a verificar automaticamente se as regras do programa funcionam corretamente, sem depender de uma API ou de um banco de dados real.

Neste exercício, vamos criar funções de validação e testar seus comportamentos.'''

def validar_preco(preco):
    if not isinstance(preco, (int, float)):
        return False

    if isinstance(preco, bool):
        return False

    return preco >= 0


def validar_estoque(quantidade):
    if not isinstance(quantidade, int):
        return False

    if isinstance(quantidade, bool):
        return False

    return quantidade >= 0


def calcular_valor_estoque(preco, quantidade):
    if not validar_preco(preco):
        raise ValueError("Preço inválido.")

    if not validar_estoque(quantidade):
        raise ValueError("Quantidade inválida.")

    return preco * quantidade


def classificar_estoque(quantidade, limite=10):
    if not validar_estoque(quantidade):
        raise ValueError("Quantidade inválida.")

    if quantidade <= limite:
        return "baixo"

    return "adequado"
