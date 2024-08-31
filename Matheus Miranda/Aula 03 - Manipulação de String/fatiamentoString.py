texto = "Curso de Python"

setimaPosicaoTexto = texto[6]
print(setimaPosicaoTexto)

textoCurso = texto[:5]
print(textoCurso)

textoPython = texto[9:]
print(textoPython)

#Contar o número de Caracteres dentro do texto (len)
qtdChar = len(texto)
print(f"Na frase temos {qtdChar} caracteres")

#Contar um numero específico de letras dentro do texto (count)
letra1 = input("Insira a letra desejada:")
letra2 = "o"
qtdLetrasUsuario = texto.count(letra1)
qtdLetrasO = texto.count(letra2)
print(f"Na frase temos {qtdLetrasUsuario} letras {letra1}")
print(f"Na frase temos {qtdLetrasO} letras {letra2}")

#Identificar a posição onde inicia uma palavra (find)
palavra = "Python"
posicaoPalavra = texto.find(palavra)
print(f"A palavra {palavra} inicia na posição {posicaoPalavra}")

#Identifica se existe a palavra no texto (in)
verificaPalavra = palavra in texto or "Sao Paulo" in texto
print(f"A palavra {palavra} está no texto? {verificaPalavra}")
