'''Objetivo: testar automaticamente a função de validação criada no exercício 103, sem precisar executar o programa manualmente para cada caso.'''

'test_validacoes.py'


import pytest

from validacoes import (
    validar_produto,
    NomeInvalidoError,
    PrecoInvalidoError,
    EstoqueInvalidoError
)


def test_produto_valido():
    produto = validar_produto("Teclado", 120.0, 5)

    assert produto == {
        "nome": "Teclado",
        "preco": 120.0,
        "estoque": 5
    }


def test_nome_vazio():
    with pytest.raises(NomeInvalidoError):
        validar_produto("   ", 120.0, 5)


def test_preco_zero():
    with pytest.raises(PrecoInvalidoError):
        validar_produto("Teclado", 0, 5)


def test_estoque_negativo():
    with pytest.raises(EstoqueInvalidoError):
        validar_produto("Teclado", 120.0, -1)

