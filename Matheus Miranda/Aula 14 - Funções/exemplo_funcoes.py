#Criando uma função simples
# def exibir_nome_programador():
#     nome = str(input("Digite o nome do programador:\n"))
#     print(f'O nome do programador é {nome}')

# #Função com retorno
# def exibir_nome_filme():
#     nome_filme = input("Digite o nome do Filme:\n")
#     return nome_filme


# exibir_nome_programador()
# print(f'O nome do Filme é {exibir_nome_filme()}')

#Criar uma função que retorne a soma de dois números digitados pelo usuário.

# def exibir_soma():
#     numero1 = float(input('Digite o 1º número:\n'))
#     numero2 = float(input('Digite o 2º número:\n'))
#     soma = numero1 + numero2
#     return soma
  
# print(f'A soma é igual a {exibir_soma()}')
    
#Função recebendo parametro
def multiplicar_dois_numeros(numero1, numero2):
    return numero1*numero2

quantidade = int(input('Digite a quantidade de produtos:\n'))

valor = float(input('Digite o valor do produto:\n'))

total_compra = multiplicar_dois_numeros(quantidade, valor)

print(f'O valor da compra é: R${total_compra}')
