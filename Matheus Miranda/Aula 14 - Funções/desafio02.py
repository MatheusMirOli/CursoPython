def maior(numero1, numero2, numero3):
    return max(numero1,numero2,numero3)

n1 = float(input('Digite o primeiro número:\n'))
n2 = float(input('Digite o segundo número:\n'))
n3 = float(input('Digite o terceiro número:\n'))

maior_numero = maior(n1,n2,n3)

print(f'O maior número digitado foi o {maior_numero}')