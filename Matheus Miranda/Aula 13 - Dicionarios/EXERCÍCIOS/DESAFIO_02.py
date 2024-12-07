#criando um dicionario vazio:
jogardor_numero = {}

#imputando os dados dos jogadores e gerando valores dos dados randomicamente:
cont = 0
algarismo = 1
numeros = []
import random
while True:
    jogador = str(input(f'Digite o nome do {algarismo + cont}º jogador:\n'))
    numero = random.randint(1,6)
    #adicionando os valores no dicionario:
    jogardor_numero[jogador] = numero
    cont += 1
    if cont == 4:
        break  

# Ordenando o dicionário por valor em ordem decrescente
jogadores_ordenados = sorted(jogardor_numero.items(), key=lambda x: x[1], reverse=True)

# Imprimindo os jogadores ordenados
for jogador, numero in jogadores_ordenados:
    print(f"{jogador} tirou {numero} no dado")

# O primeiro jogador da lista ordenada é o ganhador
ganhador = jogadores_ordenados[0][0]
print(f"\nO ganhador é {ganhador} com o número {jogadores_ordenados[0][1]}!")