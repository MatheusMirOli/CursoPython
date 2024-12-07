produtos = {
    'arroz': 20,
    'feijao': 8,
    'oleo': 7,
    'macarrao': 4,
    'sabonete': 2,
    }

#exibir elegantemente minha lista de produtos
# for prod, preco in produtos.items():
    # print(f'O {prod} está R${preco},00')
    
#verificar se há 'molho de tomate' na lista
#se houver, exibir o preço, senão avisar que não tem o produto

# for prod,preco in produtos.items():
#     if 'molho de tomate' in prod:
#         print(f'O molho de tomate custa R${preco}')
#     else:
#         print('O produto selecionado não consta na lista')

#adicionando um novo produto ao dicionario:
produtos['molho de tomate'] = 2

item = str(input('Digite o produto:\n'))
if item in produtos:
    for prod, preco in produtos.items():
        if item in prod:
            print(f'O {item} custa R${preco}')
else:
    print('O produto selecionado não consta na lista')
