import tkinter as tk

#class brsPlayer(WinDatos):
class brsPlayer:
    #global dataBases


    def __init__(self):
        self.win = tk.Tk()
        self.frame = tk.Frame(self.win)
        self.frame.pack()

        n = tk.StringVar()

        tk.Label(self.frame, text = "Nombre del jugador: ").grid(row = 0, column = 0, sticky = "nw")
        self.name = tk.Entry(self.frame, textvariable = n)
        self.name.grid(row = 0, column = 1)

        buscar = tk.Button(self.win, text = "Buscar")
        buscar.pack()

        self.win.mainloop()

    def searchPlayer(window):
        #global jugadores
        for q in jugadores:
            if self.name.get() == q:
                #abrir un objeto WinDatos
                window.destroy()



#x = brsPlayer()
