import tkinter as tk
import time

HEIGHT = 500
WIDTH = 500

class Board:

    def __init__(self, height, width):
        self.size_square = height/4
        self.window = tk.Tk()
        self.window.title("Turing Machine")
        self.window.geometry(f'{height}x{width}')
        self.window.resizable(0,0)

        self.interface = tk.Canvas(self.window)
        self.interface.pack(fill='both', expand=True)
        self.interface.configure(bg="black")

        self.drawLines()

    def __call__(self, estados):

        time.sleep(2)
        self.window.update()

        N = len(estados)
        for i in range(N):
            if i == N-1:
                self.interface.create_rectangle(220, 120, 280, 180, outline="#000", fill="#000")
                self.interface.create_rectangle(10, 280, 480, 480, outline="#000", fill="#000")
                self.interface.create_text(250,150, anchor="w",font = "Consola", text = "f", fill="white")
                self.interface.create_text(100,300, anchor="w",font = "Consola", text = estados[i][0], fill="white")
                self.interface.create_text(320,300, anchor="w",font = "Consola", text = estados[i][1][1:], fill="white")
                self.interface.create_text(250,300, anchor="w",font = "Consola", text = estados[i][1][0], fill="white")
                self.window.update()
                time.sleep(2)
                self.window.update()
            else:
                self.interface.create_rectangle(220, 120, 280, 180, outline="#000", fill="#000")
                self.interface.create_rectangle(10, 280, 480, 480, outline="#000", fill="#000")
                self.interface.create_text(250,150, anchor="w",font = "Consola", text = "q",fill="white")
                self.interface.create_text(100,300, anchor="w",font = "Consola", text = estados[i][0], fill="white")
                self.interface.create_text(320,300, anchor="w",font = "Consola", text = estados[i][1][1:], fill="white")
                self.interface.create_text(250,300, anchor="w",font = "Consola", text = estados[i][1][0], fill="white")
                self.window.update()
                time.sleep(2)
                self.window.update()
       
        self.window.mainloop()

    def drawLines(self):

        self.interface.create_rectangle(200, 100, 300, 200, outline="#FFF", fill="#000")
        self.interface.create_rectangle(250, 210, 250, 260, dash=(2,2),  outline="#FFF", fill="#000")
