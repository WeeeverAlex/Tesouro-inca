from functions import *
import sys
import time
from random import *
#from colorama import init, Fore, Style
#init()

#variaveis
jogadores = 0



#Funcao pega no projeto deep sea adventure, para colocar slow entre os prints
def print_slow(str): 
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02) 

quantos_jogadores = int(input('Quantos jogadores? '))
jogadores = quantos_jogadores
print_slow('Ok, vamos começar com ' + str(jogadores) + ' jogadores')
print()
continuar_ou_nao()
#Perigo ou Tesouro
print()
print()
perigo_ou_tesouro = tesouro_ou_perigo()
print()

if perigo_ou_tesouro == tesouro:
    valor_do_tesouro = valor_tesouro()
    print_slow(f'O valor do tesouro é {valor_do_tesouro}')
    divindo = dividir_tesouro(quantos_jogadores)
    print_slow(f'Os jogadores dividiram o tesouro e cada um ficou com {divindo}')
    print()


    
