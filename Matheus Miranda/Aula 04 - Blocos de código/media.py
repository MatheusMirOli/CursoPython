n1 = float(input("Digite a nota da primeira prova:"))
n2 = float(input("Digite a nota da segunda prova:"))
media = (n1+n2)/2
mediaCorte = 7

if media >= mediaCorte:
    print("Pegou o certificado do SENAI")
else:
    fMedia = (mediaCorte-media)
    print(f"Reprovado! Faltou {fMedia} pontos para pegar o certificado do SENAI")

print("Operação Finalizada")