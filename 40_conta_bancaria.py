'''Nível: Intermediário++

Conceitos:

Classes e objetos
Atributos
Métodos
Alteração de estado
Condicionais

Objetivo: criar uma conta bancária que permita realizar depósitos, saques e consultar o saldo.'''

# Conta bancária utilizando POO

class ContaBancaria:

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print("Saque realizado com sucesso.")

    def consultar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")


titular = input("Nome do titular: ")

conta = ContaBancaria(titular)

conta.consultar_saldo()

deposito = float(input("\nValor para depósito: R$ "))
conta.depositar(deposito)

conta.consultar_saldo()

saque = float(input("\nValor para saque: R$ "))
conta.sacar(saque)

conta.consultar_saldo()
