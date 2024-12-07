#Pedir um número inteiro para o usuário
number = int(input("Insert a number:"))

#Cálculo para definir par ou ímpar
modulo = number % 2

#Verificação se o número é par ou ímpar
if modulo == 0:
    print("The number entered is even")

else:
    print("The number entered is odd")

print("Operation completed")
