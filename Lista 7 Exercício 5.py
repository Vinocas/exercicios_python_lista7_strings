# 5. Faça um programa que leia uma string e crie uma outra string repetindo os caracteres. Ex:  carro => ccaarrrroo


frase=input("Escreva uma frase: ")

for car in frase:
    print(car * 2, end="")

input ()