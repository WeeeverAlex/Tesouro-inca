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
        return 'Enquanto o grupo estava na caverna descobriram um tesouro'
    elif sorteio == 2:
        return 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.'
    else:
        pass

#Função: Perigo a segunda vez
def perigo_segunda_vez():
    perigo = tesouro_ou_perigo()
    if perigo == 'perigo':
        perigo = tesouro_ou_perigo()
        if perigo == 'perigo':
            return print('Você foi preso na caverna')
        else:
            pass
    


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
def continuar_ou_nao_jogador1():
    while True:
        continuar = input('Jogador 1: Deseja continuar explorando a caverna?(s/n) ').upper()
        if continuar == 'S':
            print('Jogador 1: Continuando a explorar...')
            tesouro_perigo = tesouro_ou_perigo()
            if tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                print(tesouro_perigo)
                valor = valor_tesouro()
                print(f'Jogador 1: Você encontrou {valor} tesouros')
                tesouro = print(f'Jogador 1: Você pegou {dividir_tesouro(1, valor):.0f} tesouros')
                return valor, tesouro
            elif tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                print(tesouro_perigo)
                continuar = input('Jogador 1: Deseja continuar explorando a caverna?(s/n) ').upper()
                if continuar == 'S':
                    print('Jogador 1: Continuando a explorar...')
                    tesouro_perigo = tesouro_ou_perigo()
                    if tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                        print('Enquanto o grupo estava na caverna aconteceu um segundo deslizamento de pedras. E vocês ficaram presos na caverna')
                        return print('Jogador 1: Você foi preso na caverna e perdeu todos os seus tesouros')
                    elif tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                        print(tesouro_perigo)
                        valor = valor_tesouro()
                        print(f'Jogador 1: Você encontrou {valor} tesouros')
                        tesouro = print(f'Jogador 1: Você pegou {dividir_tesouro(1, valor):.0f} tesouros')
                        return valor, tesouro
                else:
                    return print('Jogador 1: Você não continuou e voltou para o acampamento')    
        else:
            print('Jogador 1: Você não continuou e voltou para o acampamento.')
            print('Jogador 1: Você não encontrou nenhum tesouro.')
            return print('A rodada acabou!')

