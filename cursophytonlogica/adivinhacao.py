import random

def jogar():
    print("************************")
    print("Bem vindo no jogo da Adivinhação")
    print("************************")

    numero_secreto = random.randrange(1, 101)
    print(numero_secreto)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade ?")
    print("(1) Facil (2)Médio (3)Difícil")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    rodada = 1

    for rodada in range(1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite um número entre 1 e 100 :")
        chute = int(chute)

        if(chute<1 or chute >100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        print("Você digitou", int(chute))

        if(acertou):
            print("Voce acertou e fez {}".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto")
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("************************")
    print("Fim do jogo")
    print("************************")

if (__name__) == ("__main__"):
    jogar()


