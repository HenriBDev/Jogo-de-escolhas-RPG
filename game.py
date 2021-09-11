from random import randrange
import os

os.system('CLS')


def main():
    CAMINHO_VERMELHO = 1
    CAMINHO_PRETO = 2
    tentativas = 7
    sala = 1

    while (tentativas > 0 and sala != 9):

        mostraVida(tentativas)
        visualSalaPrincipal(sala)

        escolha = int(input())

        if ((escolha == CAMINHO_VERMELHO and sala != 6) or (escolha == CAMINHO_PRETO and sala != 8)):
            sala += escolha
            os.system('CLS')
        elif sala == 8:
            sala = randrange(1, 6)
            os.system('CLS')
        else:
            os.system('CLS')
            mensagemFuga()
        tentativas -= 1

    if(tentativas == 0 and sala != 9):
        mensagemDerrota()
    else:
        mensagemVitoria(sala)


def mostraVida(vidas):
    cont = vidas
    while(cont > 0):
        print("<3 ", end="")
        cont -= 1


def visualSalaPrincipal(sala):
    print("\n\n===================================================")
    print("====== Bravo guerreiro, você está na {}° sala ======".format(sala))
    print("=== Escolha seu caminho, ou lamente eternamente ===")
    print("==== [1]-Caminho Vermelho == [2]-Caminho Preto ====")
    print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@                                               @@")
    print("@@      __________             ____________      @@")
    print("@@     /     _    \           /    ____    \     @@")
    print("@@    /     / \    |         /    /_   \   /     @@")
    print("@@    |     | |    \         |     /   /   |     @@")
    print("@@    |     | |     |        |    /   /_   |     @@")
    print("@@    |     \_/     |        |    \____/   /     @@")
    print("@@    /_____________|        |_____________|     @@")
    print("@@    \              \      /             /      @@")
    print("@@     \              \    /             /       @@")
    print("@@      \              \  /             /        @@")
    print("@@       \              \/             /         @@")
    print("@@                                               @@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n")

    pass


def visualSala6():  # ?

    print("\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@                                               @@")
    print("@@                 \____________/                @@")
    print("@@                  |          |                 @@")
    print("@@                  |   ____   |                 @@")
    print("@@                  |  /_   \  |                 @@")
    print("@@                  |   /   /  |                 @@")
    print("@@                  |  /   /_  |                 @@")
    print("@@                  |  \____/  |                 @@")
    print("@@                  |          |                 @@")
    print("@@                  |__________|                 @@")
    print("@@                  /          \                 @@")
    print("@@                 /            \                @@")
    print("@@                /              \               @@")
    print("@@               /                \              @@")
    print("@@              /                  \             @@")
    print("@@                                               @@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n")


def mensagemVitoria(sala):
    print("========================================================")
    print("==== Parabéns, bravo guerreiro! Você está na sala: {} ===".format(sala))
    print("==== Leve este troféu e lembre-se de sua conquista =====\n")
    print("@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@")
    print("@@   ____________   @@")
    print("@@  '._==_==_==_.'  @@")
    print("@@  .-\:       /-.  @@")
    print("@@  | (|:.     |) | @@")
    print("@@   '-|:.     |-'  @@")
    print("@@     \::.    /    @@")
    print("@@      '::. .'     @@")
    print("@@        ) (       @@")
    print("@@      _.' '._     @@")
    print("@@     '-------'    @@")
    print("@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@\n")


def mensagemDerrota():
    os.system('CLS')
    print("========================================================")
    print("== Apesar de seus esforços, suas chances se esgotaram ==")
    print("==== Tudo escurece!! Sua respiração pesa!! É O FIM!! ===\n")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@       _______________      @@")
    print("@@      /               \     @@")
    print("@@     /                 \    @@")
    print("@@  /\/                   \/\ @@")
    print("@@  \ |   XXXX     XXXX   | / @@")
    print("@@   \|   XXXX     XXXX   |/  @@")
    print("@@    |   XXX       XXX   |   @@")
    print("@@    |                   |   @@")
    print("@@    \__      XXX      __/   @@")
    print("@@      |\     XXX     /|     @@")
    print("@@      | |           | |     @@")
    print("@@      | I I I I I I I |     @@")
    print("@@      |  I I I I I I  |     @@")
    print("@@      \_             _/     @@")
    print("@@        \_         _/       @@")
    print("@@          \_______/         @@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")


def mensagemFuga():
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("!!!!!!!! VOCÊ ESTÁ TENTANDO FUGIR DE MIM?? !!!!!!!!")
    print("!!!!!! CONTINUE TENTANDO E NUNCA SAIRÁ DAQUI. !!!!!")
    print("!!!!!!! UMA VIDA SERÁ LEVADA COMO LEMBRETE. !!!!!!!")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")


if __name__ == "__main__":
    main()
