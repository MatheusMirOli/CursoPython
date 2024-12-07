
ano_atual = int(input('Insira o ano atual: '))
ano_nascimento = int(input('Insira seu ano de nascimento: '))

if (ano_atual - ano_nascimento) >= 18:
            print('Você é maior de idade')
else:
    print('Você é menor de idade')