contador = 0
algarismo = 1
numeros = []
while True:
    numero = float(input(f"Digite o {algarismo + contador}º número: \n"))
    numeros.append(numero)
    contador += 1
    if contador ==5:
        break
       
print(f'O maior valor digitado foi {max(numeros)} e o menor foi {min(numeros)} nas posiões {numeros.index(max(numeros))} e {numeros.index(min(numeros))} respectivamente')

