'''Nível: Avançado inicial

Conceitos:

datetime
Datas
Operações com datas
Funções
Condicionais

Objetivo: pedir a data de nascimento do usuário e calcular sua idade atual.'''

from datetime import datetime


def calcular_idade(data_nascimento):
    hoje = datetime.now()

    idade = hoje.year - data_nascimento.year

    # Verifica se a pessoa já fez aniversário este ano
    aniversario = (hoje.month, hoje.day) < (
        data_nascimento.month,
        data_nascimento.day
    )

    if aniversario:
        idade -= 1

    return idade


data = input("Digite sua data de nascimento (DD/MM/AAAA): ")

try:
    data_nascimento = datetime.strptime(data, "%d/%m/%Y")

    idade = calcular_idade(data_nascimento)

    print(f"\nVocê tem {idade} anos.")

except ValueError:
    print("Data inválida. Utilize o formato DD/MM/AAAA.")
    