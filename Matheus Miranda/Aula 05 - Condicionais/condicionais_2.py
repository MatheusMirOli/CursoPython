#Verificar se o usuário paga ou não passagem de busão
#Não pagam passagem pessoas menores de 6 anos e e a partir de 65 anos

idade_usuario = int(input('Insira sua idade: '))

if idade_usuario < 6 or idade_usuario >= 65:
    print('O usuário não paga passagem')
else:
    print('O usuário paga passagem')