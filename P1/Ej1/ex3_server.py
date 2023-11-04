import argparse
import socket
import numpy as np


def main(host, port):
    addr = (host,port)                                                  #Senalamos la direccion de la conexion
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                #Creamos el socket
    s.bind(addr)                                                        #Vinculamos una direccion al socket
    print("Esperando un mensaje...")
    buffer, addr1 = s.recvfrom(512)                                     #Recibimos el nombre del jugador 1
    print("Nombre jugador 1: " + buffer.decode("Utf-8"))
    buffer1, addr1 = s.recvfrom(512)                                    #Recibimos el tablero del jugador 1
    print("Tablero jugador 1:")
    buffer1 = buffer1.decode("Utf-8").split(";")                        #Separamos el tablero marcando como delimitador ";"
    print(buffer1)
    buffer2, addr2 = s.recvfrom(512)                                    #Recibimos el nombre del jugador 2
    print("Nombre jugador 2: " + buffer2.decode("Utf-8"))
    buffer3, addr2 = s.recvfrom(512)                                    #Recibimos el tablero del jugador 1
    print("Tablero jugador 2:")
    buffer3 = buffer3.decode("Utf-8").split(";")                        #Separamos el tablero marcando como delimitador ";"
    print(buffer3)


    id = int(float(1))
    exit = True                                                         #Usamos el True para crear un bucle indefinido
    jugada = 1                                                          #Se marca como 1 para expresar que empieza el jugador 1
    t1= []
    t2= []
    letras = ['A','B','C','D','E','F','G','H','I','J']                  #Creamos una lista que contenga las letras que equivalen a las columnas del tablero

    for i in range(0,len(buffer1)):                                     #Hacemos un bucle para separar entre 0 y 1 teniendo como delimitador los espacios entre ellos
        t1.append(buffer1[i].split())
        t2.append(buffer3[i].split())

    t1 = np.matrix(t1)
    t2 = np.matrix(t2)

    tablero = t1


    while exit == True:                                                 #Hacemos un bucle para saber a que jugador le toca el turno
        if jugada == 1:
            atacante = addr1
            defensor = addr2
            tablero = t2
        else :
            atacante = addr2
            defensor = addr1
            tablero = t1

        if tablero == t1:
            tablero = t2
        else:
            tablero = t1

        msg = "Turn " + str(id)
        s.sendto(str(msg).encode("Utf-8"), atacante)                    #Enviamos el mensaje "Turn" al jugador al que le toca el turno
        print("Esperando movimiento.")
        buffer4, addr = s.recvfrom(512)                                 #Recibimos le movimiento del jugador
        coor = buffer4.decode("Utf-8")                                  #Decodificamos el mensaje y lo anadimos a la variable coor
        print(coor)

        coor_letra = coor[0]                                             #Separamos la letra de las coordenadas que envia el jugador y se crea la lista corr_letra
        coor_num = int(coor[1])                                          #Separamos el numero de las coordenadas que envia el jugador y se crea la lista corr_num

        for i in range(0,len(letras)):                                  #Recorremos el vector de letras para buscar una que coincida con el movimiento del jugador
            if letras[i] == coor_letra:
                col = i                                                 #Si coincide entonces guardamos el numero en el que se situa esa letra en la variable "col"
                break


        if tablero[coor_num][col] == 1:                                     #Si coincide la fila y la columna con un 1 en el tablero:
            tablero[coor_num][col] = 0                                      #Le ha dado al barco por lo que se cambia a 0 para que no pueda volver a darle
            for c in range(0,len(tablero)):
                for f in range(0,len(tablero[c])):                      #Se usan ambos bucles para recorrer el tablero para conocer si hay mas 1
                    if tablero[f][c] == 1:                              #Si existen mas 1:
                        hit = "Hit"
                        s.sendto(str(hit).encode("Utf-8"), atacante)    #Enviamos el mensaje al jugador que este atacando en ese momento
                        id += 1                                         #Aumentamos por 1 el turno
                    else:                                               #Si no existen mas 1:
                        w = "You win"
                        s.sendto(str(w).encode("Utf-8"), atacante)      #Enviamos el mensaje de victoria al atacante
                        z = "You lost"
                        s.sendto(str(z).encode("Utf-8"), defensor)      #Enviamos el mensaje de derrota al defensor
                        exit = False                                    #Termina el juego
        else:                                                           #Si no coincide la fila y la columna con un 1 en el tablero:
            fail = "Fail"
            s.sendto(str(fail).encode("Utf-8"), atacante)               #Enviamos el mensaje de "Fail" al atacante
            jugada = 2                                                  #Cambiamos de jugador
        id = id + 1                                                     #Aumentamos por 1 el turno
    s.close()                                                           #Terminamos la conexion con el socket



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="listening port")
    parser.add_argument('--host', default='localhost', help="hostname")
    args = parser.parse_args()

    main(args.host, args.port)
