def classificacao_consumo(autonomia):
    
    if autonomia < 2:
        return "Consumo elevado"
    elif 2 <= autonomia <= 7:
        return "Consumo moderado"
    elif autonomia > 7:
        return "Consumo reduzido"
    
altura = float(input('Insira a Altura do reservatório em centímetros: '))
largura = float(input('Insira a Largura do reservatório em centímetros: '))
comprimento = float(input('Insira o Comprimento do reservatório em centímetros: '))
consumo_medio = float(input('Insira o consumo médio de Litros de água por dia: '))
capacidade_total = (altura * largura * comprimento)/1000
autonomia_dias = capacidade_total / consumo_medio
classificacao = classificacao_consumo(autonomia_dias)

print(f'A capacidade total do reservatório é de {capacidade_total} Litros')
print(f'A autonomia do reservatório é de {autonomia_dias} dias')
print(f'A classificação de consumo sem enquadra em: {classificacao}')


    
