from random import *
from re import A 
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
        tesouro = print('Enquanto o grupo estava na caverna descobriram um tesouro')
        return tesouro
    else:
        perigo = print('Enquanto o grupo estava na caverna encontraram um perigo')
        return perigo

#Função: valor do tesouro
def valor_tesouro():
    valor = randint(1,15)
    print(valor)
    return valor


#Função: dividir tesouro entre jogadores
#Este valor deve ser dividido igualmente entre os jogadores 
# Se não for possível dividir igualmente, os tesouros que sobrarem devem ficar no caminho.

def dividir_tesouro(jogadores):
    tesouro = valor_tesouro()
    tesouro_sobrou = 0
    if tesouro % jogadores == 0:
        tesouro = tesouro / jogadores
        return tesouro
    else:
        if tesouro % jogadores != 0:
            tesouro_sobrou = tesouro % jogadores
            tesouro = tesouro // jogadores
            return tesouro, tesouro_sobrou


    

#Função: perigo
#se cair perigo a primeira vez acontece nada
#se cair perigo a segunda vez, jogadores perdem todos os tesouros

def perigo(jogadores):
    perigo = tesouro_ou_perigo()
    if perigo == 'perigo':
        perigo = tesouro_ou_perigo()
        if perigo == 'perigo':
            jogadores = 0
            return jogadores
        else:
            return jogadores
    else:
        return jogadores

#Função: decidir explorar ou nao
def explorar_ou_nao():
    explorar = input('Deseja ir explorar a caverna?(s/n) ').upper()
    if explorar == 'S':
        return print('Você foi para a caverna explorar...')
    else:
        return print('Você não explorou, e ficou no acampamento')

#Função: decidir se quer continuar ou não
def continuar_ou_nao():
    continuar = input('Deseja continuar explorando a caverna?(s/n) ').upper()
    if continuar == 'S':
        return print('Continuando a explorar...')
    else:
        return print('Você não continuou e voltou para o acampamento')

            