from functions import *
import sys
import time
from random import *
from colorama import init, Fore, Style
init()


#Funcao pega no projeto deep sea adventure, para colocar slow entre os prints
def print_slow(str): 
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02) 

jogo = True
rodadas = 1

#começo
print()
print_slow('=================================================')
print()
print_slow('         Bem-vindo ao Tesouro Maia!          ')
print()
print_slow('=================================================')
print()
print()
print_slow('Boa sorte para encontrar tesouros valiosos e tome cuidado dentro da caverna =)')
print()
print()
começar = input(Fore.GREEN + 'pressione C para começar:  '+ Style.RESET_ALL).upper()
print()
if começar == 'C':
    print_slow('BEM VINDO AO TEMPLO MAIA!')     
    print()
    print()
    print_slow(Fore.RED + '')
    print_slow('   \ *          .   .   |    *  . .  ~    .      .  .  , ')
    print()
    print_slow(' ,    `-.  .            :               *           ,- ')
    print()
    print_slow('  -       `-.       *._/_\_.       .       .   ,-'  )
    print()
    print_slow('   -         `-_.,     |n|     .      .       ; ')
    print()
    print_slow('    -             \ ._/_,_\_.  .          . ,-         -')
    print()
    print_slow('     -             ._/_,_,_\_.    ,-----``         - ')
    print()
    print_slow('   -                 |..n..|-``-`                - ')
    print()
    print_slow('   -              ._/_,_,_,_\_.                 - ')
    print()
    print_slow('    -           ,  -|...n...|                  - ')
    print()
    print_slow('      -     ,-`.  _/_,_,_,_,_\_.              - ')
    print()
    print_slow('        - ,-=-`    |....n....|              - ')
    print()
    print_slow('       -;       ._/_,_,_,_,_,_\_.         - ')
    print()
    print_slow('      ,-          |.....n.....|          - ')
    print()
    print_slow('    ,;         ._/_,_,_,_,_,_,_\_.         - ')
    print()
    print_slow('`,  `.  `.  ".  `| n   ,-.   n |  ``,  `.  `,  ``.  `,  `, ')
    print()
    print_slow(',.:;..;;..;;.,o__|__o !.|.! o__|__o;,.:;.,;;,,:;,.:;,;;: ')
    print()
    print_slow('][  ][  ][  ][|_i_i_H_|_|_|_H_i_i_|  ][  ][  ][  ][  ][ ')
    print()
    print_slow('              |     //=====\\     | ')
    print()
    print_slow('              |____//=======\\____| ')
    print()
    print_slow('                  //=========\\   ' + Style.RESET_ALL)
    print()
    print()
    print_slow(Fore.BLUE + 'Seja bem vindo ao Templo Maia, aqui você irá encontrar tesouros valiosos, mas tome cuidado, pois a caverna é perigosa!')
    print()
    print()
    print_slow('Seu objetivo é conseguir o maior número de tesouros possíveis e voltar para o acampamento com vida!')
    print()
    print()
    print_slow('Se ocorrer um deslizamento de pedras 2 vezes você perderá todo seus tesouros e rodada terminará!')
    print()
    print()
    print_slow('A rodada, também termina quando todos os jogadores voltam para o acampamento')
    print()
    print()
    print_slow('Boa sorte!'+ Style.RESET_ALL)
    print()
    print()
   


