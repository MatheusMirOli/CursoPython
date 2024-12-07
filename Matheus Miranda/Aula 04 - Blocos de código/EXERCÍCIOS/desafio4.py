numero1 = input("Insira o primeiro número:")
numero2 = input("Insira o segundo número:")
numero3 = input("Insira o terceiro número:")

if numero1 > (numero2 and numero3):
    print(f'O número {numero1} é o maior')
elif numero2 > (numero1 and numero3):
    print(f'O número {numero2} é o maior')
elif numero3 > (numero1 and numero2):
    print(f'O número {numero3} é o maior')

if numero1 < (numero2 and numero3):
    print(f'O número {numero1} é o menor')
elif numero2 < (numero1 and numero3):
    print(f'O número {numero2} é o menor')
elif numero3 < (numero1 and numero2):
    print(f'O número {numero3} é o menor')
if numero1 == numero2 == numero3:
    print('Os números inseridos são iguais')
else:
    print('Operação Finalizada')
            


