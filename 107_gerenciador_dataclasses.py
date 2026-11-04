'''Objetivo: utilizar @dataclass para representar produtos, aplicar validações e organizar um catálogo de produtos em memória.'''

"modelos"


from dataclasses import dataclass, field


@dataclass
class Produto:
    nome: str
    preco: float
    estoque: int
    valor_total: float = field(init=False)

    def __post_init__(self):
        self.nome = self.nome.strip()

        if not self.nome:
            raise ValueError("Nome não pode ser vazio.")

        if self.preco <= 0:
            raise ValueError("Preço deve ser positivo.")

        if self.estoque < 0:
            raise ValueError("Estoque não pode ser negativo.")

        self.atualizar_valor_total()

    def atualizar_valor_total(self):
        self.valor_total = self.preco * self.estoque

    def vender(self, quantidade: int):
        if quantidade <= 0:
            raise ValueError("Quantidade inválida.")

        if quantidade > self.estoque:
            raise ValueError("Estoque insuficiente.")

        self.estoque -= quantidade
        self.atualizar_valor_total()


@dataclass
class Catalogo:
    produtos: list[Produto] = field(default_factory=list)

    def adicionar(self, produto: Produto):
        self.produtos.append(produto)

    def valor_total(self) -> float:
        return sum(p.valor_total for p in self.produtos)

    def listar(self):
        for produto in self.produtos:
            print(
                f"{produto.nome} | "
                f"R$ {produto.preco:.2f} | "
                f"Estoque: {produto.estoque}"
            )


"main"


from modelos import Produto, Catalogo


def main():
    catalogo = Catalogo()

    try:
        catalogo.adicionar(
            Produto("Notebook", 3500.00, 5)
        )

        catalogo.adicionar(
            Produto("Mouse", 80.00, 20)
        )

        catalogo.adicionar(
            Produto("Teclado", 150.00, 10)
        )

        print("CATÁLOGO INICIAL")
        catalogo.listar()

        print("\nRegistrando venda...")

        catalogo.produtos[0].vender(2)

        print("\nCATÁLOGO ATUALIZADO")
        catalogo.listar()

        print(
            f"\nValor total do estoque: "
            f"R$ {catalogo.valor_total():.2f}"
        )

    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()

