'''Objetivo: criar erros específicos para dados inválidos, separando a validação da execução principal.'''

'validacoes.py'


class ErroDeValidacao(Exception):
    """Erro base para validações do sistema."""


class NomeInvalidoError(ErroDeValidacao):
    pass


class PrecoInvalidoError(ErroDeValidacao):
    pass


class EstoqueInvalidoError(ErroDeValidacao):
    pass


def validar_produto(nome, preco, estoque):
    if not nome.strip():
        raise NomeInvalidoError("O nome não pode ficar vazio.")

    if preco <= 0:
        raise PrecoInvalidoError("O preço deve ser maior que zero.")

    if estoque < 0:
        raise EstoqueInvalidoError("O estoque não pode ser negativo.")

    return {
        "nome": nome.strip(),
        "preco": preco,
        "estoque": estoque
    }

'main.py'


from validacoes import (
    validar_produto,
    ErroDeValidacao
)


def main():
    try:
        nome = input("Nome do produto: ")
        preco = float(input("Preço: R$ "))
        estoque = int(input("Quantidade em estoque: "))

        produto = validar_produto(nome, preco, estoque)

        print("\nProduto validado:")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Estoque: {produto['estoque']}")

    except ValueError:
        print("Erro: informe preço e estoque em formatos válidos.")

    except ErroDeValidacao as erro:
        print(f"Erro de validação: {erro}")


if __name__ == "__main__":
    main()
