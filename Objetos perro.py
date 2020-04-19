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
        
            
salchicho= Perro('salchicho',3,8)
lolo= Perro('lolo', 5, 1)
miko=Perro ('miko', 4, 6)

print(salchicho.ladrar())

salchicho.nombre= 'Chicho'
print (salchicho)
print (lolo)
print (lolo.ladrar())

