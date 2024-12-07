numero1 = input("Insira o primeiro número:")
numero2 = input("Insira o segundo número:")
menorNumero = min(numero1 , numero2)
maiorNumero = max(numero1 , numero2)

if numero1 == numero2:
    print(f"Os números inseridos são iguais")
else:
    print(f'O menor número é {menorNumero} e o maior é {maiorNumero}')