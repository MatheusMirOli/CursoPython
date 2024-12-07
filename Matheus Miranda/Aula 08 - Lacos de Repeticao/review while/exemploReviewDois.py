#exibir os números ímpares entre 100 e 150
#resolução 1
cont = 100
while cont < 150 :
    if cont % 2 != 0:
        print(cont)
    cont += 1
#resolução 2
cont = 101
while True:
    print(cont)
    if cont >150:
        break
    cont = cont + 2

#resolução 3
cont = 101
while cont < 150:
    print (cont)
    cont = cont + 2

