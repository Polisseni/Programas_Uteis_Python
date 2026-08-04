'''Nível: Intermediário

Conceitos:

Funções
Parâmetros
Retorno (return)

Objetivo:
Criar uma função que receba três notas e retorne a média.'''

# Calcula a média de três notas utilizando uma função

def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = calcular_media(nota1, nota2, nota3)

print(f"\nMédia: {media:.2f}")
