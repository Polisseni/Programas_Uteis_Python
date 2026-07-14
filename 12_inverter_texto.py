'''Nível: Iniciante+

Conceitos:

Strings
Fatiamento (slicing)

Objetivo:
Receber uma palavra ou frase e exibi-la invertida.'''

# Inverte uma palavra ou frase

texto = input("Digite uma palavra ou frase: ")

texto_invertido = texto[::-1]

print(f"\nTexto invertido: {texto_invertido}")
