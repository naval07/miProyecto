import sqlite3
from tkinter import ttk
import tkinter as tk
import classTablWD as tdw
import classAli as al
import classApp as app

# Bases de Datos (pantillas)
dataBases = [] # En esta lista se van a guardar los nombres de las plantillas para crear la base de datos correspondiente de cada una
# -------------------- funciones -----------------
# Cerrar la ventana
def close(e):
    raiz.destroy()

def crearData(data, window):# funcion para agregar la base de datos respectiva a la lista global de plantillas o bases de datos
    global jugadores
    global dataBases

    dataBases.append(data.get() + ".db") # se concatena con el ".db" para que se pueda crear su base de datos
    print(dataBases) # imprime la lista de bases de datos temporal solo para comprobar que la funcion sirve
    window.destroy() # cierra la ventana

    win = tk.Tk()
    frameP = tk.LabelFrame(win)
    frameP.pack()
    winDat = tdw.WinDatos(win, title = "Crear Plantilla", frameP = frameP, database = jugadores, tabla = True) # abre la una ventana WinDatos para ingresar los datos de los jugadores de la plantilla
    win.mainloop()

def openWinData():
    winDat = twd.WinDatos(title = "Crear Plantilla")

#Ventana para crear la plantilla
def crearPlantilla():
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
def agregarJugador():# incluir la base dedatos a modificar
    global jugadores
    win = tk.Tk()
    frameP = tk.Frame(win)
    frameP.pack()
    wind = tdw.WinDatos(win, "Agregar Jugador", frameP, database = jugadores, destroy = True) # crea un objeto WinDatos
    win.mainloop()

# Ventana editar jugador
def editarJugador():
    global jugadores
    win = tk.Tk()
    frameP = tk.Frame(win)
    frameP.pack()
    wind = tdw.WinDatos(win, "Editar Jugador", frameP, database = jugadores, tabla = True)
    win.mainloop()

# Ventana ver alineaciones
def verAlineaciones():
    global alineaciones
    win = tk.Tk()
    frameP = tk.Frame(win)
    frameP.pack()
    wind = al.WinAlineamiento(win, "Alineaciones", frameP, alineaciones, see = True)
    win.mainloop()
# Ventana agregar alineamiento
def agregarAlineacion():
    global alineaciones
    win = tk.Tk()
    frameP = tk.Frame(win)
    frameP.pack()
    wind = al.WinAlineamiento(win, "Agregar Alineacion", frameP, alineaciones, add = True)
    win.mainloop()

# Ventana borrar alineacion
def borrarAlineacion():
    global alineaciones
    win = tk.Tk()
    frameP = tk.Frame(win)
    frameP.pack()
    wind = al.WinAlineamiento(win, "Borrar Alineacion", frameP, alineaciones, dele = True)
    win.mainloop()
# Ventana app
def Empezar():
    global alineaciones
    App = app.App("fondoapp.png", alineaciones)


"""Variables Globales"""
jugadores = []
alineaciones = []
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
plantilla.add_command(label = "Editar jugador", command = editarJugador) # falta crear el comando a ejecutar cuando se creckee "Editar jugador/es"
#- Opciones -
opciones.add_command(label = "Ver alineaciones", command = verAlineaciones)
opciones.add_command(label = "Agregar tipo de alineacion", command = agregarAlineacion)
opciones.add_command(label = "Borrar tipo de alineacion", command = borrarAlineacion)
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
tk.Button(raiz, image = bgEmpezar, command = Empezar).place(x = 265, y = 111)
#textologo.place(x=100, y=200)

raiz.bind('<Control-q>', close) # mediante este metodo, se ejecuta la funcion close al opimir Control+q (solo en la raiz)
raiz.focus_set() # recibe las teclas pulsadas al tener la riz abierta

tk.mainloop()
