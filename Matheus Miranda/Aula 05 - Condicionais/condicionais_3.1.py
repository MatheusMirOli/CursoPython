usuario = str(input('Insira o nome do usário: '))
usuario_correto = 'Administrador'
senha_correta = 1234

if usuario == usuario_correto:
    senha = int(input('Insira a senha: '))
    if senha == senha_correta:
        print('Acesso ao sistema')
    else:
        print('Acesso negado')
else:
    print('Usuário incorreto')
    
    
