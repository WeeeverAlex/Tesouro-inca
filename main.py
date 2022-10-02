from functions import *
import sys
import time
from random import *
from colorama import init, Fore, Style
init()

#variaveis
jogadores = 0
jogo = True
tesouros_jogador1 = 0
tesouros_jogador2 = 0





#Funcao pega no projeto deep sea adventure, para colocar slow entre os prints
def print_slow(str): 
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02) 

while jogo:
    quantos_jogadores = int(input('Quantos jogadores? (1/2)  '))
    jogadores = quantos_jogadores
    if quantos_jogadores == 1:
        print_slow('Ok, vamos começar com ' + str(jogadores) + ' jogador')
        print()
        continuar_ou_nao_jogador1()
    elif quantos_jogadores == 2:
        print_slow('Ok, vamos começar com ' + str(jogadores) + ' jogadores')
        print()
        continuar_ou_nao_jogador2()
    else:
        print('Digite 1 ou 2 jogadores')
        print()
        continue


    break

    
