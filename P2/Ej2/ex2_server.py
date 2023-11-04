import argparse
import socket
import socketserver
import time


def main(host, port):
    addr = (host, port)
    s_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s_listener.bind(addr)
    print("Conectando al cliente...")
    s_listener.listen()
    s_for_client, addr = s_listener.accept()

    print("Esperando fichero del cliente...")
    contenido = s_for_client.recv(1024).decode("utf-8")
    print("Fichero recibido. Su contenido es:")
    print(contenido)
    linea = contenido.split()
    print("Las lineas divididas por palabras del fichero son:")
    print(linea)

    cont = 0
    i = 0
    j = 0
    lista = []
    longitud =len(linea)

    for i in range(0,longitud):            #Se divide en palabras
        for j in range (0,len(linea[i])):    #Se divide en letras
            if linea[i][j] == 'a':
                lista.append(linea[i])
                cont += 1
                break
    print("El numero de palabras que tiene 'a' son: ",cont)
    print("La lista de palabras con 'a' son: ",lista)
    print("Se va a enviar info")
    lista = lista.split('\n')
    s_for_client.send(str(lista).encode("utf-8"))
    time.sleep(0.5)
    s_for_client.send(str(cont).encode("utf-8"))
    s_listener.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="listening port")
    parser.add_argument('--host', default='localhost', help="hostname")
    args = parser.parse_args()

    main(args.host, args.port)
