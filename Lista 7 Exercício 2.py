"""
2.	Considerando uma frase digitada pelo usuário, pede-se para verificar se é uma frase palíndromo, não levando em consideração espaços e caracteres especiais ou acentuados.
"""

frase = input("Digite a frase: ").lower()


fraseR = frase[::-1]

if frase == fraseR:
    print("É palíndromo") 
else:
    print("Não é palíndromo")

input()