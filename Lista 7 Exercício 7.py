# 7.	Faça um programa que leia duas strings e imprima a interseção entre elas. 
# Ex:   cabelo e pelo => e, l, o 



palavra = input("Escreva uma frase: ")
palavra2 = input("Escreva uma frase: ")


for car in palavra:
    for car2 in palavra2:
        if car == car2:
            print(car, end=", ")

input()