contador = 0
algarismo = 1
numeros = []
while True:
    numero = int(input(f"Digite o {algarismo + contador}º algarismo: \n"))
    numeros.append(numero)
    contador += 1
    if contador ==10:
        break
    
menor = min(numeros)
maior = max(numeros)
media = sum(numeros) / len(numeros)

print(f'O menor algarismo digitado é igual a: {menor}')
print(f'O maior algarismo digitado é igual a: {maior}')
print(f'A média dos algarismos digitados é igual a: {media}')