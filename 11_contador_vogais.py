'''Nível: Iniciante+

Conceitos:

Strings
Laço for
Condicionais
Operador in

Objetivo:
Solicitar uma palavra ou frase ao usuário e informar quantas vogais ela possui.'''

# Conta a quantidade de vogais em uma palavra ou frase

texto = input("Digite uma palavra ou frase: ").lower()

vogais = "aeiou"
contador = 0

for letra in texto:
    if letra in vogais:
        contador += 1

print(f"\nO texto possui {contador} vogais.")
