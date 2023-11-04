from bottle import run
import requests

# Lo primero que se hace en el cliente es el menú. Juraría que no hace falta crear un post ni nada, se accede al menú
# por la terminal y ya.
# Si no fuera así creamos un /menu y listo, pero creo que es así:

print("1. Añadir sala\n")
print("2. Mostrar información de sala\n")
print("3. Añadir reserva\n")
print("4. Listar reservas\n")
print("5. Eliminar reserva\n")
print("6. Exit\n")
opcion = int(input("Introduce la opción que deseas:\n"))

if opcion == 1:
    i = 0
    recursos = []
    res = ""

    # Los datos deben ser recogidos por el cliente según dice el guión de la práctica.
    # Aquí recogemos el nombre de usuario y la contraseña. Esto también se envía al server para que él compruebe que el
    # usuario existe y eso (en el guión pone que se haga así)
    print("Nombre de usuario:")
    nombre = input()
    print("Contraseña:")
    pwd = input()

    print("Introduzca el id de la sala:")
    idsala = input()
    print("Introduzca la capacidad de la sala:")
    capacidad = input()

    # Esto es un bucle para crear un vector de recursos.El usuario introduce recursos hasta que escribe nd,entonces para
    while res != "nd":
        print(f"Recurso {i + 1} de la sala: (Pulse nd si ya no hay más recursos)")
        res = input()
        if res != "nd":  # Hace falta este if porque si no se cuela el "nd" al final del vector
            recursos.append(res)
        i += 1

    # Cuando lo tenemos tod, mandamos el json al server en el get en el que llamamos a la página que toca
    anadir = requests.post('http://localhost:8080/addRoom', json={"nombre": nombre, "pwd": pwd, "IDsala": idsala,
                                                                  "Capacidad": capacidad, "Recursos": recursos})
    print(anadir.status_code)  # Realmente no se para qué sirve esto
    print(anadir.text)

if opcion == 2:
    # Repetimos lo del usuario.Le preguntaré a Sara si es así o se puede comprobar antes de elegir, pero creo que es así
    print("Nombre de usuario:")
    nombre = input()
    print("Contraseña:")
    pwd = input()

    print("id de la sala que desea consultar")
    Idsala = input()

    # res se pasa como variable, aunque tambien se podría meter en el mismo json del nombre y la contraseña.
    # Como vi que la funcion del server recibía una variable lo he puesto así
    listar = requests.get('http://localhost:8080/showInformationRoom/<Idsala>', json={"nombre": nombre, "pwd": pwd,
                                                                                      "Idsala": Idsala})
    print(listar.status_code)
    print(listar.text)

if opcion == 3:
    print("Nombre de usuario:")
    nombre = input()
    print("Contraseña:")
    pwd = input()

    print("ID de la sala que desea reservar:")
    idsala = input()
    print("fecha en la que desea hacer la reserva: (formato: día-mes-año")
    fecha = input()
    print("Hora de inicio:")
    hora_inicio = input()
    print("Duración de la reserva (en minutos)")
    duracion = input()

    anadirres = requests.get('http://localhost:8080/addBooking', json={"nombre": nombre, "pwd": pwd, "Idsala": idsala,
                                                                       "fecha": fecha, "hora_inicio": hora_inicio,
                                                                       "duracion": duracion})
    print(anadirres.status_code)
    print(anadirres.text)

if opcion == 4:
    print("Nombre de usuario:")
    nombre = input()
    print("Contraseña:")
    pwd = input()

    print("Dni:")
    dni = input()

    listarres = requests.get('http://localhost:8080/showBookings/<dni>', json={'nombre': nombre, 'pwd': pwd,
                                                                               'dni': dni})
    print(listarres.status_code)
    print(listarres.text)

if opcion == 5:
    print("Nombre de usuario:")
    nombre = input()
    print("Contraseña:")
    pwd = input()

    print("Id de la reserva que desea anular:")
    Idreserva = input()

    eliminarres = requests.get('http://localhost:8080/delete/Booking/<Idreserva>', json={'nombre': nombre, 'pwd': pwd,
                                                                                         'Idreserva': Idreserva})
    print(eliminarres.status_code)
    print(eliminarres.text)

if opcion == 6:
    print("Gracias por usar nuestra plataforma")

if __name__ == '__main__':
    run(host='localhost', port=8080)

# Dudas SD
# Cómo se pone la fecha en el json-reservas?
# Si paso una variable del cliente, lo pilla la función (se ve en listar una sala)?
# Sumar minutos?
# El login se hace al principio y ya está, o se tiene que hacer en antes de enviar cada petición?
# Bucles en jsons
# Error 405?
