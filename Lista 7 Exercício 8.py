# 8.	Uma entidade beneficente fez um sorteio cujos bilhetes continham números de 6 dígitos. O sorteio foi baseado nos dois primeiros prêmios da loteria federal, sendo o número sorteado formado pelos três últimos dígitos do primeiro e do segundo prêmio. Por exemplo, se o primeiro prêmio fosse 34.582 e o segundo 54.098, o número da LBV seria 582.098. Escreva um programa que lê os dois prêmios e retorna o número sorteado.

n1 = input("Digite o número do 1° prêmio: ")
n2 = input("Digite o número do 2° prêmio: ")

print(n1[3:6], end=".")
print(n2[3:6])

input()