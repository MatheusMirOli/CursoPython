#criando dicionario vazio:
aluno_situacao = {}

#imputando os dados de um aluno:
aluno = str(input('Digite o nome do aluno:\n'))
nota = float(input('Digite a média do aluno:\n'))

#imputando os dados de vários alunos:
# cont = 0
# algarismo = 1
# numeros = []

# while True:
#     aluno = str(input(f'Digite o nome {algarismo + cont}º aluno\n(Digite SAIR para parar): '))
#     nota = float(input(f'Digite a {algarismo + cont}ª média:\n'))
#     aluno_situacao[aluno] = nota
#     cont += 1
#     if cont == 4:
#         break  

#declarando a condição para aprovado ou reprovado:
if nota >=6:
    situacao = "APROVADO"
elif nota <6:
    situacao = "REPROVADO"
    
#adiconando dados no dicionario:
aluno_situacao[aluno] = [situacao,nota]

for al,val in aluno_situacao.items():
    for sit,nta in aluno_situacao.values():
        print(f'O aluno {al} fechou com média {nta}, por isto sua situação é {sit}')
    
print(aluno_situacao)
    
