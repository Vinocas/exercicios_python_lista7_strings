"""
1.	Considerando uma frase digitada pelo usuário, pede-se para imprimir:
a.	A quantidade de caracteres
b.	Separar (split) a frase nos espaços em branco.
c.	A frase invertida
d.	Toda a frase em caixa alta
e.	Toda a frase em caixa baixa

"""

frase = input("Digite a frase: ")

for indice in range (0,len(frase)):
    print(f"indice:{indice}")

print(frase.split())
print(frase[::-1])
print(frase.upper())
print(frase.lower())

input()