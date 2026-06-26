'''Exercício 3 — Calculadora simples

Nível: Iniciante +
Conceitos: operadores, condicionais

Objetivo:
Criar uma calculadora que faça soma, subtração, multiplicação e divisão.'''

# Calculadora simples

numero1 = float(input("Primeiro número: "))
operacao = input("Escolha (+, -, *, /): ")
numero2 = float(input("Segundo número: "))


if operacao == "+":
    resultado = numero1 + numero2

elif operacao == "-":
    resultado = numero1 - numero2

elif operacao == "*":
    resultado = numero1 * numero2

elif operacao == "/":
    resultado = numero1 / numero2

else:
    resultado = "Operação inválida"


print("Resultado:", resultado)
