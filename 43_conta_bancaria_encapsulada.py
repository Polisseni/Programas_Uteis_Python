'''Nível: Intermediário/Avançado

Conceitos:

Encapsulamento
@property
@setter
Validação de atributos
Classes e métodos

Objetivo: melhorar a classe ContaBancaria do exercício 40, impedindo que o saldo seja alterado diretamente para um valor inválido.'''

# Conta bancária utilizando encapsulamento

class ContaBancaria:

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
        else:
            print("O saldo não pode ser negativo.")

    def depositar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            print("Depósito realizado com sucesso.")
        else:
            print("O valor deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor deve ser positivo.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo = self.saldo - valor
            print("Saque realizado com sucesso.")

    def consultar_saldo(self):
        print(f"Saldo: R$ {self.saldo:.2f}")


conta = ContaBancaria("Vitor", 1000)

conta.consultar_saldo()

conta.depositar(500)
conta.consultar_saldo()

conta.sacar(300)
conta.consultar_saldo()

conta.saldo = -500
conta.consultar_saldo()
