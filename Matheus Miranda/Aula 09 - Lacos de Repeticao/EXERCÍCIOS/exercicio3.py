nome= input('Digite seu nome: \n')
nome_limpo = nome.lower().replace(" ","")
nome_invertido = ""
contador = len(nome_limpo) - 1
while contador >= 0:
    nome_invertido += nome_limpo[contador]
    contador -= 1
    if len(nome_invertido) == len(nome_limpo):
        print(nome_invertido.capitalize())
        break
    