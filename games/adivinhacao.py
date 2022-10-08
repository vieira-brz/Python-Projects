import random

def jogar():
    print("#####################################")
    print("# Bem vindo ao jogo de Adivinhação! #")
    print("#####################################")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 100

    print("Qual o nível de dificuldade?")
    print("(1) - Fácil\n(2) - Médio\n(3) - Difícil")
    nivel = input("\nNível: ")
    nivel = int(nivel)

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5


    for rodada in range(1, tentativas + 1):

        print("\nTentativa {} de {}".format(rodada, tentativas))

        chute = input("Digite um número entre 1 e 100: ")
        chute = int(chute)

        if (chute < 1 or chute > 100):
            print("Número inválido!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("\n> Parabéns, você acertou!\n> Pontuação {}".format(pontos))
            break
        else:
            if (maior):
                print("Você errou, o seu chute foi maior do que o número secreto!")
            elif(menor):
                print("Você errou, o seu chute foi menor do que o número secreto!")
            else:
                print("Erro!")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos_perdidos

            if (rodada == tentativas):
                print("\n> Número secreto: {}\n> Pontuação {}".format(numero_secreto, pontos))

    print("\n################")
    print("# Fim de Jogo! #")
    print("################\n")

if (__name__ == "__main__"):
    jogar()