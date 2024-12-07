lista_carros = ['Fusca','Kombi','Chevete','Parati']

#adicionar mais um veículo
lista_carros.append('Belina')

#exibir a lista
print(lista_carros)

#exibir a lista elegantemente
for exibir in lista_carros:
    print(exibir)
    
#remover um item da lista
lista_carros.remove("Fusca")

for exibir in lista_carros:
    print(exibir)
    
#exibir a lista ordenadamente
lista_carros.sort()
print(lista_carros)