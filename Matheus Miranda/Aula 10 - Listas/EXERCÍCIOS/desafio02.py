contador = 0
algarismo = 1
numeros = []
while True:
    numero = int(input(f"Digite o {algarismo + contador}º número: \n"))
    if numero in numeros:
        pass
    else:
        numeros.append(numero)
    contador += 1
    if contador ==10:
        break
numeros.sort()
print(f'Os números únicos digitados foram: {numeros}')