while jogo:
    rodada = True
    perigo = 0
    tesouro_jogador1 = 0
    tesouro_jogador2 = 0
    continuar1 = 'S'
    continuar2 = 'S'
    retorno = True

    print(Fore.CYAN +'-------------------------------------------------------------------------------------------------------------------------------------------')
    print(f'Rodada {rodadas}' +Style.RESET_ALL )
    print()

    while rodada:

        if continuar1 == 'S':
            continuar1 = input('Jogador 1: Deseja continuar explorando a caverna?(s/n) ').upper()
            
            
        if continuar2 == 'S':
            continuar2 = input('Jogador 2: Deseja continuar explorando a caverna?(s/n) ').upper()
            print()

        #entrada invalida no input
        while continuar1 != 'S' and continuar1 != 'N':
            print(Fore.LIGHTMAGENTA_EX+'Entrada inválida'+ Style.RESET_ALL)
            print()
            continuar1 = input('Jogador 1: Deseja continuar explorando a caverna?(s/n) ').upper()
            continuar2 = input('Jogador 2: Deseja continuar explorando a caverna?(s/n) ').upper()
            print()

        while continuar2 != 'S' and continuar2 != 'N':
            print(Fore.LIGHTMAGENTA_EX+'Entrada inválida'+ Style.RESET_ALL)
            print()
            continuar1 = input('Jogador 1: Deseja continuar explorando a caverna?(s/n) ').upper()
            continuar2 = input('Jogador 2: Deseja continuar explorando a caverna?(s/n) ').upper()
            print()    

        sorteio = tesouro_ou_perigo()
        print()


        if continuar1 == 'S' and continuar2 == 'S':

            if sorteio == 2:
                perigo += 1
                print(Fore.RED + 'Perigo' + Style.RESET_ALL)
                print()
                

                if perigo == 2:
                    tesouro_jogador1 = 0
                    tesouro_jogador2 = 0
                    print('Vocês foram presos na caverna')
                    print()
                    if tesouro_jogador1 > tesouro_jogador2:
                        print('Jogador 1 venceu a rodada!')
                        print(f'Tesouros do Jogador1: {tesouro_jogador1}')
                        print()
                    elif tesouro_jogador1 < tesouro_jogador2:
                        print(f'Tesouros do Jogador2: {tesouro_jogador1}')
                        print('Jogador 2 venceu a rodada!')    
                        print()
                    else:
                        print(Fore.BLUE+ 'Empate!' + Style.RESET_ALL)
                        print()
                    rodada = False
                    rodadas += 1

            elif sorteio == 1:
                tesouro = valor_tesouro()
                print(f'Valor do tesouro: {tesouro}')
                tesouro_dividido = dividir_tesouro(2, tesouro)
                tesouro_jogador1 += tesouro_dividido
                tesouro_jogador2 += tesouro_dividido
                print(f'Jogador1: {tesouro_jogador1}')
                print(f'Jogador2: {tesouro_jogador2}')
                print()

        elif continuar1 == 'S':
            if retorno == True:
                print('Jogador 2: retornou ao acampamento')
                print()
                retorno = False

            if sorteio == 2:
                perigo += 1
                print(Fore.RED + 'Perigo' + Style.RESET_ALL)
                print()
                

                if perigo == 2:
                    tesouro_jogador1 = 0
                    print('Jogador 1: Você ficou preso na caverna')
                    if tesouro_jogador1 > tesouro_jogador2:
                        print('Jogador 1 venceu a rodada!')
                        print(f'Tesouros do Jogador1: {tesouro_jogador1}')
                        print()
                    elif tesouro_jogador1 < tesouro_jogador2:
                        print(f'Tesouros do Jogador2: {tesouro_jogador1}')
                        print('Jogador 2 venceu a rodada!')    
                        print()
                    else:
                        print(Fore.BLUE+ 'Empate!' + Style.RESET_ALL)
                        print()
                    rodada = False
                    rodadas += 1
                    

            elif sorteio == 1:
                tesouro = valor_tesouro()
                print(f'Valor do tesouro: {tesouro}')
                tesouro_jogador1 += tesouro
                print(f'Jogador1: {tesouro_jogador1}')
                print()

           
        elif continuar2 == 'S':
            if retorno == True:
                print('Jogador 1: retornou ao acampamento')
                print()
            retorno = False

            if sorteio == 2:
                perigo += 1
                print(Fore.RED + 'Perigo' + Style.RESET_ALL)
                print()
                

                if perigo == 2:
                    print('Jogador2: Você ficou preso na caverna')
                    print()
                    tesouro_jogador2 = 0
                    if tesouro_jogador1 > tesouro_jogador2:
                        print('Jogador 1 venceu a rodada!')
                        print()
                        print(f'Tesouros do Jogador1: {tesouro_jogador1}')
                        print()
                    elif tesouro_jogador1 < tesouro_jogador2:
                        print('Jogador 2 venceu a rodada!')
                        print()
                        print(f'Tesouros do Jogador2: {tesouro_jogador2}')  
                        print()
                    else:
                        print(Fore.BLUE+ 'Empate!' + Style.RESET_ALL)
                        print()   
                    rodada = False
                    rodadas += 1
                    

            elif sorteio == 1:
                tesouro = valor_tesouro()
                print(f'Valor do tesouro: {tesouro}')
                tesouro_jogador2 += tesouro
                print(f'Jogador1: {tesouro_jogador2}')
                print()

            
        else:
            print()
            print(Fore.CYAN + "TODOS OS JOGADORES SAIRAM DA CAVERNA E RETORNARAM AO ACAMPAMENTO" + Style.RESET_ALL)
            print()
            print(f'Teosuros do Jogador1: {tesouro_jogador1}')
            print(f'Tesouros do Jogador2: {tesouro_jogador2}')
            print()

            if tesouro_jogador1 > tesouro_jogador2:
                print('Jogador 1 venceu a rodada!')
                print()
                print(tesouro_jogador1)
                print()
            elif tesouro_jogador1 < tesouro_jogador2:
                print(tesouro_jogador2)
                print()
                print('Jogador 2 venceu a rodada!')    
                print()
            else:
                print(Fore.BLUE+ 'Empate!' + Style.RESET_ALL)
                print()
            rodada = False
            rodadas += 1
            
        
