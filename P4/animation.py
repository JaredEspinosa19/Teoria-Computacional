import tkinter as tk
import time
import random

HEIGHT = 600
WIDTH = 600

class Board:

    def __init__(self, height, width):
        self.size_square = height/4
        self.window = tk.Tk()
        self.window.title("Chess Board")
        self.window.iconbitmap("P4\\images\\rey.ico")
        self.window.geometry(f'{height}x{width}')
        self.window.resizable(0,0)

        self.king1 = tk.PhotoImage(file="P4\\images\\rey22.png")

        self.king2 = tk.PhotoImage(file="P4\\images\\rey21.png")

        self.interface = tk.Canvas(self.window)
        self.interface.pack(fill='both', expand=True)

        self.positions ={ '1':{'x':0, 'y':0},
                        '2':{'x':150, 'y':0},
                        '3':{'x':300, 'y':0},
                        '4':{'x':450, 'y':0},
                        
                        '5':{'x':0, 'y':150},
                        '6':{'x':150, 'y':150},
                        '7':{'x':300, 'y':150},
                        '8':{'x':450, 'y':150},
                        
                        '9':{'x':0, 'y':300},
                        '10':{'x':150, 'y':300},
                        '11':{'x':300, 'y':300},
                        '12':{'x':450, 'y':300},

                        '13':{'x':0, 'y':450},
                        '14':{'x':150, 'y':450},
                        '15':{'x':300, 'y':450},
                        '16':{'x':450   , 'y':450}
            }

        self.drawLines()

        

    def __call__(self,mov,player1,player2=[],number_p=2):

        if number_p==1:
            self.lbl = self.interface.create_image(0, 0, image = self.king1, anchor = "nw")
            k1_x = 0
            k1_y = 0
            for i in range(mov):
                #Jugador 1
                k1_difx = self.positions[player1[i]]['x'] - k1_x
                k1_dify = self.positions[player1[i]]['y'] - k1_y
                self.window.update()
                self.interface.move(self.lbl,k1_difx,k1_dify) #Son los pixeles que se va a mover NO LA NUEVA POSICION
                time.sleep(2)
                self.window.update()
                k1_x = self.positions[player1[i]]['x']
                k1_y = self.positions[player1[i]]['y']
        
        else:
            self.lbl = self.interface.create_image(0, 0, image = self.king1, anchor = "nw")
            self.lbl2 = self.interface.create_image(450, 0, image = self.king2, anchor = "nw")    
            k1_x = 0
            k1_y = 0
            k2_x = 450
            k2_y = 0
            ####
            p1 = random.randint(0,1)
            p2 = 1-p1

            print(f"Jugador 1 orden movimiento = {p1+1}")
            print(f"Jugador 2 orden movimiento = {p2+1}")

            for i in range(mov):

                if p1==0: ##Jugador 1 primero
                    #Jugador 1
                    k1_difx = self.positions[player1[i]]['x'] - k1_x
                    k1_dify = self.positions[player1[i]]['y'] - k1_y
                    self.window.update()
                    self.interface.move(self.lbl,k1_difx,k1_dify) #Son los pixeles que se va a mover NO LA NUEVA POSICION
                    time.sleep(2)
                    self.window.update()
                    #Jugador 2
                    k2_difx = self.positions[player2[i]]['x'] - k2_x
                    k2_dify = self.positions[player2[i]]['y'] - k2_y
                    self.window.update()
                    self.interface.move(self.lbl2,k2_difx,k2_dify) #Son los pixeles que se va a mover NO LA NUEVA POSICION
                    time.sleep(2)
                    self.window.update()

                else:##Jugador 2 primero
                     #Jugador 2
                    k2_difx = self.positions[player2[i]]['x'] - k2_x
                    k2_dify = self.positions[player2[i]]['y'] - k2_y
                    self.window.update()
                    self.interface.move(self.lbl2,k2_difx,k2_dify) #Son los pixeles que se va a mover NO LA NUEVA POSICION
                    time.sleep(2)
                    self.window.update()
                    #Jugador 1
                    k1_difx = self.positions[player1[i]]['x'] - k1_x
                    k1_dify = self.positions[player1[i]]['y'] - k1_y
                    self.window.update()
                    self.interface.move(self.lbl,k1_difx,k1_dify) #Son los pixeles que se va a mover NO LA NUEVA POSICION
                    time.sleep(2)
                    self.window.update()
                
                k1_x = self.positions[player1[i]]['x']
                k1_y = self.positions[player1[i]]['y']
                k2_x = self.positions[player2[i]]['x']
                k2_y = self.positions[player2[i]]['y']



        self.window.mainloop()

    def drawLines(self):

        for i in range(4):
            for j in range(4):
                if(i+j)%2==0:
                    self.interface.create_rectangle(i*self.size_square, j*self.size_square,(i+1)*self.size_square,(j+1)*self.size_square,fill= "#B22222")
                else:
                    self.interface.create_rectangle(i*self.size_square, j*self.size_square,(i+1)*self.size_square,(j+1)*self.size_square,fill= "#000000")
        
    

## SE DEBE CREAR EL TABLERPO
## Y CUANDO SE LLAMAN SE DEBE MANDAR EL NUMERO DE MOVIMIENTOS
## Y MANDAR LOS MOVIMIENTOS, EN LISTAS

# chess = Board(600,600)
# chess(5,['1','2','3','4','8'],['3','7','8','12','16'],2)
# # chess(5,['1','2','3','4','8'],[],1)