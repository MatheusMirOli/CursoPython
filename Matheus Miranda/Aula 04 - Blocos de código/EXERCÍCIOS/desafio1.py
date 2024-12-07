import random
numeroAleatorio = random.randint(0,5)
numero = int(input("Digite um número entre 0 e 5:"))

if numero == numeroAleatorio:
    print('PARABÉNS!! Você ganhou')
    
else:
    print('Infelizmente não foi dessa vez. Tente novamente.')