def continuar_ou_nao_jogador2():
        continuar1 = input('Jogador 1: Deseja continuar explorando a caverna?(s/n) ').upper()
        continuar2 = input('Jogador 2: Deseja continuar explorando a caverna?(s/n) ').upper()
        if continuar1 == 'S' and continuar2 == 'S':
            print('Jogador 1: Continuando a explorar...')
            print('Jogador 2: Continuando a explorar...')
            tesouro_perigo = tesouro_ou_perigo()
            if tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                print(tesouro_perigo)
                valor = valor_tesouro()
                print(f'Jogadores 1 e 2: Vocês encontraram {valor} tesouros')
                tesouro1 = print(f'Jogadores 1: Você pegou {dividir_tesouro(2, valor)} tesouros')
                tesouro2 = print(f'Jogador 2: Você pegou {dividir_tesouro(2, valor)} tesouros')
                return valor, tesouro1, tesouro2
            elif tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                print(tesouro_perigo)
                continuar1 = input('Jogador 1: Deseja continuar explorando a caverna?(s/n) ').upper()
                continuar2 = input('Jogador 2: Deseja continuar explorando a caverna?(s/n) ').upper()
                if continuar1 == 'S' and continuar2 == 'S':
                    print('Jogador 1: Continuando a explorar...')
                    print('Jogador 2: Continuando a explorar...')
                    tesouro_perigo = tesouro_ou_perigo()
                    if tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                        print('Enquanto o grupo estava na caverna aconteceu um segundo deslizamento de pedras. E vocês ficaram presos na caverna')
                        return print('Jogadores 1 e 2: Vocês foram presos na caverna e perderam todos os seus tesouros')
                    elif tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                        print(tesouro_perigo)
                        valor = valor_tesouro()
                        valor = valor_tesouro()
                        print(f'Jogadores 1 e 2: Vocês encontraram {valor} tesouros')
                        tesouro1 = print(f'Jogadores 1: Você pegou {dividir_tesouro(2, valor):.0f} tesouros')
                        tesouro2 = print(f'Jogador 2: Você pegou {dividir_tesouro(2, valor):.0f} tesouros')
                        return valor, tesouro1, tesouro2
                    else:
                        print('Jogador: Você não continuou e voltou para o acampamento')
                        return print('A rodada acabou!')
            
        elif continuar1 == 'S'and continuar2 == 'N':
            print('Jogador 1: Continuando a explorar...')
            print('Jogador 2: Você não continuou e voltou para o acampamento')
            tesouro_perigo = tesouro_ou_perigo()
            if tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                print(tesouro_perigo)
                valor = valor_tesouro()
                print(f'Jogador 1: Você encontrou {valor} tesouros')
                tesouro = print(f'Jogador 1: Você pegou {dividir_tesouro(1, valor):.0f} tesouros')
                return valor, tesouro
            elif tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                print(tesouro_perigo)
                continuar = input('Jogador 1: Deseja continuar explorando a caverna?(s/n) ').upper()
                if continuar == 'S':
                    print('Jogador 1: Continuando a explorar...')
                    tesouro_perigo = tesouro_ou_perigo()
                    if tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                        print('Enquanto o grupo estava na caverna aconteceu um segundo deslizamento de pedras. E vocês ficaram presos na caverna')
                        return print('Jogador 1: Você foi preso na caverna e perdeu todos os seus tesouros')
                    elif tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                        print(tesouro_perigo)
                        valor = valor_tesouro()
                        print(f'Jogador 1: Você encontrou {valor} tesouros')
                        tesouro = print(f'Jogador 1: Você pegou {dividir_tesouro(1, valor):.0f} tesouros')
                        return valor, tesouro
                else:
                    print('Jogador 1: Você não continuou e voltou para o acampamento.')
                    print('Jogador 1: Você não encontrou nenhum tesouro.')
                    return print('A rodada acabou!')


        elif continuar1 == 'N' and continuar2 == 'S':
            print('Jogador 1: Você não continuou e voltou para o acampamento')
            print('Jogador 2: Continuando a explorar...')
            tesouro_perigo = tesouro_ou_perigo()
            if tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                print(tesouro_perigo)
                valor = valor_tesouro()
                print(f'Jogador 2: Você encontrou {valor} tesouros')
                tesouro = print(f'Jogador 2: Você pegou {dividir_tesouro(1, valor):.0f} tesouros')
                return valor, tesouro
            elif tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                print(tesouro_perigo)
                continuar = input('Jogador 2: Deseja continuar explorando a caverna?(s/n) ').upper()
                if continuar == 'S':
                    print('Jogador 2: Continuando a explorar...')
                    tesouro_perigo = tesouro_ou_perigo()
                    if tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                        print('Enquanto o grupo estava na caverna aconteceu um segundo deslizamento de pedras. E vocês ficaram presos na caverna')
                        return print('Jogador 2: Você foi preso na caverna e perdeu todos os seus tesouros')
                    elif tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                        print(tesouro_perigo)
                        valor = valor_tesouro()
                        print(f'Jogador 2: Você encontrou {valor} tesouros')
                        tesouro = print(f'Jogador 2: Você pegou {dividir_tesouro(1, valor):.0f} tesouros')
                        return valor, tesouro
                else:
                    print('Jogador 2: Você não continuou e voltou para o acampamento')
                    return print('A rodada acabou!')

        elif continuar1 == 'N' and continuar2 == 'N':
            print('Jogadores 1 e 2: Vocês não continuaram e voltaram para o acampamento') 
            return print('A rodada acabou!')

        else:
            print('Jogador: Você não continuou e voltou para o acampamento')
            return print('A rodada acabou!')

