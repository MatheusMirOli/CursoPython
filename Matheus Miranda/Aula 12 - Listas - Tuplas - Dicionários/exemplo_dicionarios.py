meu_dicionario_cursos = {'python':'60h',
                        'java':'80h',
                        'javaScript':'60h'}

#exibir os itens do dicionário
print(meu_dicionario_cursos)
print(10 * "#")

#exibir elegantemente meu dicionário
for exibir in meu_dicionario_cursos.items():
    print(exibir)
print(10 * "#")

#exibir elegantemente apenas as chaves
for chaves in meu_dicionario_cursos:
    print(chaves)
print(10 * "#")

#exibir elegantemente apenas os valores
for valores in meu_dicionario_cursos.values():
    print(valores)
print(10 * "#")

#adicionar um elemento ao dicionário
meu_dicionario_cursos['Google Foundations'] = '40h'
meu_dicionario_cursos['Python Framework'] = '80h'
meu_dicionario_cursos['Python para Data Science'] = '60h'

#exibir qual a carga horária do curso de Google Foundations
#exibir qual a carga horária do curso de Excel

    #Minha forma:
k1 = input('Insira o curso desejado: ')
if k1 not in meu_dicionario_cursos.keys():
    print(f'O curso {k1} não está disponível no momento')
else:
    for k,v in meu_dicionario_cursos.items():
        if k1 in k:
            print(f'A carga horária do curso de {k} é igual a {v}')

    #Forma professor
# for cha,val in meu_dicionario_cursos.items():
#     #se o valor for Google Foundations, exibir a carga horária
#     # if cha == "Google Foundations":
#     #     print(f'A carga horária do curso de {cha} é igual a {val}')
#     if "Google Foun" in cha:
#         print(f'A carga horária do curso de {cha} é igual a {val}')

# if 'Excel' not in meu_dicionario_cursos.keys():
#     print(f'O curso de Excel não está disponível no momento')
# else:
#     for cha, val in meu_dicionario_cursos.items():
#         if "Exc" in cha:
#             print(f'A carga horária do curso de {cha} é igual a {val}')
    
        
        

