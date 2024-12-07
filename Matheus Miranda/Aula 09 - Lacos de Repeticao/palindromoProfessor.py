#Capturar uma string do usuario
nome = input('Digite um nome para vê-lo ao contrário:\n')
#Exibir o tamanho do nome
#print(len(nome))
#Exibir somente a letra S
#print((nome[4]))

#Exibindo 1
nome_invertido = nome[::-1]
print(nome_invertido.capitalize())

#Exibindo 2
nome_invertido2 = ''.join(reversed(nome))
print(nome_invertido2.capitalize())

#Exibindo 3 - Inversão na raça
cont = 1
while True:
    if cont == len(nome) + 1:
        break
    print(nome[len(nome)-cont])
    cont = cont + 1

