lista_matriz = []
lista_par = []
lista_impar = []
algarismo = 1
cont = 0
while True:
    numero = int(input(f'Digite o {algarismo + cont}º número a ser inserido na lista \n(Para encerrar, digite 0):\n'))
    if numero == 0:
        print('Código encerrado')
        break
    elif numero != 0 and numero not in lista_matriz:
        lista_matriz.append(numero)
    cont += 1
    if cont == 1000:
        break

for numero in lista_matriz:
    if numero % 2 == 0 and numero > 0:
        lista_par.append(numero)
    elif numero % 2 != 0 and numero > 0:
        lista_impar.append(numero)
        
lista_matriz.sort()
lista_par.sort()
lista_impar.sort()
total = sum(lista_matriz)

print(f'A lista matriz é igual a: {lista_matriz}')
print(f'A lista de números pares é igual a: {lista_par}')
print(f'A lista de números ímpares é igual a: {lista_impar}')
print(f'A soma de todos os números é igual a: {total}')
