def normal(x):
    return x

def cuadrado (y):
    return y*y

def sumaTodos(limitTo,f):
    result=0
    for i in range (limitTo+1):
        result +=f(i)
        
    return result


print (sumaTodos(100, normal))
print (sumaTodos(4, cuadrado))

