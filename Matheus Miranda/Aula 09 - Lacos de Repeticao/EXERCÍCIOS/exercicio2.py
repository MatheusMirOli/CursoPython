contador = 0
algarismo = 1
idade_mulheres = []
idade_homens = []
while True:
    sexo = str(input(f"Digite o sexo da {algarismo + contador}ª pessoa: (M/F) \n")).upper()
    idade = int(input(f'Digite a idade da {algarismo + contador}ª pessoa:\n'))
    if sexo == "M":
        idade_homens.append(idade)
    elif sexo == "F":
        idade_mulheres.append(idade)
    else:
        print('Sexo inválido. Por favor, digite M ou F.')
        contador -= 1
    contador += 1
    if contador ==10:
        break

media_idade_mulheres = sum(idade_mulheres) / len(idade_mulheres)
media_idade_homens = sum(idade_homens) / len(idade_homens)
todas_as_idades = idade_mulheres + idade_homens
media_geral = sum(todas_as_idades) / len(todas_as_idades)

print(f'A média de idade das mulheres é igual a: {media_idade_mulheres}')
print(f'A média de idade dos homens é igual a: {media_idade_homens}')
print(f'A média geral de idades é igual a: {media_geral}')