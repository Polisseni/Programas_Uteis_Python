'''Nível: Avançado inicial

Conceitos:

Biblioteca datetime
Data e hora
Formatação com strftime()

Objetivo: criar um programa que mostre a data e o horário atuais formatados.'''

from datetime import datetime

# Obtém a data e hora atuais
agora = datetime.now()

data = agora.strftime("%d/%m/%Y")
horario = agora.strftime("%H:%M:%S")

print(f"Data atual: {data}")
print(f"Horário atual: {horario}")
