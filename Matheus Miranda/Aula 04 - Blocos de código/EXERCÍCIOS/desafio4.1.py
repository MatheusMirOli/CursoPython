numero1 = input("Insira o primeiro número:")
numero2 = input("Insira o segundo número:")
numero3 = input("Insira o terceiro número:")
menorNumero = min(numero1 , numero2 , numero3)
maiorNumero = max(numero1 , numero2 , numero3)

if numero1 == numero2 == numero3:
    print(f"Os números inseridos são iguais")
else:
    print(f'O menor número é {menorNumero} e o maior é {maiorNumero}')
