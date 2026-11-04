'''Objetivo: criar uma estrutura reutilizável para armazenar e consultar diferentes tipos de objetos utilizando tipagem genérica.'''

"repositorio"


from typing import Generic, TypeVar, Protocol


class Identificavel(Protocol):
    id: int


T = TypeVar("T", bound=Identificavel)


class Repositorio(Generic[T]):

    def __init__(self):
        self._dados: dict[int, T] = {}

    def adicionar(self, objeto: T) -> None:
        if objeto.id in self._dados:
            raise ValueError("ID já cadastrado.")

        self._dados[objeto.id] = objeto

    def buscar(self, identificador: int) -> T | None:
        return self._dados.get(identificador)

    def listar(self) -> list[T]:
        return list(self._dados.values())

    def remover(self, identificador: int) -> bool:
        if identificador not in self._dados:
            return False

        del self._dados[identificador]
        return True

    def quantidade(self) -> int:
        return len(self._dados)


"main"


from dataclasses import dataclass
from repositorio import Repositorio


@dataclass
class Produto:
    id: int
    nome: str
    preco: float


@dataclass
class Cliente:
    id: int
    nome: str
    email: str


def main():
    produtos = Repositorio[Produto]()
    clientes = Repositorio[Cliente]()

    produtos.adicionar(
        Produto(1, "Notebook", 3500.00)
    )

    produtos.adicionar(
        Produto(2, "Mouse", 80.00)
    )

    clientes.adicionar(
        Cliente(1, "Ana", "ana@email.com")
    )

    clientes.adicionar(
        Cliente(2, "Carlos", "carlos@email.com")
    )

    print("PRODUTOS")
    for produto in produtos.listar():
        print(produto)

    print("\nCLIENTES")
    for cliente in clientes.listar():
        print(cliente)

    print("\nBUSCA DE PRODUTO")
    print(produtos.buscar(1))

    print("\nREMOVENDO PRODUTO")
    produtos.remover(2)

    print("Produtos restantes:", produtos.quantidade())


if __name__ == "__main__":
    main()
