class Perro():
    def __init__(self, n, e, p):
        self.nombre= n
        self.edad=e
        self.peso=p
        
    def ladrar(self):
        if self.peso >5:
            return "GUAU GUAU"
        else:
            return "guau, guau"
            
    def __str__(self):
        return "Perro {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)
        
        
class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo= amo
        self.__trabajando= False
        
    def __str__(self):
        return "Perro de asistencia de {}".format(self.amo)
   
    def pasear(self):
        return ("Soy {} y ayudo a {} a pasear".format (self.nombre, self.amo))
       #si se pone print en lugar de return, sale un None bajo el primer print, ya que se hace un print de un print
   
    def ladrar(self):
        if self.__trabajando:
            return "shhhh, estoy trabajando"
        else:
            return Perro.ladrar(self)
            
    def trabajando(self, valor= None):
        if valor== None:
            return self.__trabajando
        else:
            self.__trabajando= valor
            

salchicho= Perro('salchicho',3,8)
lolo= Perro('lolo', 5, 1)
miko=Perro ('miko', 4, 6)
rantanplan= PerroAsistencia('rantanplan', 6,8, 'Lucky Luke')
risitas= PerroAsistencia('risitas', 7, 2, 'Pierre',)


print(salchicho.ladrar())

salchicho.nombre= 'Chicho'
print (salchicho)
print (lolo)
print (lolo.ladrar())
print (rantanplan)
print(rantanplan.ladrar())
print (rantanplan.pasear())

risitas.trabajando(True)
print(risitas.ladrar())

