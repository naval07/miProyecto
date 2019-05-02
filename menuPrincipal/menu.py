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
fondo = tk.PhotoImage(file = "fondomenu01.gif")
fondomenu = tk.Label(raiz, image = fondo)
fondomenu.pack()
##------------------------------- Botones -------------------
tk.Button(raiz, bd = 1, height = 2, width = 10, activebackground = "lightblue", bg = "green", text = "Plantilla").place(x = 550, y = 110)
tk.Button(raiz, bd = 1, height = 2, width = 10, activebackground = "lightblue", bg = "green", text = "Alineacion").place(x = 350, y = 110)
tk.Button(raiz, bd = 1, height = 2, width = 10, activebackground = "lightblue", bg = "green", text = "Empezar").place(x = 150, y = 110)
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
