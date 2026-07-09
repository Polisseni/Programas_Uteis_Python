'''Nível: Iniciante+

Conceitos:

while
Acumuladores
Contadores

Objetivo:
Permitir que o usuário digite quantas notas desejar. 
O programa termina quando ele digita -1 e então calcula a média.'''

# Calcula a média de várias notas

soma = 0
quantidade = 0

print("Digite -1 para finalizar.\n")

while True:
    nota = float(input("Digite uma nota: "))

    if nota == -1:
        break

    soma += nota
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"\nMédia: {media:.2f}")
else:
    print("\nNenhuma nota foi informada.")
    