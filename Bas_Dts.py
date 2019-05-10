from tkinter import ttk
from tkinter import Tk
from tkinter import *


import sqlite3

class Registro:

	db_nm = "DataBase.db" 

	def __init__ (self,window):
		self.wind = window
		self.wind.title("Registro de datos")
	#Crear un Frame
		frame = LabelFrame(self.wind , text = "Jugadores")
		frame.grid(row = 0 , column = 0 , columnspan = 6 , pady = 20)

	# Nombres de los jugadores Input
		Label(frame , text = "Nombre y Apellido:" ).grid(row = 1, column = 0)
		self.name = Entry(frame)
		self.name.focus()
		self.name.grid(row = 1 , column = 1, sticky = "nw" , pady = 5)
	# Dorsal input
		Label (frame , text = "Dorsal:").grid(row = 2 , column = 0)
		self.Dor = Entry(frame)
		self.Dor.grid(row = 2 , column = 1, sticky = "nw" , pady = 5)
	#Posicion inpuy
		Label (frame , text = "Posicion:").grid(row = 3 , column = 0 )
		self.pos = Entry(frame)
		self.pos.grid(row = 3 , column = 1, sticky = "nw" , pady = 5)
	#Boton para guardar datos
		ttk.Button(frame , text = "Guardar").grid(row = 4 , columnspan = 2, sticky = W + E ) 
	#Tabla
		self.tree = ttk.Treeview(height = 20 , columns = 4)
		self.tree["columns"] = ("#1","#2","#3","#4","#5")
		self.tree.grid(row = 5 , column = 0 , columnspan = 5, sticky =  W + E , pady = 20)
		self.tree.column("#0",width = 150 , minwidth = 150, stretch = True)
		print(self.tree)
		self.tree.heading("#0" , text = "Dorsal" , anchor = CENTER )
		self.tree.heading( "#1" , text = "Jugadores" ,anchor = CENTER)
		self.tree.heading( "#2" , text = "Posicion", anchor = CENTER )
		self.tree.heading( "#3" , text = "Pases Buenos" , anchor = CENTER)
		self.tree.heading( "#4" , text = "Total de pases" , anchor = CENTER)
		self.tree.heading( "#5" , text = "Efectividad" , anchor = CENTER)
	

	#def Conexion 
	
		



if __name__ == "__main__":
	window = Tk ()
	aplication = Registro(window)
	window.mainloop()