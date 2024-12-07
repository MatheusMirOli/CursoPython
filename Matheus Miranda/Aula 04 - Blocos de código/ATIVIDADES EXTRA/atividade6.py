time1 = str(input("Insira o nome do time 1: "))
time2 = str(input("Insira o nome do time 2: "))
gols_time1 = int(input(f"Insira a quantiade de gols marcadas pelo {time1}: "))
gols_time2 = int(input(f"Insira a quantiade de gols marcadas pelo {time2}: "))

if gols_time1 == gols_time2:
    print('Resultado: Empate!')
else:
    if gols_time1 > gols_time2:
        print(f'Vitória do {time1}')
    else:
        if gols_time2 > gols_time1:
            print(f'Vitória do {time2}')
        else:
            print('Operação finalizada')