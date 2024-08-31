#1
numero1 = int(input('Digite um número inteiro:'))
quadrado = numero1 ** 2
print(f'{numero1} ao quadrado é igual a: {quadrado}')

#2
caractere1 = input('Digite seu nome:')
caractere2 = input('Digite seu último sobrenome:')
print(f'O usuário se chama {caractere1} {caractere2}')

#3
numero2 = int(input('Digite um numero inteiro:'))
sucessor = numero2 + 1
antecessor = numero2 - 1
print(f'O sucessor de {numero2} é igual a {sucessor} e seu antecessor é igual a {antecessor}')

#4
base = float(input('Digite a medida da Base do retângulo:'))
altura = float(input('Digite a medida da Altura do retângulo:'))
perimetro = (base*2) + (altura*2)
area = base * altura
print(f'Em um retângulo com base igual a {base} cm e altura igual a {altura} cm , temos um Perímetro igual a {perimetro} cm e uma Área igual a {area} cm^2')

#5
valorPrestacao = float(input('Digite o valor da prestação:'))
taxa = float(input('Digite o valor da taxa de juros anual em porcentagem:'))
tempo = int(input("Digite os dias de atraso:"))
prestacaoAtraso = valorPrestacao + (valorPrestacao * ((taxa/100)/365) * tempo)
print(f'O valor da prestação em atraso é de R$ {prestacaoAtraso}')
