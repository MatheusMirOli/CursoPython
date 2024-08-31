nomeCompleto = "Matheus Miranda de Oliveira"

primeiroNome = nomeCompleto[0:7]
print(primeiroNome)

primeiroSobrenome = nomeCompleto[8:15]
print(primeiroSobrenome)

segundoSobrenome = nomeCompleto[-8:]
print(segundoSobrenome)

#Quantidade de caracteres
qtdChar = len(nomeCompleto)
print(f"No nome {nomeCompleto} há {qtdChar} caracteres")

#Quantidade de letras "a"
qtdLetra = nomeCompleto.count("a")
print(f"No nome {nomeCompleto} há {qtdLetra} letras 'a' ")

#Onde inicia seu último sobrenome
palavra = "Oliveira"
posicaoPalavra = nomeCompleto.find(palavra)
print(f"O sobrenome {palavra} inicia na posição {posicaoPalavra}")

#Verificar se o seu nome tem os seguintes sobrenomes: "Silva", "Souza" ou "Santos"
sobrenome1 = "Silva"
sobrenome2 = "Souza"
sobrenome3 = "Santos"
verificaPalavra = sobrenome1 in nomeCompleto or sobrenome2 in nomeCompleto or sobrenome3 in nomeCompleto
print(f"O nome {nomeCompleto} têm os sobrenomes {sobrenome1}, {sobrenome2} ou {sobrenome3}? {verificaPalavra}")