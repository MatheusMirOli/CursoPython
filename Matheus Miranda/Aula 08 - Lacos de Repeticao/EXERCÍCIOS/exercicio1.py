import time
contador = 10
while True:
    print(contador)
    contador-=1
    time.sleep(1)
    if contador==0:
        break