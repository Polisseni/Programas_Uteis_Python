'''Nível: Intermediário

Conceitos:

Funções
Retorno booleano (True/False)

Objetivo:
Criar uma função que informe se um número é par.'''

# Verifica se um número é par utilizando uma função

def eh_par(numero):
    return numero % 2 == 0


numero = int(input("Digite um número: "))

if eh_par(numero):
    print(f"{numero} é par.")
else:
    print(f"{numero} é ímpar.")
    