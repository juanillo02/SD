# Exercise 1 Template

# Do not modify the file name or function header

# Return the sum of those parameters that contain an even number
#from Tools.scripts.mailerdaemon import x

#funcion que queremos comprobar
def accum(x, y, z):
    #declaramos la variable sum a 0
    sum = 0
    #Si el resto de dividir x entre 2 es 0 entonces
    if x % 2 == 0:
        #a la variable sum se suma a ella misma y el valor de x, guardandose en la variable sum
        sum = sum + x
    # Si el resto de dividir y entre 2 es 0 entonces
    if y % 2 == 0:
        #a la variable sum se suma a ella misma y el valor de y, guardandose en la variable sum
        sum = sum + y
    # Si el resto de dividir z entre 2 es 0 entonces
    if z % 2 == 0:
        #a la variable sum se suma a ella misma y el valor de z, guardandose en la variable sum
        sum = sum + z
    #Si el tipo del valor de x es float entonces
    if type(x) is not int :
        #Devuelve TypeError
        raise TypeError("No es un numero entero")
    # Si el tipo del valor de y es float entonces
    if type(y) is not int :
        # Devuelve TypeError
        raise TypeError("No es un numero entero")
    # Si el tipo del valor de z es float entonces
    if type(z) is not int :
        # Devuelve TypeError
        raise TypeError("No es un numero entero")
    #Devuelve la sum una vez hecho todos los comprobantes
    return sum
