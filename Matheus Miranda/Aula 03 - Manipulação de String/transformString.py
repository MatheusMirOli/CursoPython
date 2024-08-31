#Trocando uma palavra dentro de um texto
texto = 'Matheus Miranda'
trocaPalavra = texto.replace('Miranda','Oliveira')
print(trocaPalavra)

#Deixando todos os caracteres em maiúsculo
texto = 'MatHeus.mIraNda@yAhoo.Com.Br'
textoMaiusculo = texto.upper()
print(textoMaiusculo)

#Deixando todos os caracteres em minúsculo
textoMinusculo = texto.lower()
print(textoMinusculo)

#Deixando a primeira letra de cada palavra em Maiúsculo
texto = 'matheus miranda de oliveira'
textoTitulo = texto.title()
print(textoTitulo)

#Deixando apenas a primeira letra da frase em Maiúsculo
texto = 'matheus miranda de oliveira'
textoPrimeiraLetra = texto.capitalize()
print(textoPrimeiraLetra)

#Elimina Espaçoes inúteis
texto = '                    SENAI             '
print(f'A palavra {texto} tem {len(texto)} caracteres')

textoStrip = texto.strip()
print(f'A palavra {textoStrip} tem {len(textoStrip)} caracteres')