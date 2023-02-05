import animation as an
import chess_automata as afn
import random
import linecache
import sys
import os
sys.setrecursionlimit(10**6)


chess = { '1':{'r': ['6'], 'n':['2','5']},
          '2':{'r': ['1','3','6'], 'n':['5','7']},
          '3':{'r': ['6','8'], 'n':['2','4','7']},
          '4':{'r': ['3','8'], 'n':['7']},
          '5':{'r': ['1','6','9'], 'n':['2','10']},        
          '6':{'r': ['1','3','9','11'], 'n':['2','5','7','10']},
          '7':{'r': ['3','6','8','11'], 'n':['2','4','10','12']},
          '8':{'r': ['3','11'], 'n':['4','7','12']},
          '9':{'r': ['6','14'], 'n':['5','10','13']},
          '10':{'r': ['6','9','11','14'], 'n':['5','7','13','15']},        
          '11':{'r': ['6','8','14','16'], 'n':['7','10','12','15']},
          '12':{'r': ['8','11','16'], 'n':['7','15']},
          '13':{'r': ['9','14'], 'n':['10']},
          '14':{'r': ['9','11'], 'n':['10','13','15']},
          '15':{'r': ['11','14','16'], 'n':['10','12']},
          '16':{'r': ['11'], 'n':['12','15']}

}

alfabeto = {'r','n'}

def chooseMove(wm1,lm1,wm2,lm2,num):
   
    str1 = ""
    if os.path.exists(r"P4\\WinnerMoves1.txt"):
        moves = linecache.getline(r"P4\\WinnerMoves1.txt",random.randint(1,wm1))
        str_1 = "Jugada Ganadora"
    else:
        moves = linecache.getline(r"P4\\Moves1.txt",random.randint(1,lm1))
        str_1 = "Jugada No Ganadora"
   
    play = moves[:-1] if '\n' in moves else moves     
    p1 = play.split(',')
    
    str_2 = ""
    if num==2:
        state = True

        while state == True:
            
            if os.path.exists(r"P4\\WinnerMoves2.txt"):
                moves2 = linecache.getline(r"P4\\WinnerMoves2.txt",random.randint(1,wm2))
                str_2 = "Jugada Ganadora"
            else:
                moves2 = linecache.getline(r"P4\\Moves2.txt",random.randint(1,lm2))
                str_2 = "Jugada No Ganadora"
            play = moves2[:-1] if '\n' in moves2 else moves2       
            p2 = play.split(',')

            for i in range(len(p1)):
                p_1 = p1[i]
                p_2 = p2[i]

                if p_1 == p_2 or p_1==p2[i-1] or p_2==p1[i-1]:
                    
                    state=True
                    break
                else:
                    state=False
    
    else:
        p2 = []
                
    return p1,p2,str_1,str_2
    
def rankMoves(final_state, file ,n_file):

    wm=0
    lm=0

    with open(file,'r') as file:
        
        for line in file:
            x = line[:-1] if '\n' in line else line

            if(x[-1*len(final_state):]==final_state):
                f = open(f"P4\\WinnerMoves{n_file}.txt",'a')
                f.write(line)
                wm+=1
            else:
                f = open(f"P4\\LosserMoves{n_file}.txt",'a')
                f.write(line)   
                lm+=1
            f.close()

    return wm,lm

def createMovement(len):

    string = ""
    for x in range(len):
        ran = random.randint(0,1)
        if ran == 0: #r
            string = string + 'r' 
        else: #n
            string = string + 'n'

    return string


if __name__=='__main__':

   #INICIO PROGRAMA
    print("-----------------JUEGO AJEDREZ-------------------")
    print("Seleccione el número de jugadores: ")
    print("1 jugador ")
    print("2 jugadores ")
    num = int(input(""))

    print("Seleccione el modo en que se ejecutará el juego:")
    print("1 - Manual ")
    print("2 - Automático ")
    modo = int(input(""))

    str_1 = ''
    str_2 = ''
    mov = 0

    if modo==1: #modo manual
        if num==1:
            print("Escriba la cadena de movimientos del jugador 1")
            str_1 = input("Movimientos aceptados: n y r ")
            str_2 = ""
            mov = len(str_1)
        else:
            print("Escriba la cadena de movimientos del jugador 1")
            str_1 = input("Movimientos aceptados: n y r ")
            print("Escriba la cadena de movimientos del jugador 2")
            str_2 = input("Movimientos aceptados: n y r ")
            mov = len(str_1)
    else:#aumatico
        mov = random.randint(1,10)
        str_1 = createMovement(mov)
        str_2 = createMovement(mov)

    #Crear automatas
    player1 = afn.AFN(chess,alfabeto,'16','1')
    player2 = afn.AFN(chess,alfabeto,"13",'4')
    
    #Crear jugadas
    path_1 = player1.getMoves(str_1,[],1)
    path_2 = player2.getMoves(str_2,[],2)
    
    # #CLasificar jugadas
    wm1,lm1 = rankMoves(player1.estados_finale,path_1,1)
    wm2,lm2 = rankMoves(player2.estados_finale,path_2,2)
    
    #Escoger dos jugadas
    if num==1:
        key1,key2,st_1,st_2 = chooseMove(wm1,lm1,wm2,lm2,1)
    else:
        key1,key2,st_1,st_2 = chooseMove(wm1,lm1,wm2,lm2,2)

    #Checar
    if num==1:
        print("Movimientos")
        print("Jugador 1")
        print(str_1)
        print("\n")

        print("Jugada obtenida")
        print("Jugador 1 : ")
        print(key1)
        print(st_1)
        print("\n")
        key2 = []
    else:
        print("Movimientos")
        print("Jugador 1:")
        print(str_1)
        print("\n")
        print("Jugador 2:")
        print(str_2)
        print("\n")
    
        print("Jugadas obtenidas")
        print("Jugador 1 : ")
        print(key1)
        print(st_1)
        print("\n")
        print("Jugador 2 : ")
        print(key2)
        print(st_2)
        print("\n")
        
    #Animacion
    chess = an.Board(600,600)
    chess(mov,key1,key2,num)
