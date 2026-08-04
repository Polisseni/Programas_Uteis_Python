'''Nível: Intermediário

Conceitos:

Várias funções
Organização do código

Objetivo:
Separar cada operação matemática em uma função diferente.

Arquivo:'''

# Calculadora utilizando funções

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


numero1 = float(input("Primeiro número: "))
operacao = input("Operação (+, -, *, /): ")
numero2 = float(input("Segundo número: "))

if operacao == "+":
    print("Resultado:", somar(numero1, numero2))
elif operacao == "-":
    print("Resultado:", subtrair(numero1, numero2))
elif operacao == "*":
    print("Resultado:", multiplicar(numero1, numero2))
elif operacao == "/":
    if numero2 != 0:
        print("Resultado:", dividir(numero1, numero2))
    else:
        print("Não é possível dividir por zero.")
else:
    print("Operação inválida.")
    