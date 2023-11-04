"""
#Video 1
Numero_uno = 2
numero_uno = "Hola mundo"
print(numero_uno, Numero_uno)
print("Esto es una suma")
numero_uno = 2
numero_dos = 4
resultado = numero_uno + numero_dos
print(resultado)
"""
"""
#Video 2 Agregar a la cadena de caracteres
mensaje = "Hola"
mensaje += " "
mensaje += "Ernesto"
print(mensaje)
#Concatenación
print("Concatenación")
mensaje = "Hola"
espacio = " "
nombre = "Ernesto"
print (mensaje + espacio + nombre)
#Concatenacion con numeros
numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
resultado = str(resultado)
print ("El resultado de la suma es: " + resultado)
#Para no tener que hacer el str se pone,
print ("El resultado de la suma es: ", resultado)
#Buscar subcadena
mensaje = "Hola Ernesto"
buscar_subcadena = mensaje.find("Ernesto")
print (buscar_subcadena)
extraer_subacdena = mensaje[1:8]
print (extraer_subacdena)
#Comparar cadenas
mensaje_uno = "Hola"
mensaje_dos = "Hola"
print (mensaje_uno == mensaje_dos)
"""

#Video 3 Palabras Reservadas
#and del for is raise assert
#if else elif from lambda return
#break global not try class except
#or while continue exec import yield
#def finally in print
"""
#Video 4 Operaciones aritméticos
print ("Suma:") #Resta -
numero_uno = 5  #Multiplicación *
numero_dos = 4  #Potencia **
resultado = numero_uno + numero_dos  #Division /, division entera //
print ("El resultado de la suma es: ", resultado) #Resto %
"""
#Video 5 Comentarios
#Se puede poner con
# es para una sola linea y tambien "sirve para una linea"
# """para varias lineas"""
"""
#Video 6 Tipos de datos
#entero
numero = 15
print(numero, type(numero))
#flotante
num_flot = 15.5
print(num_flot, type(num_flot))
#complejos
num_com = 5 + 6j
print(num_com, type(num_com))
#String
nombre = "Ernesto"
print(nombre, type(nombre))
#Booleano
v_f = 3 == 3
print(v_f, type(v_f))
"""
"""
#Video 7 Entrada de datos
palabra = input("Introduce una palabra: ")
num_int = int(input("Introduce un número entero: "))
num_float = float(input("Introduce un número flotante: "))
num_compless = complex(input("Introduce un número complejo: "))
print ("String: ", palabra)
print ("Número entero: ", num_int)
print ("Número flotante: ", num_float)
print ("Número complejo: ", num_compless)
nombre = input("¿Cúal es tu nombre?: ")
print ("Hola " + nombre + ", vamos a realizar una suma.")
num_uno = int(input("Introduce un número: "))
num_dos = int(input("Introduce un número: "))
resultado = num_uno + num_dos
print ("El resultado de la suma es: ", resultado)
"""
"""
#Video 8 y 9 Condicionales
num_uno = 5
if  num_uno == 5 :
    print ("El número es cinco")
else :
    print ("El número no es cinco")
print("Fin.")
print("Sistema para calcular la media")
nombre = input("¿Cúal es tu nombre?: ")
mat = int(input("Introduce la nota de matemáticas: "))
fis = int(input("Introduce la nota de física: "))
tec = int(input("Introduce la nota de tecnología: "))
med = (mat + fis+ tec) / 3
if med >= 6 :
    print ("La nota media de", nombre ,"es:", round(med,2))
    print ("Enhorabuena estas aprobado.")
else :
    print ("La nota media de", nombre , "es", round(med,2))
    print ("Lo sentimos, estas suspenso")
print("Fin.")
"""
"""
#Video 10 Condicionales elif
num_uno = 3
if num_uno == 1 :
    print ("El número es: Uno.")
elif num_uno == 2 :
    print ("El número es: Dos.")
else :
    print ("El número se desconoce.")
print ("Convertidor de números a letras")
num_uno = int(input("¿Cúal es el número que quieres introducir?: "))
if num_uno == 1:
    print ("El número es: Uno.")
elif num_uno == 2:
    print ("El número es: Dos.")
elif num_uno == 3:
    print("El número es: Tres.")
elif num_uno == 4:
    print ("El número es: Cuatro.")
elif num_uno == 5:
    print ("El número es: Cinco.")
else :
    print ("El programa solo convierte hasta el 5")
print ("Fin.")
"""
"""
#Video 11 Condicionales anidados
print ("Conversor")
print ("Menú de opciones: \n")
print ("Presiona 1 para convertir de número a palabra. \n")
print ("Presiona 2 para convertir de palabra a número. \n")
opcion = int(input("¿Cúal es la opción que eliges?"))
if opcion == 1 :
    print ("\n Conversor de número a palabra. \n")
    op_uno = int(input("Introduce el numero a converir: "))
    if op_uno == 1 :
        print ("El número es: Uno.")
    elif op_uno == 2 :
        print ("El número es: Dos.")
    elif op_uno == 3 :
        print ("El número es: Tres.")
    elif op_uno == 4 :
        print ("El número es: Cuatro.")
    elif op_uno == 5 :
        print ("El número es: Cinco.")
    else :
        print ("Solo puedo convertir hasta el 5")
elif opcion == 2 :
    print ("\n Conversor de palabra a número. \n")
    op_dos = input("Introduce una palabra a convertir: ")
    op_dos = op_dos.lower() #Convierte a minúscula
    if op_dos == 'uno' :
        print ("La palabra es: 1.")
    elif op_dos == 'dos' :
        print ("La palabra es: 2.")
    elif op_dos == 'tres' :
        print ("La palabra es: 3.")
    elif op_dos == 'cuatro' :
        print ("La palabra es: 4.")
    elif op_dos == 'cinco' :
        print ("La palabra es: 5.")
    else :
        print ("Solo puedo convertir del uno al cinco")
else :
    print ("Opción no disponible.")
"""
#Video 12 Operadores relacionales
# < menor que, > mayor que, == igual a, !=  diferente a
# <= menor o igual a, >= mayor o igual a
"""
#Video 13 Operaciones lógicas
#and
num_uno = 5
num_dos = 5
if num_uno == 5 and num_dos >= 5 :
    print ("Ambas condiciones se cumplen.")
else :
    print ("Una o las dos condiciones no se cumplen.")
#or
if num_uno == 5 or num_dos >= 5 :
    print ("Una o las dos condiciones se cumplen.")
else :
    print ("No se cumplen ninguna de las dos.")
#not
num_tres = 2
if not num_tres > 5 :
    print ("La condición se invirtió y se cumple.")
else :
    print ("Se cumple la condición ya que el número es mayor a 5.")
"""
"""
#Video 14 Operadores de asignación
#asignación
#x=5
#x=y
#y=5
#asignación de suma, resta
#x=3 resta: -=, división entera: //=
#x+=5 multiplicación: *=, exponente: **=
#x=8 división: /=, resto: %=
mensaje = "Hola "
mensaje += "Juan"
numero = 5
numero += 3
print (mensaje, "tu número es:", numero)
nombre = "Hola "
nombre += input("Escribe tu nombre: ")
print (nombre, ", esto es el incremento y decremento de una varibable \n")
print ("Incremento:")
x=1
print ("El valor inicial de x es:", x)
x+=1
x+=1
x+=1
x+=1
print ("El valor final de x es:", x, "\n")
print ("Decremento:")
print("El valor incial de x es:", x)
x-=1
x-=1
x-=1
x-=1
print ("El valor final de x es:", x)
"""
"""
#Video 15 parametros sep y end
print ("Esto es un", end=" ")
print ("ejemplo")
print("1","2","3","4","5", sep="-")
"""
"""
#Video 16 While
x=1
while x<10 :
    print ("Juan")
    x+=1
print ("Fin.")
"""
"""
#Video 17 break y continue
print ("While con la sentencia break \n")
con=0
while con < 10 :
    con += 1
    if con == 5 :
        break #Para en el 5
    print ("Valor actual de la variable:", con)
print ("Fin del programa")
print ("\nWhile con la sentencia break \n")
con=0
while con < 10 :
    con += 1
    if con == 5 :
        continue #Continua despues del 5 pero no muestra el 5
    print ("Valor actual de la variable:", con)
print ("Fin del programa")
"""
"""
#Video 18 len()
print ("Hola tine", len("Hola"), "caracteres.")
long = len("La Geekipedia")
print ("La Geekipedia tiene", long, "caracteres.")
"""
"""
#Video 19 Concatenacion format()
nombre = "Juan"
edad = 22
print ("Hola {} tienes {} años.".format(nombre, edad))
print ("Hola {nombre} tienes {edad} años.".format(nombre= "Juan", edad=22))
print ("Hola {0} tienes {1} años.".format(nombre, edad))
"""
"""
#Video 20 f-Strings{}
print (f"El resultado de la suma 4+1 = {4+1}")
nombre ="Carlos"
alt = 1.8
edad = 22
print (f"Hola {nombre}, tu altura es de {alt} metros y tienes {edad} años.")
nombre = input("¿Cúal es tu nombre?: \n")
num_uno = int(input("Introduce un número: \n"))
num_dos = int(input("Introduce otro número: \n"))
print(f"Hola {nombre}, el resultado de sumar {num_uno} + {num_dos} es: {num_uno+num_dos}")
"""
"""
#Video 21 strip ()
cadena = " Hola Juan "
cadena = cadena.strip("a nHo")
print(cadena)
cadena1 = "\tHola Juan\n"
print (cadena1)
cadena1 = cadena1.strip("a nHo\t\n")
print(cadena1)
"""
"""
#Video 22 rstrip() y lstrip()
cadena = "\tHola Ernesto\n"
print (cadena)
cadena = cadena.rstrip("s tHo\t\n")
print (cadena)
cadena1 = "\tHola Ernesto\n"
print(cadena1)
cadena1 = cadena1.lstrip("s toH\t\n")
print(cadena1)
"""