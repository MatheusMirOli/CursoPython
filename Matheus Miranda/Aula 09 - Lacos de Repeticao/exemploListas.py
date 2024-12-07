#Criação de uma lista vazia
lista = []
#Criação de uma lista de nomes
nomes = ["Marcos","Paulo","Marcia","Joana"]
#Exibindo uma lista
print(nomes)
#Exibir uma lista "Elegantemente"
for exibir_nomes in range(len(nomes)):
    print(nomes[exibir_nomes])
    
#Exibir apenas Paulo
    print(nomes[1])
    
#Exibir apenas Joana
    print(nomes[3])
    
#Adicionar um carro na lista vazia
lista.append('Fox')
print(lista)
#Adicionar um carro na lista vazia
lista.append('Fusca')
print(lista)
#Exibir uma lista "Elegantemente"
for exibir_lista in range(len(lista)):
    print(lista[exibir_lista])