def area(dimensao1, dimensao2):
    return dimensao1*dimensao2

largura = float(input('Digite a largura do terreno em metros:\n'))

comprimento = float(input('Digite o comprimento do terreno em metros:\n'))

area_calculada = area(largura, comprimento)

print(f'A área do terreno é de: {area_calculada} m²')