"""
4. Faça um programa que leia uma string e um caractere e diga quantas vezes o caractere aparece na string
"""

frase=input("Escreva uma frase: ")
car= input("Digite o caractere: ")
cont=0

for vog in frase:
    if vog in car:
        cont += 1

print(cont) 

input()