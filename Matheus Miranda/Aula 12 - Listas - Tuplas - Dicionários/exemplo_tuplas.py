lanches_tupla = ('mistão','beirute','bauru','coxinha')

#exibindo uma tupla
print(lanches_tupla)

#exibir elegantemente
for lan in lanches_tupla:
    print(lan)
    
print(10 * '#')

#converter uma tupla em lista
lanches_lista = list(lanches_tupla)
for li in lanches_lista:
    print(li)
print(10 * '#')
#adicionar um item a lista convertida
lanches_lista.append('dogão')
for li in lanches_lista:
    print(li)
print(10 * '#')
#converter uma lista em tupla
novo_lanches = tuple(lanches_lista)
for novo_la in novo_lanches:
    print(novo_la)
print(10 * '#')
