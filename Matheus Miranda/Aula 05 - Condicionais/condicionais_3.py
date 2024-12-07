usuario = str(input('Insira o nome do usário: '))
usuario_correto = 'Adm'
email_recuperacao = 'adm@senai.com.br'
senha_correta = 1234

if usuario == usuario_correto:
    senha = int(input('Insira a senha: '))
    if senha == senha_correta:
        print('Acesso ao sistema')
    else:
        print('Senha incorreta. Acesso negado')
        resposta = str(input('Deseja redifinir a senha: ')).capitalize()
        if resposta == "Sim":
            email = str(input('Insira o e-mail de recuperação: '))
            if email == email_recuperacao:
                 print('Uma nova senha foi enviada para seu e-mail')
                 print('Operação finalizada')
            else:
                print('O e-mail de recuperação inserido está incorreto')
        else:
            print('Operação finalizada')
else:
    print('Usuário incorreto')
    
    
