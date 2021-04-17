print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

#while(rodada <= total_de_tentativas):
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #String Interpolation
    chute = int(input("Digite o seu numero: "))

    print("Você digitou:", chute)

    if (numero_secreto == chute):
        print("Você acertou")
    else:
        if (chute > numero_secreto):
            print("Você errou, seu chute foi maior que o numero secreto")
        elif (chute < numero_secreto):
            print("Você errou, seu chute foi menor que o numero secreto")
    
    # rodada = rodada + 1

print("*********************************")
print("Fim do Jogo")
print("*********************************")