from random import randrange
import os

os.system('CLS')
tentativas = 0
sala = 1
CAMINHO_VERMELHO = 1
CAMINHO_PRETO = 2

while (tentativas < 7 and sala != 9):
    tentativas += 1
    print("Você está na sala: {}\nEscolha seu caminho".format(sala))
    print("[1] - Caminho Vermelho\n[2] - Caminho Preto")

    escolha = int(input())

    if ((escolha == CAMINHO_VERMELHO and sala != 6) or (escolha == CAMINHO_PRETO and sala != 8)):
        sala += escolha
        os.system('CLS')
    elif sala == 8:
        sala = randrange(1, 5)
        os.system('CLS')
    else:
        print("\nNão existe esse caminho!\n\n")


if tentativas >= 7:
    print("Você gastou todos seus recursos, não há mais saidas, você e seus companheiros morreram")
else:
    print("Você está na sala: {}\nVocê venceu!!".format(sala))