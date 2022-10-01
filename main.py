from functions import *
import sys
import time
from random import *
from colorama import init, Fore, Style
init()

#variaveis
jogadores = 0

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

#if perigo_ou_tesouro == tesouro:
   #valor_do_tesouro = valor_tesouro()
    #print_slow(f'O valor do tesouro é {valor_do_tesouro}')
    #divindo = dividir_tesouro(quantos_jogadores)
    #print_slow(f'Os jogadores dividiram o tesouro e cada um ficou com {divindo}')
    #print()


    
