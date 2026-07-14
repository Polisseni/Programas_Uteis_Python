'''Nível: Iniciante+

Conceitos:

Strings
replace()
lower()
Comparação de textos

Objetivo:
Verificar se uma palavra ou frase é um palíndromo (lê-se da mesma forma de trás para frente), ignorando espaços e 
diferenças entre maiúsculas e minúsculas.'''

# Verifica se uma palavra ou frase é um palíndromo

texto = input("Digite uma palavra ou frase: ")

texto_formatado = texto.replace(" ", "").lower()

if texto_formatado == texto_formatado[::-1]:
    print("\nÉ um palíndromo!")
else:
    print("\nNão é um palíndromo.")
    