from random import *
import sys
import time


#Funcao pega no projeto deep sea adventure, para colocar slow entre os prints
def print_slow(str): 
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)  

#Função: sorteio tesouros ou perigo
def tesouro_ou_perigo():
    sorteio = randint(1,2)
    if sorteio == 1:
        print('Enquanto o grupo estava na caverna descobriram um tesouro')
        return 1
    elif sorteio == 2:
        print('Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras.')
        return 2
    

#Função: valor do tesouro
def valor_tesouro():
    valor = randint(1,15)
    return valor


#Função: dividir tesouro entre jogadores
#Este valor deve ser dividido igualmente entre os jogadores 
# Se não for possível dividir igualmente, os tesouros que sobrarem devem ficar no caminho.

def dividir_tesouro(jogadores, tesouros):
    if tesouros %  jogadores == 0:
        tesouros = tesouros // jogadores
        return tesouros

    else:
        if tesouros % jogadores != 0:
            tesouros = tesouros // jogadores
            return tesouros

