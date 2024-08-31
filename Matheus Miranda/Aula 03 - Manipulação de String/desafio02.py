#DESAFIO 02
cidade = input('Insira o nome da sua cidade:')
palavra = 'Santo'
splitCidade = cidade.split()[0]
verificaCidade = palavra in splitCidade
print(f'A cidade {cidade} começa com a palavra {palavra}: {verificaCidade}')
