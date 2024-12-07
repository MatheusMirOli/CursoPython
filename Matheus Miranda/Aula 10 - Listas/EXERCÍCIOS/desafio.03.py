contador = 0
algarismo = 1
numeros = []
while True:
    numero = int(input(f"Digite o {algarismo + contador}º número: \n"))
    posicao = 0
    while posicao < len(numeros) and numeros[posicao] < numero:
        posicao += 1 
    numeros.insert(posicao,numero)
    contador += 1
    if contador ==5:
        break
    
print(f'A Lista ordenada é:\n{numeros}')
    
