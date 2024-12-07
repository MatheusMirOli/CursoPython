
lista_dicionarios = []
dicionario = {}

#imputando os dados das pessoas em cada dicionário:
cont = 0
algarismo = 1
while True:
    dicionario['nome'] = str(input(f'Digite o nome da {algarismo + cont}ª pessoa:\n'))
    dicionario['sexo'] = str(input(f'Digite o sexo da {algarismo + cont}ª pessoa (FEM/MASC):\n'))
    dicionario['idade'] = int(input(f'Digite a idade da {algarismo + cont}ª pessoa:\n'))
    #adicionando os valores no dicionario:
    lista_dicionarios.append(dicionario.copy())
    cont += 1
    if cont == 2:
        break  

#Quantidade de pessoas cadastradas:
print(f'Foram cadastradas {len(lista_dicionarios)} pessoas')

#Média de idade do grupo:
soma_idades = 0
for pessoa in lista_dicionarios:
    soma_idades += pessoa['idade']
media_idade = soma_idades / len(lista_dicionarios)

print(f'A média de idade do grupo é: {media_idade}')

#Uma lista com todas as mulheres:
mulheres = [pessoa for pessoa in lista_dicionarios if pessoa['sexo'] == 'FEM']
print("Mulheres cadastradas:")
for mulher in mulheres:
    print(mulher['nome'])
    
#Uma lista com todas as pessoas com idade acima da média:
# pessoas_acima = []
acima_da_media = [pessoa for pessoa in lista_dicionarios if pessoa['idade'] > media_idade]
print("Pessoas com idade acima da média:")
for pessoa in acima_da_media:
    print(pessoa['nome'])
    # pessoas_acima.append(pessoa['nome'])
    # print(pessoas_acima)
