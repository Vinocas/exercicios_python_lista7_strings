def pangrama(str):
    alfabeto = "abcdefghijklmnopqrstuvxwyz"
    for char in alfabeto:
        if char not in str.lower():
            return False
    
    return True

frase = str(input('Digite uma frase beeem longa e sem acentuação: '))

if(pangrama(frase) == True):
    print('A frase inserida é um pangrama!')
else:
    print('A frase inserida não é um pangrama!')

input()