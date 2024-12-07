cont = 0
algarismo = 1
numeros = []

while True:
    numero = int(input(f'Digite o {algarismo + cont}º número:\n'))
    if numero % 2 == 0:
        numeros.append(numero)
    cont += 1
    if cont == 6:
        break
    
soma = sum(numeros)
print(f'A soma entre os 6 números, se pares, é igual a: {soma}')