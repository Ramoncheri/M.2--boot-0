from Func1Nivel import sumaTodos

doble= lambda x:x*2

print(sumaTodos(3, doble))
print(sumaTodos(3, lambda x: x**3))

#en el resultado va a asalir el nombre del modulo porque está asi mandado en el módulo de la función sumaTodos