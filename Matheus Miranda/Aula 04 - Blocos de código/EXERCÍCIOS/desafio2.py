velocidade = int(input('Digite o valor do velocímetro em Km/h:'))
velocidadeMaxima = 80
multa = 7*(velocidade - velocidadeMaxima)

if velocidade > 80:
    print(f'Você foi multado! A multa vai custar R$ {multa}')
    
else:
    print('Você está dentro da velocidade permitida')
    