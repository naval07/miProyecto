import pandas as pd


l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
Datos = {}
cstN = "Jugadores"
cstA = "Apellido"
cstDor = "Dorsal"
cstPB = " Pases buenos"
cst_Ef = "Efectividad"

#def Pases_Buenos (n):
#    count += 0
#    if n 
    







while True : 
    a = input("Quieres Continuar")#Escribir si con las dos minusculas
    if a == "si":
        b = input ("Nombre de un jugador") #El nombre que ingrese debe considir con los demas datos que pidan 
        i = input ("Apellido de el jugador")
        bi = input ("Numero Dorsal ")
        bis = input ( "Numero de Puntajes buenos ")
        biss = input ("Efectividad del dia de hoy") #Ingresar la efectividad en porcentaje
        
        l1.append(b)
        l5.append(i)
        l2.append(bi)
        l3.append(bis)
        l4.append(biss)
    else:
        break 



Datos[cstN]=l1
Datos[cstA]=l5
Datos[cstDor]=l2
Datos[cstPB]=l3
Datos[cst_Ef]=l4
df= pd.DataFrame(Datos)             

Base_Datos = pd.("BaseDato)              



#print(l1)
#print(l2)
#print (l3)
#print (l4)
#
#print(Datos)
print(df) 
#print(Base_Datos)
