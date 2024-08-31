#DESAFIO 05
nome = input('Insira seu nome completo: ')
splitNome = nome.split()
print(f'Primeiro nome: {splitNome[0]}')
print(f'Último nome: {splitNome[-1]}')
print(f'Nome resumido: {splitNome[0]} {splitNome[-1]}')
