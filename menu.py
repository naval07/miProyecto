import sqlite3
from tkinter import ttk
import tkinter as tk

# Bases de Datos (pantillas)
dataBases = [] # En esta lista se van a guardar los nombres de las plantillas para crear la base de datos correspondiente de cada una
# Clase Tabla
class Tabla(ttk.Frame):
    global dataBases # Permite usar la variable global dataBases

    def __init__(self, frame, bool = False, database = 0):
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



# Clase WinDatos
class WinDatos(ttk.Frame):
    global dataBases
    # Inicia el registro con la ultima plantilla igresada por defecto
    def __init__(self, title, tabla = False, base = 0):
        self.title = title # Titulo de la ventana
        self.tabla = tabla # Tipo de tabla
        self.base = base # base de datos
        self.window = tk.Tk() # abre la raiz
        super().__init__(self.window)
        self.window.title(title)
        # Variables
        self.n = tk.StringVar() # campo llenado en Nombre
        self.d = tk.StringVar() # campo llenado en dorsal
        self.p = tk.IntVar() # opcion escogida del radiobutton
        # Crea Frame y LabelFrame
        frameP = tk.Frame(self.window) # crea el frame principal
        frameP.pack() # empaca o almacena el frame principal en la raiz
        frame = tk.LabelFrame(frameP, text = "Datos del jugador") # crea un LabelFrame o (sub frame) y lo hubica en el frame princial
        frame.pack() # empaca o almacena el LabelFrame en el frame principal
        # Input Nombre
        tk.Label(frame, text = "Nombre: ").grid(row = 0, column = 0) # crea label "Nombre: " y lo hubica en el LabelFrame o (subframe)
        self.name = tk.Entry(frame, textvariable = self.n) # crea la entrada de texto para Nombre
        self.name.grid(row = 0, column = 1, sticky = "nw") # hubica la entrada de Nombre
        # Input Dorsal
        tk.Label(frame, text = "Dorsal: ").grid(row = 1, column = 0) # crea label "Dorsal: " y lo hubica en el LabelFrame o (subframe)
        self.dorsal = tk.Entry(frame, textvariable = self.d) # crea la entrada de texto para Dorsal
        self.dorsal.grid(row = 1, column = 1, sticky = "nw") # hubica la entrada Dorsal
        # Input Posicion
        tk.Label(frame, text = "Posicion: ").grid(row = 2, column = 0) # crea label "Posicion: " y lo hubica en el LabelFrame o (subframe)
        arq = tk.Radiobutton(frame, text = "Arquero", variable = self.p, value = 1).grid(row = 2, column = 1, sticky= "nw", pady = 5) # crea el radiobutton u opcion de "Arquero "
        defen = tk.Radiobutton(frame, text = "Defensa", variable = self.p, value = 2).grid(row = 3, column = 1, sticky= "nw", pady = 5) # crea el radiobutton u opcion de "Defensa "
        medio = tk.Radiobutton(frame, text = "Mediocampista", variable = self.p, value = 3).grid(row = 4, column = 1, sticky= "nw", pady = 5) # crea el radiobutton u opcion de "Mediocampista "
        dela = tk.Radiobutton(frame, text = "Delantero", variable = self.p, value = 4).grid(row = 5, column = 1, sticky= "nw", pady = 5) # crea el radiobutton u opcion de "Delantero "
        # Boton Guardar
        tk.Button(frame, text = "Agregar", command = self.agregar).grid(row = 6, column = 1, sticky = "nsew") # Crea el boton para "guardar" los datos ingresados (Que por ahora solo los imprime)

        if self.tabla == True: # se crea la tabla
            tabla = Tabla(frameP) # se hubica la tabla en el frame principal

        self.window.mainloop()

    def agregar(self): # comando para el boton Agregar (el cual por ahora solo imprime) los datos ingresados
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
# -------------------- funciones -----------------
# Cerrar la ventana
def close(e):
    raiz.destroy()

