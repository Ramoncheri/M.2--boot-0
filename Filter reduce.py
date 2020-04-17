from functools import reduce

lista=(1,3,4,-1,15,10)


def esPar(x):
    return x%2==0

y= filter(esPar, lista)

print(list(y))

sumatorio= reduce(lambda x,y: x+y, lista)

print(sumatorio)

suma100= reduce(lambda x,y:x+y, range(101))
#esto suma los 100 primeros numeros. Range, si solo se pone un valor, supone que empieza desde 0
print(suma100)
