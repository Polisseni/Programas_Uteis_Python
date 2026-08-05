'''Nível: Intermediário

Conceitos:

Funções
try / except
Tratamento de exceções
Validação de entrada

Objetivo:
Criar uma calculadora que continue funcionando mesmo que o usuário digite valores inválidos.'''

# Calculadora com tratamento de exceções

def calcular(numero1, numero2, operacao):
    if operacao == "+":
        return numero1 + numero2
    elif operacao == "-":
        return numero1 - numero2
    elif operacao == "*":
        return numero1 * numero2
    elif operacao == "/":
        return numero1 / numero2
    else:
        return None


try:
    numero1 = float(input("Primeiro número: "))
    operacao = input("Operação (+, -, *, /): ")
    numero2 = float(input("Segundo número: "))

    resultado = calcular(numero1, numero2, operacao)

    if resultado is None:
        print("Operação inválida.")
    else:
        print(f"Resultado: {resultado}")

except ValueError:
    print("Erro: digite apenas números.")

except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")
    