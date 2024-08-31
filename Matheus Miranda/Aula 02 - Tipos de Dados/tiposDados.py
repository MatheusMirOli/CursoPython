#Operador Soma (+)
numero1 = 5
numero2 = 5
soma = numero1 + numero2
print('A soma é igual a' , soma)
print('A soma é igual a ' + str(soma))
print(f'A soma é igual a {soma}')

#Operador Subtração (-)
numeroSub1 = 10
numeroSub2 = 5
subtracao = numeroSub1 - numeroSub2
print('A subtração é igual a' , subtracao)
print('A subtração é igual a ' + str(subtracao))
print(f'A subtração é igual a {subtracao}')

#Operador Multiplicação (*)
numeroMult1 = int(input('Digite um valor entre 0 e 10:'))
numeroMult2 = int(input('Digite um valor entre 0 e 10:'))
multiplicacao = numeroMult1 * numeroMult2
print('A multiplicação é igual a' , multiplicacao)
print('A multiplicação é igual a ' + str(multiplicacao))
print(f'A multiplicação é igual a {multiplicacao}')

#Operador Divisão (/)
numeroDiv1 = int(input('Digite um valor entre 0 e 10:'))
numeroDiv2 = int(input('Digite um valor entre 0 e 10:'))
divisao = numeroDiv1 / numeroDiv2
print('A divisão é igual a' , divisao)
print('A divisão é igual a ' + str(divisao))
print(f'A divisão é igual a {divisao}')

#Void Volume 
diameter = float(input('Digite o valor do diâmetro da Coluna:' ))
lenght = int(input('Digite o valor do comprimento da Coluna:' ))
volumeInjection = float(input('Digite o valor do volume de injeção:'))
voidvolume = ((((diameter/2)**2) * lenght * 3.14) / (volumeInjection*2000))
print(f'O volume morto da coluna cromatogrática é igual a {voidvolume:.2f}')

#Operador Modulo (%)
numeroMod1 = 5
numeroMod2 = 2
modulo = numeroMod1 % numeroMod2
print(f'O resto da divisão é igual a {modulo}')

#Operador Potencia (**)
numeroBase = 5
numeroExpoente = 2
potencia = numeroBase ** numeroExpoente
print(f'A potencia é igual a {potencia}')

#Operador Divisão Inteira (//)
numeroDivInt1 = 5
numeroDivInt2 = 2
divisaoInt = numeroDiv1 // numeroDiv2
print(f'A divisão inteira é igual a {divisaoInt}')