#exemplo de while - laços de repetição
#exibir o nome do programador 10 vezes
print("Exibindo o nome do programador 5 vezes")
contador = 1
while contador < 6:
    #print(contador)
    print("Ewerson")
    contador = contador + 1 
    #final loop

print(15*"#")
#exibir a tabuada do 7
print("Exibindo a tabuada do 7")
contadorDois = 1
while contadorDois <= 10:
    print(f"7 x {contadorDois} = {contadorDois* 7} ")
    #incremento
    contadorDois+=1
    #contadorDois = contadorDois + 1

print(15*"&")
#exibir a tabuado do 9
print("Exibindo a tabuada do 9")
contadorTres = 1
while contadorTres <=98600:
     print(f"9 x {contadorTres} = {contadorTres* 9} ")
     contadorTres +=1
     #criando condição de parada
     if contadorTres >= 11:
         break
     
print(15*"&")
#exibir a tabuado do 5
print("Exibindo a tabuada do 5")
#print(contador)
contador = 1   
while True:
    print(f"5 x {contador} = {contador*5}")
    contador+=1
    #inserindo condição de parada
    if contador == 11:
        break
    
    