#Ventana para crear la plantilla
def crearPlantilla():

    def crearData(data, window): # funcion para agregar la base de datos respectiva a la lista global de plantillas o bases de datos
        global dataBases
        dataBases.append(data.get() + ".db") # se concatena con el ".db" para que se pueda crear su base de datos
        print(dataBases) # imprime la lista de bases de datos temporal solo para comprobar que la funcion sirve
        window.destroy() # cierra la ventana
        winDat = WinDatos(title = "Crear Plantilla", tabla = True) # abre la una ventana WinDatos para ingresar los datos de los jugadores de la plantilla


    win = tk.Tk() # crea la raiz
    win.title("Crear plantilla")
    frame = tk.Frame(win) # crea un frame y lo hubica en la raiz
    frame.grid(row = 0, column = 0)
    tk.Label(frame, text = "Ingrese el nombre").grid(row = 0, column = 0)
    tk.Label(frame, text = "de su plantilla: ").grid(row = 1, column = 0)
    d = tk.IntVar() # se establece el tipo de variable
    data = tk.Entry(frame, textvariable = d) # crea un Entry, lo hubica en el frame, y asigna el tipo de variable que recibe (en este caso es variable int ya que d = IntVar)
    data.grid(row = 1, column = 1)
    imprimir = tk.Button(frame, text = "Crear", command = lambda: crearData(data, win)).grid(row = 2, column = 0) #crea el boton de imprimir
    win.mainloop()

# Ventana crear jugador
def agregarJugador(): # incluir la base dedatos a modificar
    win = WinDatos(title = "Agregar Jugador", tabla = False) # crea un objeto WinDatos

# Ventana editar jugador
#def editarJugador():

""" acá empieza el codigo principal """

## ----------------------------- Raiz ---------------------
raiz = tk.Tk() # crea la raiz

raiz.title("Dayel: Para entrenadores")
raiz.geometry("750x450") # define el tamaño de la pestana
raiz.resizable(width="False", height="False") # hace que el tamaño de la ventana sea igual siempre
## ----------------------------- Menu ----------------------
barramenu = tk.Menu(raiz) # crea la barra menu (donde van las opciones "Plantilla" "opciones" "Ayuda")
raiz.config(menu = barramenu) # hubica la barramenu en la raiz
# ---- pestanas menu ---------------  ## Crea las pestanitas que va a tener el barramenu
archivo = tk.Menu(barramenu, tearoff = 0)
plantilla = tk.Menu(barramenu, tearoff = 0)
opciones = tk.Menu(barramenu, tearoff = 0)
ayuda = tk.Menu(barramenu, tearoff = 0)
#---- cascada -----   ## "hace visible" las pestanitas creadas
barramenu.add_cascade(label = "Plantilla", menu = plantilla)
barramenu.add_cascade(label = "Opciones", menu = opciones)
barramenu.add_cascade(label = "Ayuda", menu = ayuda)
#- Plantilla - # agrega las opciones a mostrar cuando se seleciona una pestana
plantilla.add_command(label = "Crear plantilla", command = crearPlantilla) # cuando se da click en "Crear plantilla" se ejecuta la funcion crearPlantilla (revisa la linea 98)
plantilla.add_command(label = "Nuevo jugador", command = agregarJugador) # cuando se da click en "Nuevo Jugador" se ejecuta la funcion agregarJugador (linea 121)
plantilla.add_command(label = "Editar jugador/es") # falta crear el comando a ejecutar cuando se creckee "Editar jugador/es"
#- Opciones -
opciones.add_command(label = "Agregar tipo de alineamiento")
opciones.add_command(label = "Borrar tipo de alineamiento")
#- Ayuda -
ayuda.add_command(label = "Datos de la aplicacion")
ayuda.add_command(label = "Datos de creadores")
##------------------------------- Imagenes ------------------
#textofoto = tk.PhotoImage(file = "textlogo.png")
#textologo = tk.Label(raiz, image = textofoto)
bgEmpezar = tk.PhotoImage(file = "empezar.png") # crea la variable que contiene el fondo del boton "Empezar"
fondo = tk.PhotoImage(file = "fondomenu001.png") # crea la variable que contiene el fondo de la raiz
fondomenu = tk.Label(raiz, image = fondo) # asigna el fondo de la raiz
fondomenu.pack()
##------------------------------- Botones -------------------)
tk.Button(raiz, text = "Empezar", image = bgEmpezar).place(x = 265, y = 111)
#textologo.place(x=100, y=200)

raiz.bind('<Control-q>', close) # mediante este metodo, se ejecuta la funcion close al opimir Control+q (solo en la raiz)
raiz.focus_set() # recibe las teclas pulsadas al tener la riz abierta

tk.mainloop()
