valor_compra = float(input('Insira o valor da compra: '))
qtd_parcelas = int(input('Insira a quantidade de prestações: '))
valor_parcelas = (valor_compra/qtd_parcelas)

print(f'Você terá {qtd_parcelas} prestações no valor de R${valor_parcelas} sem juros')