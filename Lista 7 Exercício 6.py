# 6.	Faça um programa que leia uma string e crie uma outra string repetindo apenas as  vogais Ex:  carro => caarroo 

frase=input("Escreva uma frase: ")
x=["a","e","i","o","u", "A","E","I","O","U",]


for car in frase:
    if car in x:
        print(car * 2, end="") 
    else:
        print(car, end="")

input()