frase = str (input('Digite uma frase: '))

i = 0
v = 0

for i in frase:
    if (i == 'A' or i == 'a'
    or i == 'E' or i == 'e'
    or i == 'I' or i == 'i'
    or i == 'O' or i == 'o'
    or i == 'U' or i == 'u'):
        v = v + 1

print('O número de vogais é: ' + str(v))

input()