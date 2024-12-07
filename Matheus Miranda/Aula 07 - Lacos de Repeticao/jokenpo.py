import random
pontosJogador = 0
pontosMaquina = 0

while True:
    resposta = input("Deseja jogar JOkênpo? S/N \n")
    if resposta.upper() =="N":
        break
    else:
        opcaoJogador = int(input("escolha uma das opções: \n "+
                      "1 - para Pedra \n " + 
                      "2 - para Papel \n " + 
                      "3 - para Tesoura \n"))
        opcaoMaquina = random.randint(1,3) 
        if opcaoJogador == 1:
            if opcaoMaquina ==1:
                print("Você esolheu Pedra \n A máquina também escolhe Pedra\n")
                print("Resultado empate")
            elif opcaoMaquina ==2:
                print("Você esolheu Pedra \n A máquina escolheu Papel\n")
                print("Vitoria da Máquina")
                pontosMaquina+=1               
            else:
                print("Você esolheu Pedra \n A máquina escolheu Tesoura\n")
                print("Você venceu")
                pontosJogador+=1 
        elif opcaoJogador == 2:
            if opcaoMaquina ==1:
                print("Você esolheu Papel \n A máquina escolheu Pedra\n")
                print("Resultado empate")
            elif opcaoMaquina ==2:
                print("Você esolheu Papel \n A máquina também escolheu Papel\n")
                print("Vitoria da Máquina")
                pontosMaquina+=1               
            else:
                print("Você esolheu Papel \n A máquina também escolhe Tesoura\n")
                print("Você venceu")
                pontosJogador+=1
        elif opcaoJogador ==3:
            if opcaoMaquina ==1:
                print(f"")
            elif opcaoMaquina ==2:
                print(f"")
            else:
                print(f"")
        else:
            print("Opção inválida !!!")
                
            
        
    
