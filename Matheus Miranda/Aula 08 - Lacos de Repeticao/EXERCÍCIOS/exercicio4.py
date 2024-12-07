numero = int(input("Digite um número para calcular sua taboada: \n"))
print(f"Exibindo a tabuada do {numero}")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")