cont = 0
numeros = []
while True:
    numero = cont
    if cont % 3 == 0 and cont % 2 != 0:
        numeros.append(numero)
    cont += 1
    if cont == 501:
        break
    
soma = sum(numeros)
print(f'A soma entre todos os números ímpares que são múltiplos de três, é igual a: {soma}')
    