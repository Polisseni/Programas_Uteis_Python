'''Nível: Intermediário

Conceitos:

Definição de funções (def)
Parâmetros
Retorno (return)
Reutilização de código

Objetivo:
Criar uma função que receba um número e retorne seu quadrado'''

# Calcula o quadrado de um número utilizando uma função

def calcular_quadrado(numero):
    return numero ** 2


valor = float(input("Digite um número: "))

resultado = calcular_quadrado(valor)

print(f"\nO quadrado de {valor} é {resultado}.")
