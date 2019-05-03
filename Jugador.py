
class Jugador:
    def __init__ (self, nombre, apellido, dorsal, posicion, pases = 0, pasest = 0):
        self.name = nombre
        self.lastname = apellido
        self.dorsal = dorsal
        self.posicion = posicion
        self.pases = pases
        self.pasest = pasest
        
    def Efectividad (self):
        e = ((self.pases)*100)//self.pasest
        print ("Tuvo una efectividad del {0} %".format(e))
        
    #def OrganizacionB (self):
        
        
    
        
    
       