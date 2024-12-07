distancia = int(input('Digite a distância da viagem em Km:'))
valor200 = distancia * 0.50
valorLongas = distancia * 0.45

if distancia <= 200:
    print(f'A passagem irá custar R$ {valor200}')
else:
    print(f'A passagem irá custar R$ {valorLongas}')