'''Nível: Avançado inicial

Conceitos:

datetime
timedelta
Diferença entre datas
Funções
try/except

Objetivo: informar quantos dias existem entre duas datas fornecidas pelo usuário.'''

from datetime import datetime


def calcular_diferenca(data1, data2):
    diferenca = abs(data2 - data1)
    return diferenca.days


try:
    primeira_data = input("Digite a primeira data (DD/MM/AAAA): ")
    segunda_data = input("Digite a segunda data (DD/MM/AAAA): ")

    data1 = datetime.strptime(primeira_data, "%d/%m/%Y")
    data2 = datetime.strptime(segunda_data, "%d/%m/%Y")

    dias = calcular_diferenca(data1, data2)

    print(f"\nAs datas possuem {dias} dias de diferença.")

except ValueError:
    print("Data inválida. Utilize o formato DD/MM/AAAA.")
    