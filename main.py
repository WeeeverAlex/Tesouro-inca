from numpy import true_divide
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
rodada = True
rodadas = 1





#Funcao pega no projeto deep sea adventure, para colocar slow entre os prints
def print_slow(str): 
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02) 

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
    print_slow(Fore.LIGHTRED_EX + 'Seja bem vindo ao Templo Maia, aqui você irá encontrar tesouros valiosos, mas tome cuidado, pois a caverna é perigosa!')
    print()
    print()
    print_slow('Seu objetivo é conseguir o maior número de tesouros possíveis e voltar para o acampamento com vida!')
    print()
    print()
    print_slow('Boa sorte!'+ Style.RESET_ALL)
    print()
    print()        

while jogo:
    print(Fore.RED + "Iniciando Rodada"+ Style.RESET_ALL)
    continuar1 = input('Jogador 1: Deseja continuar explorando a caverna?(s/n) ').upper()
    continuar2 = input('Jogador 2: Deseja continuar explorando a caverna?(s/n) ').upper()
    if continuar1 == 'S' and continuar2 == 'S':
        print('Jogador 1: Continuando a explorar...')
        print('Jogador 2: Continuando a explorar...')
        tesouro_perigo = tesouro_ou_perigo()

        if tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
            print(tesouro_perigo)
            valor = valor_tesouro()
            dividir = dividir_tesouro(2, valor)
            print(f'Jogadores 1 e 2: Vocês encontraram {valor} tesouros')
            tesouro1 = print(f'Jogadores 1: Você pegou {dividir} tesouros')
            tesouro2 = print(f'Jogador 2: Você pegou {dividir} tesouros')
            tesouros_jogador1 += dividir
            tesouros_jogador2 += dividir
            continuar1 = input('Jogador 1: Deseja continuar explorando a caverna?(s/n) ').upper()
            continuar2 = input('Jogador 2: Deseja continuar explorando a caverna?(s/n) ').upper()

            if continuar1 == 'S' and continuar2 == 'S':
                print('Jogador 1: Continuando a explorar...')
                print('Jogador 2: Continuando a explorar...')
                tesouro_perigo2 = tesouro_ou_perigo()

                if tesouro_perigo2 == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                    print('Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.')
                    

                elif tesouro_perigo2 == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                    print(tesouro_perigo)
                    valor = valor_tesouro()
                    dividir = dividir_tesouro(2, valor)
                    print(f'Jogadores 1 e 2: Vocês encontraram {valor} tesouros')
                    tesouro1 = print(f'Jogadores 1: Você pegou {dividir:.0f} tesouros')
                    tesouro2 = print(f'Jogador 2: Você pegou {dividir:.0f} tesouros')
                    tesouros_jogador1 += dividir
                    tesouros_jogador2 += dividir

        
                else:
                    print('Jogador: Você não continuou e voltou para o acampamento')
                    print('A rodada acabou!')
                    
                    

            elif continuar1 == 'S' and continuar2 == 'N':
                print('Jogador 1: Continuando a explorar...')
                print('Jogador 2: Você não continuou e voltou para o acampamento')
                tesouro_perigo = tesouro_ou_perigo()
                if tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                    print(tesouro_perigo)
                    valor = valor_tesouro()
                    dividir = dividir_tesouro(2, valor)
                    print(f'Jogador 1: Você encontrou {valor} tesouros')
                    tesouro = print(f'Jogador 1: Você pegou {dividir:.0f} tesouros')
                    tesouros_jogador1 += dividir
                

                    
                elif tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                    print(tesouro_perigo)
                    continuar = input('Jogador 1: Deseja continuar explorando a caverna?(s/n) ').upper()
                    if continuar == 'S':
                        print('Jogador 1: Continuando a explorar...')
                        tesouro_perigo = tesouro_ou_perigo()
                        if tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                            print('Enquanto o grupo estava na caverna aconteceu um segundo deslizamento de pedras. E vocês ficaram presos na caverna')
                            print('Jogador 1: Você foi preso na caverna e perdeu todos os seus tesouros')
                            

                        elif tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                            print(tesouro_perigo)
                            valor = valor_tesouro()
                            dividir = dividir_tesouro(2, valor)
                            print(f'Jogador 1: Você encontrou {valor} tesouros')
                            tesouro = print(f'Jogador 1: Você pegou {dividir:.0f} tesouros')
                            tesouros_jogador1 += dividir
                            
                            
                    else:
                        print('Jogador 1: Você não continuou e voltou para o acampamento.')
                        print('Jogador 1: Você não encontrou nenhum tesouro.')
                        print('A rodada acabou!')
                        
                

            elif continuar1 == 'N' and continuar2 == 'S':
                print('Jogador 1: Você não continuou e voltou para o acampamento')
                print('Jogador 2: Continuando a explorar...')
                tesouro_perigo = tesouro_ou_perigo()
                if tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                    print(tesouro_perigo)
                    valor = valor_tesouro()
                    dividir = dividir_tesouro(2, valor)
                    print(f'Jogador 2: Você encontrou {valor} tesouros')
                    tesouro = print(f'Jogador 2: Você pegou {dividir:.0f} tesouros')
                    tesouros_jogador2 += dividir
                   

                    
                elif tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                    print(tesouro_perigo)
                    continuar = input('Jogador 2: Deseja continuar explorando a caverna?(s/n) ').upper()
                    if continuar == 'S':
                        print('Jogador 2: Continuando a explorar...')
                        tesouro_perigo = tesouro_ou_perigo()
                        if tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                            print('Enquanto o grupo estava na caverna aconteceu um segundo deslizamento de pedras. E vocês ficaram presos na caverna')
                            print('Jogador 2: Você foi preso na caverna e perdeu todos os seus tesouros')
                            

                        elif tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                            print(tesouro_perigo)
                            valor = valor_tesouro()
                            dividir = dividir_tesouro(2, valor)
                            print(f'Jogador 2: Você encontrou {valor} tesouros')
                            tesouro = print(f'Jogador 2: Você pegou {dividir:.0f} tesouros')
                            tesouros_jogador2 += dividir
                            
                            
                    else:
                        print('Jogador 2: Você não continuou e voltou para o acampamento')
                        print('A rodada acabou!')
                   

            elif continuar1 == 'N' and continuar2 == 'N':
                print('Jogadores 1 e 2: Vocês não continuaram e voltaram para o acampamento') 
                print('A rodada acabou!')
              

            else:
                print('Jogador 1: Você não digitou uma opção válida')
                print('Jogador 2: Você não digitou uma opção válida')
                print('A rodada acabou!') 
             
                


        elif tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
            print(tesouro_perigo)
            continuar1 = input('Jogador 1: Deseja continuar explorando a caverna?(s/n) ').upper()
            continuar2 = input('Jogador 2: Deseja continuar explorando a caverna?(s/n) ').upper()

            if continuar1 == 'S' and continuar2 == 'S':
                print('Jogador 1: Continuando a explorar...')
                print('Jogador 2: Continuando a explorar...')
                tesouro_perigo2 = tesouro_ou_perigo()

                if tesouro_perigo2 == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                    print('Enquanto o grupo estava na caverna aconteceu um segundo deslizamento de pedras. E vocês ficaram presos na caverna')
                    print('Jogadores 1 e 2: Vocês foram presos na caverna e perderam todos os seus tesouros')
                 

                elif tesouro_perigo2 == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                    print(tesouro_perigo2)
                    valor = valor_tesouro()
                    dividir = dividir_tesouro(2, valor)
                    print(f'Jogadores 1 e 2: Vocês encontraram {valor} tesouros')
                    tesouro1 = print(f'Jogadores 1: Você pegou {dividir:.0f} tesouros')
                    tesouro2 = print(f'Jogador 2: Você pegou {dividir:.0f} tesouros')
                    tesouros_jogador1 += dividir
                    tesouros_jogador2 += dividir
                    
        
                else:
                    print('Jogador: Você não continuou e voltou para o acampamento')
                    print('A rodada acabou!')
                  
        
                
            elif continuar1 == 'S' and continuar2 == 'N':
                print('Jogador 1: Continuando a explorar...')
                print('Jogador 2: Você não continuou e voltou para o acampamento')
                tesouro_perigo = tesouro_ou_perigo()
                if tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                    print(tesouro_perigo)
                    valor = valor_tesouro()
                    dividir = dividir_tesouro(2, valor)
                    print(f'Jogador 1: Você encontrou {valor} tesouros')
                    tesouro = print(f'Jogador 1: Você pegou {dividir:.0f} tesouros')
                    tesouros_jogador1 += dividir
                    

                    
                elif tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                    print(tesouro_perigo)
                    continuar = input('Jogador 1: Deseja continuar explorando a caverna?(s/n) ').upper()
                    if continuar == 'S':
                        print('Jogador 1: Continuando a explorar...')
                        tesouro_perigo = tesouro_ou_perigo()
                        if tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                            print('Enquanto o grupo estava na caverna aconteceu um segundo deslizamento de pedras. E vocês ficaram presos na caverna')
                            print('Jogador 1: Você foi preso na caverna e perdeu todos os seus tesouros')
                            
                            

                        elif tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                            print(tesouro_perigo)
                            valor = valor_tesouro()
                            dividir = dividir_tesouro(2, valor)
                            print(f'Jogador 1: Você encontrou {valor} tesouros')
                            tesouro = print(f'Jogador 1: Você pegou {dividir:.0f} tesouros')
                            tesouros_jogador1 += dividir
                            
                            
                    else:
                        print('Jogador 1: Você não continuou e voltou para o acampamento.')
                        print('Jogador 1: Você não encontrou nenhum tesouro.')
                        print('A rodada acabou!')



            elif continuar1 == 'N' and continuar2 == 'S':
                print('Jogador 1: Você não continuou e voltou para o acampamento')
                print('Jogador 2: Continuando a explorar...')
                tesouro_perigo = tesouro_ou_perigo()
                if tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                    print(tesouro_perigo)
                    valor = valor_tesouro()
                    dividir = dividir_tesouro(2, valor)
                    print(f'Jogador 2: Você encontrou {valor} tesouros')
                    tesouro = print(f'Jogador 2: Você pegou {dividir:.0f} tesouros')
                    tesouros_jogador2 += dividir
                   

                    
                elif tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                    print(tesouro_perigo)
                    continuar = input('Jogador 2: Deseja continuar explorando a caverna?(s/n) ').upper()
                    if continuar == 'S':
                        print('Jogador 2: Continuando a explorar...')
                        tesouro_perigo = tesouro_ou_perigo()
                        if tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                            print('Enquanto o grupo estava na caverna aconteceu um segundo deslizamento de pedras. E vocês ficaram presos na caverna')
                            print('Jogador 2: Você foi preso na caverna e perdeu todos os seus tesouros')
                        elif tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                            print(tesouro_perigo)
                            valor = valor_tesouro()
                            dividir = dividir_tesouro(2, valor)
                            print(f'Jogador 2: Você encontrou {valor} tesouros')
                            tesouro = print(f'Jogador 2: Você pegou {dividir:.0f} tesouros')
                            tesouros_jogador2 += dividir
                            
                            
                    else:
                        print('Jogador 2: Você não continuou e voltou para o acampamento')
                        print('A rodada acabou!')
                    

            elif continuar1 == 'N' and continuar2 == 'N':
                print('Jogadores 1 e 2: Vocês não continuaram e voltaram para o acampamento') 
                print('A rodada acabou!')
              
               
            else:
                print('Jogador 1: Você não digitou uma opção válida')
                print('Jogador 2: Você não digitou uma opção válida')
                print('A rodada acabou!') 
               
        

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    elif continuar1 == 'S' and continuar2 == 'N':
        print('Jogador 1: Continuando a explorar...')
        print('Jogador 2: Você não continuou e voltou para o acampamento')
        tesouro_perigo = tesouro_ou_perigo()
        if tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
            print(tesouro_perigo)
            dividir = dividir_tesouro(1, valor)
            valor = valor_tesouro()
            print(f'Jogador 1: Você encontrou {valor} tesouros')
            tesouro = print(f'Jogador 1: Você pegou {dividir:.0f} tesouros')
            tesouros_jogador1 += dividir
            
            
        elif tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
            print(tesouro_perigo)
            continuar = input('Jogador 1: Deseja continuar explorando a caverna?(s/n) ').upper()
            if continuar == 'S':
                print('Jogador 1: Continuando a explorar...')
                tesouro_perigo = tesouro_ou_perigo()
                if tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                    print('Enquanto o grupo estava na caverna aconteceu um segundo deslizamento de pedras. E vocês ficaram presos na caverna')
                    print('Jogador 1: Você foi preso na caverna e perdeu todos os seus tesouros')
                elif tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                    print(tesouro_perigo)
                    valor = valor_tesouro()
                    dividir = dividir_tesouro(2, valor)
                    print(f'Jogador 1: Você encontrou {valor} tesouros')
                    tesouro = print(f'Jogador 1: Você pegou {dividir:.0f} tesouros')
                    tesouros_jogador1 += dividir
                    
                    
            else:
                print('Jogador 1: Você não continuou e voltou para o acampamento.')
                print('Jogador 1: Você não encontrou nenhum tesouro.')
                print('A rodada acabou!')
                
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    elif continuar1 == 'N' and continuar2 == 'S':
        print('Jogador 1: Você não continuou e voltou para o acampamento')
        print('Jogador 2: Continuando a explorar...')
        tesouro_perigo = tesouro_ou_perigo()
        if tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
            print(tesouro_perigo)
            valor = valor_tesouro()
            dividir = dividir_tesouro(2, valor)
            print(f'Jogador 2: Você encontrou {valor} tesouros')
            tesouro = print(f'Jogador 2: Você pegou {dividir:.0f} tesouros')
            tesouros_jogador2 += dividir
            
            
        elif tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
            print(tesouro_perigo)
            continuar = input('Jogador 2: Deseja continuar explorando a caverna?(s/n) ').upper()
            if continuar == 'S':
                print('Jogador 2: Continuando a explorar...')
                tesouro_perigo = tesouro_ou_perigo()
                if tesouro_perigo == 'Enquanto o grupo estava na caverna aconteceu um deslizamento de pedras. Se ocorrer denovo, vocês ficarão presos na caverna.':
                    print('Enquanto o grupo estava na caverna aconteceu um segundo deslizamento de pedras. E vocês ficaram presos na caverna')
                    print('Jogador 2: Você foi preso na caverna e perdeu todos os seus tesouros')
                elif tesouro_perigo == 'Enquanto o grupo estava na caverna descobriram um tesouro':
                    print(tesouro_perigo)
                    valor = valor_tesouro()
                    dividir = dividir_tesouro(2, valor)
                    print(f'Jogador 2: Você encontrou {valor} tesouros')
                    tesouro = print(f'Jogador 2: Você pegou {dividir:.0f} tesouros')
                    tesouros_jogador2 += dividir
                    
                    
            else:
                print('Jogador 2: Você não continuou e voltou para o acampamento')
                print('A rodada acabou!')
              
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#                    

    elif continuar1 == 'N' and continuar2 == 'N':
        print('Jogadores 1 e 2: Vocês não continuaram e voltaram para o acampamento') 
        print('A rodada acabou!')
       
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    else:
        print('Jogador: Você não continuou e voltou para o acampamento')
        print('A rodada acabou!')
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    if tesouros_jogador1 > tesouros_jogador2:
        print('Jogador 1: Você ganhou a rodada!')
        print()

    elif tesouros_jogador1 < tesouros_jogador2:
        print('Jogador 2: Você ganhou a rodada!')
        print()

    else:
        print('Jogadores: Empate!')
        print()

    rodadas += 1
    print(Fore.CYAN +'--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(f'Rodada {rodadas}' +Style.RESET_ALL )

    jogo = True


    


    
    