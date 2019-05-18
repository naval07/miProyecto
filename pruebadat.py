from tkinter import ttk
import tkinter as tk

class WinDatos(ttk.Frame):
    global dataBases
    # Inicia el registro con la ultima plantilla igresada por defecto
    def __init__(self, base = 0):
        self.base = base
        self.window = tk.Tk()
        super().__init__(self.window)
        self.window.title("Crear Plantilla")
        # Variables
        self.n = tk.StringVar() # campo llenado en Nombre
        self.d = tk.StringVar() # campo llenado en dorsal
        self.p = tk.IntVar() # opcion escogida del radiobutton
        # Crea Frame y LabelFrame
        frameP = tk.Frame(self.window)
        frameP.pack()
        frame = tk.LabelFrame(frameP, text = "Datos del jugador")
        frame.pack()
        # Input Nombre
        tk.Label(frame, text = "Nombre: ").grid(row = 0, column = 0)
        self.name = tk.Entry(frame, textvariable = self.n)
        self.name.grid(row = 0, column = 1, sticky = "nw")
        # Input Dorsal
        tk.Label(frame, text = "Dorsal: ").grid(row = 1, column = 0)
        self.dorsal = tk.Entry(frame, textvariable = self.d)
        self.dorsal.grid(row = 1, column = 1, sticky = "nw")
        # Input Posicion
        tk.Label(frame, text = "Posicion: ").grid(row = 2, column = 0)
        arq = tk.Radiobutton(frame, text = "Arquero", variable = self.p, value = 1).grid(row = 2, column = 1, sticky= "nw", pady = 5)
        defen = tk.Radiobutton(frame, text = "Defensa", variable = self.p, value = 2).grid(row = 3, column = 1, sticky= "nw", pady = 5)
        medio = tk.Radiobutton(frame, text = "Mediocampista", variable = self.p, value = 3).grid(row = 4, column = 1, sticky= "nw", pady = 5)
        dela = tk.Radiobutton(frame, text = "Delantero", variable = self.p, value = 4).grid(row = 5, column = 1, sticky= "nw", pady = 5)
        # Boton Guardar
        tk.Button(frame, text = "Agregar", command = self.agregar).grid(row = 6, column = 1, sticky = "nsew")
        #Tabla
        self.tree = ttk.Treeview(frameP, height = 2 , columns = 4, padding = 2)
    #    self.tree.config(columns = ("#1","#2","#3","#4","#5","#6"))
        self.tree["columns"] = ("#1","#2","#3","#4","#5","#6")
        #self.tree.grid(row = 5 , column = 0 , columnspan = 5, sticky =  "nw" , pady = 5)
        self.tree.pack()
        self.tree.column("#0", width = 50, minwidth = 50, stretch = True)
        #print(self.tree)
        #self.tree.heading( "#0" , text = "Dorsal",anchor = "center")
        self.tree.heading( "#0" , text = "Dorsal",anchor = "center")
        self.tree.heading( "#1" , text = "Nombre" , anchor = "center")
        self.tree.heading( "#2" , text = "Apellido" ,anchor = "center")
        self.tree.heading( "#3" , text = "Posicion", anchor = "center")
        self.tree.heading( "#4" , text = "Pases buenos " , anchor = "center")
        self.tree.heading( "#5" , text = "Pases Totales" , anchor = "center")
        self.tree.heading( "#6" , text = "Efectividad" , anchor = "center")

        self.window.mainloop()

    def agregar(self):
	    print("Nombre:  " + "\t" + self.name.get())
	    #print("Apodo:  " + "\t" + a.get())
	    print("Dorsal:  " + "\t" + self.dorsal.get())
	    if self.p.get() == 1:
	        print("Posicion:" + "\t" + "Arquero")
	    elif self.p.get() == 2:
	        print("Posicion:" + "\t" + "Defensa")
	    elif self.p.get() == 3:
	        print("Posicion:" + "\t" + "Mediocampista")
	    else:
	        print("Posicion:" + "\t" + "Delantero")

regis = WinDatos()
