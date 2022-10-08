import forca
import adivinhacao

def execute():
    print("\n(1) Forca\n(2) Adivinhação\n")

    e_numero = False
    while (not e_numero):
        qual = input("Qual jogo queres jogar? \nR: ")
        e_numero = qual.isnumeric()

        if (e_numero):
            qual = int(qual)
            print("\n" * 100)
        else:
            print("Erro, letra digitada! Digite o número referente ao jogo que deseja jogar.\n")
            continue


    if (qual == 1):
        forca.jogar()
    elif (qual == 2):
        adivinhacao.jogar()

if (__name__ == '__main__'):
    execute()