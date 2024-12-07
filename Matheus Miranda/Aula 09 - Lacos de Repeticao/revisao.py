#Contagem regressiva de 10 a 0
#Utilizando for

for numero in range(10,-1,-1):
    print(numero)
    
#Contagem progressiva de 0 a 10
#Utilizando while de 1 em 1 segundo

import time
contador = 0
while True:
    print(contador)
    contador+=1
    time.sleep(1)
    if contador>10:
        break
    
import time
contador1 = 0
while contador1 <=10:
    print(contador1)
    contador1 = contador1 +1
    time.sleep(1)
    
