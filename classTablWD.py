from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

class Tabla(ttk.Frame):
    global dataBases # Permite usar la variable global dataBases

    def __init__(self, frame, database = None, bool = False):

        self.bool = bool
        self.frame = frame # frame o ventana principal
        self.database = database # Base de datos correspondiente a la plantilla
        if self.bool == True: # si bool es verdadero entonces permite ver la totalidad de los datos
            self.tree = ttk.Treeview(self.frame, height = 20 , columns = 4)
            self.tree["columns"] = ("#1","#2","#3","#4","#5","#6")
            self.tree.heading( "#0" , text = "Dorsal",anchor = "center")
            self.tree.heading( "#1" , text = "Nombre" , anchor = "center")
            self.tree.heading( "#2" , text = "Apellido" ,anchor = "center")
            self.tree.heading( "#3" , text = "Posicion", anchor = "center")
            self.tree.heading( "#4" , text = "Pases buenos " , anchor = "center")
            self.tree.heading( "#5" , text = "Pases Totales" , anchor = "center")
            self.tree.heading( "#6" , text = "Efectividad" , anchor = "center")
        else: # si bool es falso, solo deja ver los datos basicos del jugador
            self.tree = ttk.Treeview(self.frame, height = 20 , columns = 2)
            self.tree["columns"] = ("#1","#2","#3")
            self.tree.heading( "#0" , text = "Dorsal",anchor = "center")
            self.tree.heading( "#1" , text = "Nombre" , anchor = "center")
            self.tree.heading( "#2" , text = "Apellido" ,anchor = "center")
            self.tree.heading( "#3" , text = "Posicion", anchor = "center")

        self.tree.pack() # introduce la tabla en el frame o ventana principal
        self.tree.column("#0",width = 50 , minwidth = 50, stretch = True)

        """self.get_Registro()

    def get_Registro(self):
        #Limpiar Datos de la tabla
        records = self.tree.get_children()
        for elemnts in records:
            self.tree.delete(elemnts)
        #Consultar Datos
        query = 'SELECT * FROM task  ORDER BY Nombres DESC'
        db_rows = self.run_query(query)
        #Rellenar datos
        for row in db_rows:
            self.tree.insert("",0 , text = (row [2]), values = (row [1], row[3] , row[4] ,row[5] ,row[6] ) )

    def agregarDest(self):
        if self.Validation():
            query = "INSERT INTO task VALUES (NULL , ? ,?,?,?,?,?)"
            parameters = (self.dorsal.get(),self.name.get(),self.p.get(),self.PasesBuenos,self.PasesTotales,self.Efectividad)
            self.run_query(query , parameters)
            self.tk.message["text"]="El jugador {} a sido añadido exitosamente".format(self.name.get())
            self.name.delete(0 ,"end")
            self.pos.delete(0,"end")
            self.Dor.delete(0,"end")
        else:
            self.tk.message["text"]="Se requiere llenar todos los espacios en blanco "
        self.get_Registro()
"""
class WinDatos(ttk.Frame):
    # Inicia el registro con la ultima plantilla igresada por defecto
    def __init__(self, window, title, frameP, database = None, destroy = False, tabla = False):
        self.dest = destroy
        self.options = ["Arquero", "Defensa", "Mediocampista", "Delantero"] # list
        self.frameP = frameP
        self.title = title
        self.tabla = tabla
        self.base = database
        self.window = window
        super().__init__(self.window)
        self.window.title(title)
        # Crea Frame y LabelFrame
        frame = self.frameP
        # Variables
        self.n = tk.StringVar() # campo llenado en Nombre
        self.d = tk.StringVar() # campo llenado en dorsal
        self.p = tk.StringVar(frame)# opcion escogida del dropdownMenu
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

        self.dropdowMenu = tk.OptionMenu(frame, self.p, self.options[0], self.options[1], self.options[2], self.options[3])
        self.p.set(self.options[0])
        self.dropdowMenu.grid(row = 2, column = 1)
        # Boton Guardar
        if self.dest == False:
            tk.Button(frame, text = "Agregar", command = self.agregar).grid(row = 6, column = 1, sticky = "nsew")
        if self.dest == True:
            tk.Button(frame, text = "Agregar", command = self.agregarDest).grid(row = 6, column = 1, sticky = "nsew")
        #Tabla
        if self.tabla == True:
            tabla = Tabla(self.window)

    def setPos(self, var):
        var.set(self.options[0])

    def agregarDest(self):
        if self.name.get() in self.base:
            msj = "El jugador " + self.name.get() + " Ya existe"
            messagebox.showerror("Error", msj)
        else:
            self.base += [self.name.get()]
            print("Dorsal:  \t" + self.dorsal.get())
            print("Posicion: \t" + self.p.get())
            self.window.destroy()
        for q in self.base:
            c = 0
            if self.name.get() == q:
                msj = "El jugador " + self.name.get() + " Ya existe"
                messagebox.showerror("Error", msj)
            else:
                self.base += [self.name.get()]
                break


    def agregar(self):
        if self.name.get() in self.base:
            msj = "El jugador " + self.name.get() + " Ya existe"
            messagebox.showerror("Error", msj)
        else:
            self.base += [self.name.get()]
            print("Dorsal:  \t" + self.dorsal.get())
            print("Posicion: \t" + self.p.get())
