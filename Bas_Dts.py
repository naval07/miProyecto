
from tkinter import ttk
from tkinter import Tk
from tkinter import *


import os
import sqlite3
#import pyodbc

class Registro:

	db_nm = "DatosCreate.db"
	schema_filename  = "Crear_schema.sql"



	def __init__ (self, window):
		self.wind = window
		self.wind.title("Registro de datos")
	#Crear un Frame
		frame = LabelFrame(self.wind , text = "Jugadores")
		frame.grid(row = 0 , column = 0 , columnspan = 6 , pady = 40)
		#frame.pack()


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
	#Inician siendo 0 porque mas adelante se van agregando los datos
		self.PasesBuenos = 0
		self.PasesTotales=0
		self.Efectividad = 0
		self.x = 0


	#Boton para guardar datos
		ttk.Button(frame , text = "Guardar" , command = self.add_Registro).grid(row = 4 , columnspan = 2, sticky = W + E )
	#Salida de un mensage
		self.message = Label(text = "" , fg = "red")
		self.message.grid(row = 4 , column = 0 , columnspan = 2 , sticky = W + E)


	#Tabla
		self.tree = ttk.Treeview(height = 10 , columns = 4)
		self.tree["columns"] = ("#1","#2","#3","#4","#5","#6")
		self.tree.grid(row = 5 , column = 0 , columnspan = 5, sticky =  W + E , pady = 20)
		self.tree.column("#0", width = 250 ,  minwidth = 50, stretch = True)
		print(self.tree)
		self.tree.heading( "#0" , text = "Nombre y Apellido",anchor = CENTER)
		self.tree.heading( "#1" , text = "Dorsal" , anchor = CENTER )
		self.tree.heading( "#2" , text = "Posicion", anchor = CENTER )
		self.tree.heading( "#3" , text = "Pases buenos " , anchor = CENTER)
		self.tree.heading( "#4" , text = "Pases Totales" , anchor = CENTER)
		self.tree.heading( "#5" , text = "Efectividad" , anchor = CENTER)
		self.tree.column("#1" ,width = 50 , minwidth = 50 , stretch = True)
		self.tree.column("#2" ,width = 200 , minwidth = 50 , stretch = True)
		self.tree.column("#3" ,width = 200 , minwidth = 50 , stretch = True)
		self.tree.column("#4" ,width = 200 , minwidth = 50 , stretch = True)
		self.tree.column("#5" ,width = 200 , minwidth = 50 , stretch = True)

		#self.Conexion() #Se usa el self.Conexion para crear la tabla ya de una vez que diga existente podremos comenzar a crear la tabla

		#Botones de Elimincion y Edicion
		ttk.Button(text = "Eliminar" , command = self.delete_Jugador).grid(row = 6 , column = 0 , sticky = W + E)
		ttk.Button(text = "Editar" , command = self.edit_registro).grid(row = 6 , column = 1 , sticky = W + E)
		ttk.Button(text = "Pases Totales" , command = self.PasesTot).grid(row = 6 , column = 2 , sticky = W + E)

		#Para agregar los datos
		self.get_Registro()


	#Crear La Conexion para empezar a crear la base de datos
	def Conexion(self ):
		db_is_new = not os.path.exists(self.db_nm)
		Cnci = sqlite3.connect(self.db_nm)
		if db_is_new:
		    print("Necesito crear")
		else:
		    print("Database exist ")

		conn.close()

	def run_query (self , query , parameters= ()):
		with sqlite3.connect(self.db_nm) as conn:
			cursor = conn.cursor()
			result = cursor.execute(query , parameters)
			conn.commit()
		return result


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

	def Validation (self) :
		if len(self.Dor.get() )!= 0:
			if len(self.name.get() ) !=0 :
				if len ( self.pos.get() ) !=0 :
					return ("({0} , {1} ,{2} )").format(self.Dor.get(),self.name.get(),self.pos.get())

	def add_Registro(self) :
		if self.Validation():
			query = "INSERT INTO task VALUES (NULL , ? ,?,?,?,?,?)"
			parameters = (self.Dor.get(),self.name.get(),self.pos.get(),self.PasesBuenos,self.PasesTo.get(),self.Efectividad)
			self.run_query(query , parameters)
			self.message["text"]="El jugador {} a sido añadido exitosamente".format(self.name.get())
			self.name.delete(0 ,"end")
			self.pos.delete(0,"end")
			self.Dor.delete(0,"end")

		else:
			self.message["text"]="Se requiere llenar todos los espacios en blanco "
		self.get_Registro()

	def delete_Jugador(self):
		self.message["text"]=""
		try:
			self.tree.item(self.tree.selection())["text"][5]
		except IndexError as e:
			self.message["text"]="Elija el jugador que desea Eliminar"
			return
		self.message["text"] = ""
		Nombres = self.tree.item(self.tree.selection())["text"]
		#print(Nombres)
		query = "DELETE FROM task WHERE Nombres = ? "
		self.run_query(query , (Nombres ,  ))
		self.message["text"]= " El jugador {0} a sido eliminado de tu base de datos".format(Nombres)
		self.get_Registro()

	def edit_registro(self):
		self.message["text"]=""
		try:
			self.tree.item(self.tree.selection())["text"][0]
		except IndexError as e:
			self.message["text"]="Elija el jugador que desea Editar"
			return
		Nombre = self.tree.item(self.tree.selection())["text"]
		old_Dorsal= self.tree.item(self.tree.selection())["values"][0]
		old_Posicion= self.tree.item(self.tree.selection())["values"][1]
		#Crear una ventana dentro de esta ventana para poder de alli editar los datos
		self.edit_wid = Toplevel() #Se usa para crear una ventana dentro de otra ventana
		self.edit_widtitle = "Editar Jugador"
		#Nombre Antiguo
		Label(self.edit_wid , text = "Nombre Actual: " ).grid(row = 0 , column =1)
		Entry(self.edit_wid , textvariable = StringVar(self.edit_wid, value = Nombre), state = "readonly").grid(row = 0 , column = 2)

		#Nombre New
		Label(self.edit_wid , text = "Nuevo Nombre: ").grid(row = 1 , column = 1)
		New_name = Entry(self.edit_wid)
		New_name.grid(row = 1 , column = 2 )

		#Antiguo numero de Dorsal
		Label(self.edit_wid , text = "Dorsal Actual:").grid(row = 2 , column = 1)
		Entry(self.edit_wid, textvariable = StringVar (self.edit_wid , value = old_Dorsal), state = "readonly").grid(row = 2 , column = 2)

		#Nuevo Numero de la Dorsal
		Label(self.edit_wid , text = "Nueva Dorsal:").grid(row = 3 , column = 1)
		New_Dorsal = Entry(self.edit_wid)
		New_Dorsal.grid(row = 3 , column = 2)

		#Antigua posicion
		Label(self.edit_wid , text = "Posicion Actual:").grid(row = 4 , column = 1)
		Entry(self.edit_wid , textvariable = StringVar(self.edit_wid , value = old_Posicion), state = "readonly").grid(row = 4 , column = 2)

		#Nueva Posicionrror
		Label(self.edit_wid , text = "Nueva Posicion:").grid(row = 5 , column = 1)
		New_Posicion = Entry(self.edit_wid)
		New_Posicion.grid(row = 5 , column = 2)

		#Boton para guardar o actualizar  los cambios

		Button(self.edit_wid , text = "Actualizar" , command = lambda: self.edit_record(New_name.get(),Nombre , New_Dorsal.get(), old_Dorsal , New_Posicion.get(), old_Posicion)).grid(row=6 , column = 2 , sticky = W)

	def edit_record (self , New_name , Nombre , New_Dorsal , old_Dorsal ,New_Posicion , old_Posicion):
		query = "UPDATE task set Nombres = ? , Dorsal = ? , Posicion = ? WHERE Nombres = ? AND Dorsal = ? AND Posicion = ?"
		paramenters = ( New_name ,  New_Dorsal ,New_Posicion , Nombre , old_Dorsal , old_Posicion )
		self.run_query(query , paramenters)

		self.edit_wid.destroy()
		self.message["text"] = "Se actualizo el jugador {} correctamente".format(New_name)
		self.get_Registro()

	def PasesTot (self):
		self.message["text"]=""
		try:
			self.tree.item(self.tree.selection())["text"][0]
		except IndexError as e:
			self.message["text"]="Elija el jugador que dea añadirle sus pases"
			return
		Nombre = self.tree.item(self.tree.selection())["text"]
		old_PasesTot = self.tree.item(self.tree.selection())["values"][2]
		old_PasesBuenos= self.tree.item(self.tree.selection())["values"][3]
		old_Efectividad= self.tree.item(self.tree.selection())["values"][4]
		#Crear una ventana dentro de esta ventana para poder de alli editar los datos
		self.Pases_wid = Toplevel() #Se usa para crear una ventana dentro de otra ventana
		self.Pases_widtitle = "Añadir Puntos de el jugador"
		#Pases Totales Antiguo
		Label(self.Pases_wid , text = "Pasos Totales Actual: " ).grid(row = 0 , column =1)
		Entry(self.Pases_wid , textvariable = StringVar(self.Pases_wid, value = old_PasesTot), state = "readonly").grid(row = 0 , column = 2)

		#Pases Totales New
		Label(self.Pases_wid, text = "Nuevos Pases ").grid(row = 1 , column = 1)
		New_PasT = Entry(self.Pases_wid)
		New_PasT.grid(row = 1 , column = 2 )

		#Antiguo numero de Dorsal
		Label(self.Pases_wid , text = "Pases Buenos Actual:").grid(row = 2 , column = 1)
		Entry(self.Pases_wid, textvariable = StringVar (self.Pases_wid, value = old_PasesBuenos), state = "readonly").grid(row = 2 , column = 2)

		#Nuevo Numero de los pases Buenos
		Label(self.Pases_wid , text = "Nueva Pases Buenos:").grid(row = 3 , column = 1)
		New_PassB = Entry(self.Pases_wid)
		New_PassB.grid(row = 3 , column = 2)

		#Antigua posicion
		Label(self.Pases_wid , text = "Efectividad Actual:").grid(row = 4 , column = 1)
		Entry(self.Pases_wid, textvariable = StringVar(self.Pases_wid , value = old_Efectividad), state = "readonly").grid(row = 4 , column = 2)

		#Nueva Posicionrror
		Label(self.Pases_wid , text = "Nueva Efectivadad:").grid(row = 5 , column = 1)
		New_Efectividad = Entry(self.Pases_wid)
		New_Efectividad.grid(row = 5 , column = 2)

		#Boton para guardar o actualizar  los cambios

		Button(self.Pases_wid , text = "Actualizar" , command = lambda: self.Pass_Record(New_PasT.get(),old_PasesTot , New_PassB.get(), old_PasesBuenos , New_Efectividad.get(), old_Efectividad)).grid(row=6 , column = 2 , sticky = W + E)

	def Pass_Record (self , New_PasT , old_PasesTot , New_PassB , old_PasesBuenos ,New_Efectividad , old_Efectividad):
		query = "UPDATE task set PasesTotales = ? , PasesBuenos = ? , Efectividad = ? WHERE PasesTotales = ? AND PasesBuenos = ? AND Efectividad = ?"
		paramenters = ( New_PasT ,  New_PassB ,New_Efectividad , old_PasesTot , old_PasesBuenos, old_Efectividad )
		self.run_query(query , paramenters)
		self.Pases_wid.destroy()
		self.message["text"] = "Se actualizaron los pases del jugador  {} correctamente".format(self.name)
		self.get_Registro()



if __name__ == "__main__":
	window = Tk ()
	aplication = Registro(window)
	window.mainloop()
