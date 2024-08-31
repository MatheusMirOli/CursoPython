#DESAFIO 04
frase = input('Insira uma frase:')
letra = 'A'
contagemLetra = frase.count(letra)
posicaoLetraInicial = frase.find(letra)
posicaoLetraFinal = frase.rfind(letra)
print(f'A frase {frase} contém {contagemLetra} letras {letra}')
print(f'A letra {letra} aparece a primeira vez na posição {posicaoLetraInicial}')
print(f'A letra {letra} aparece pela última vez na posição {posicaoLetraFinal}')
