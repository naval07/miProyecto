import tkinter as tk
from tkinter import messagebox
import classAli as al
import tkinter.font as tkFont
from tkinter import font

class App:

    def __init__(self, fondoname, list):

        self.als = list
        self.fondo = str(fondoname)
        self.win = tk.Tk()
        self.win.geometry("750x450")
        self.bgim = tk.PhotoImage(file = self.fondo)
        self.bg = tk.Label(self.win, image = self.bgim)
        self.bg.pack()
        #msj = "Para sumar un pase bueno optima la flecha arriba\n\nPara sumar un pase malo oprima la flecha abajo"
        #messagebox.showinfo("Empezar", msj)

        def quit(e):
            self.win.destroy()
        self.win.bind("<q>", quit)

        defe = al.ChooseAl(self.win, self.bg, self.bgim, self.als)

        self.win.mainloop()

        
"""als = ["4-3-3", "4-2-3-1"]
x = App("fondoapp.png", als)"""
#root = tk.Tk()
#print(tkFont.families())
#print(tkFont.names())
#izquierda
"""tk.Button(self.win).place(x = 40, y = 200, height = 50, width = 50) # Arquero
tk.Button(self.win).place(x = 180, y = 20, height = 50, width = 50) # lateral I
tk.Button(self.win).place(x = 122, y = 140, height = 50, width = 50) # Central I
tk.Button(self.win).place(x = 122, y = 260, height = 50, width = 50) # Central D
tk.Button(self.win).place(x = 180, y = 375, height = 50, width = 50) # Lateral D
tk.Button(self.win).place(x = 252, y = 140, height = 50, width = 50) # 6 I
tk.Button(self.win).place(x = 252, y = 260, height = 50, width = 50) # 6 D
tk.Button(self.win).place(x = 335, y = 45, height = 50, width = 50) # extremo I
tk.Button(self.win).place(x = 335, y = 200, height = 50, width = 50) # 10
tk.Button(self.win).place(x = 335, y = 350, height = 50, width = 50) # extremo D
tk.Button(self.win).place(x = 435, y = 200, height = 50, width = 50) # del"""
#derecha
"""tk.Button(self.win).place(x = 660, y = 200, height = 50, width = 50) # Arquero
tk.Button(self.win).place(x = 530, y = 20, height = 50, width = 50) # Lateral D
tk.Button(self.win).place(x = 580, y = 140, height = 50, width = 50) # Central D
tk.Button(self.win).place(x = 580, y = 260, height = 50, width = 50) # Central I
tk.Button(self.win).place(x = 530, y = 375, height = 50, width = 50) # lateral I
tk.Button(self.win).place(x = 450, y = 140, height = 50, width = 50) # 6 D
tk.Button(self.win).place(x = 450, y = 260, height = 50, width = 50) # 6 I
tk.Button(self.win).place(x = 360, y = 45, height = 50, width = 50) # extremo D
tk.Button(self.win).place(x = 360, y = 200, height = 50, width = 50) # 10
tk.Button(self.win).place(x = 360, y = 355, height = 50, width = 50) # extremo I
tk.Button(self.win).place(x = 260, y = 200, height = 50, width = 50) # del"""
