# Exercise 2 Template

# Do not modify the file name or function header

# Adds e to mylist and returns the resulting list
def list_add(mylist, e):
    #Añadimos a mylist el elemento e
    mylist.append(e)
    #Si el tipo de e es nulo entoces escribe TypeError
    if type(e) is 0:
        raise TypeError("El elemento e es nulo")
    # devolvemos mylist con el elemento e añadido
    return mylist

# Removes the first occurrence of e in mylist and returns the resulting list
def list_del(mylist, e):
    # Eleminado a mylist el elemento e
    mylist.remove(e)
    # Si el tipo de e es nulo entoces escribe TypeError
    if type(e) is 0:
        raise TypeError("El elemento e es nulo")
    #Si la lista mylist esta vacia entonces escribe TypeError
    if type(mylist) is None:
        raise TypeError("La lista mylist esta vacia")
    # devolvemos mylist con el elemento e eliminado
    return mylist

# Adds the tuple t (value, key) to mydict and returns the resulting dictionary
def dict_add(mydict, t):
    # Añadimos a mydict el elemento t separado en 2 tuplas
    mydict [t[0]] = t[1]
    # Si el tipo de t es nulo entoces escribe TypeError
    if type(t) is 0:
        raise TypeError("El elemento e es nulo")
    # Si la lista mylist esta vacia entonces escribe TypeError
    if len(t) is not 2:
        raise TypeError("t no es una tupla de 2 elementos")
    # devolvemos mydict con el elemento t añadido
    return mydict
