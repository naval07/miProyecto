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
archivo = tk.Menu(barramenu)
opciones = tk.Menu(barramenu)
ayuda = tk.Menu(barramenu)
#---- cascada -----
barramenu.add_cascade(label = "Archivo", menu = archivo)
barramenu.add_cascade(label = "Opciones", menu = opciones)
barramenu.add_cascade(label = "Ayuda", menu = ayuda)

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
tk.Button(raiz, image = bgAlineacion, text = "Alineacion").place(x = 312, y = 107)
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
