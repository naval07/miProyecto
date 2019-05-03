import tkinter as tk
## ----------------------------- Raiz ---------------------
raiz = tk.Tk()
raiz.title("Dayel: Para entrenadores")
raiz.geometry("750x450")
raiz.resizable(width="False", height="False")
## ----------------------------- Menu ----------------------
barramenu = tk.Menu(raiz)
raiz.config(menu = barramenu)
#---- pestañas menu ---------------
archivo = tk.Menu(barramenu, tearoff = 0)
opciones = tk.Menu(barramenu, tearoff = 0)
ayuda = tk.Menu(barramenu, tearoff = 0)
#---- cascada -----
barramenu.add_cascade(label = "Archivo", menu = archivo)
barramenu.add_cascade(label = "Opciones", menu = opciones)
barramenu.add_cascade(label = "Ayuda", menu = ayuda)
#-- contenidos --
#- Archivo -
archivo.add_command(label = "Crear plantilla")
archivo.add_command(label = "Nuevo entrenador")
archivo.add_command(label = "Nuevo asistente técnico")
archivo.add_command(label = "Nuevo jugador")
#- Opciones -
opciones.add_command(label = "Editar jugador/es")
opciones.add_command(label = "Editar entrenadores")
opciones.add_command(label = "Editar asistentes")
opciones.add_command(label = "Agregar alineamiento")
#- Ayuda -
ayuda.add_command(label = "Datos de la aplicacion")
ayuda.add_command(label = "Datos de creadores")
##------------------------------- Imagenes ------------------
textofoto = tk.PhotoImage(file = "textlogo.png")
textologo = tk.Label(raiz, image = textofoto)
bgEmpezar = tk.PhotoImage(file = "Empezar.png")
bgPlantilla = tk.PhotoImage(file = "Plantilla.png")
bgAlineacion = tk.PhotoImage(file = "Alineacion.png")
fondo = tk.PhotoImage(file = "fondomenu01.png")
fondomenu = tk.Label(raiz, image = fondo)
fondomenu.pack()
##------------------------------- Botones -------------------
tk.Button(raiz, image = bgPlantilla, text = "Plantilla").place(x = 480, y = 107)
tk.Button(raiz, image = bgAlineacion, text = "Alineacion").place(x = 312, y = 105)
tk.Button(raiz, text = "Empezar", image = bgEmpezar).place(x = 145, y = 107)
textologo.place(x=100, y=200)


tk.mainloop()

#------------------------------ Fondo ---------------------
#fondoframe = tk.Frame()
##fondoframe.pack(fill = "both", expand="True")
#fondoframe.config(bg = "blue")

#texto = tk.PhotoImage(file = "textlogo.png")
##tk.Label(fondoframe, image = texto).pack()
#fond = tk.Label(raiz, image = fondo)
#fond.grid(row = 0, column = 0)
#text = tk.Label(raiz, image = texto)
#text.grid(row = 0, column = 0)
