import argparse
import socket
import socketserver
import time


def main(host, port, filein, fileout):
    addr = (host, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if filein is None:
        raise OSError ("El fichero no se pudo abrir.")
    with open(filein,'r') as f1:
        contenido = f1.read()
        print("Conectando al servidor...")
        s.connect(addr)
        print("Enviando el fichero...")
        s.sendall(contenido.encode("utf-8"))
        print("Fichero enviado.")
        s1 = s.recv(1024)
        time.sleep(0.5)
        s2 = s.recv(1024)
        s_for_server, s_for_server2 = s1, s2
        recibo1 = s_for_server.decode("utf-8")
        time.sleep(0.5)
        recibo2 = s_for_server2.decode("utf-8")
        print("se recibió")
        print(recibo1)
        print(recibo2)
        #recibo1 = recibo1.split()
        print (recibo1, sep='\n')
        with open(fileout,'w') as f2:
            """
            recibo = recibo1.strip("[]")
            recibo = recibo.replace(",","")
            recibo1 = recibo.replace("'","")
            #f2.write('\n'.join(recibo1))
            f2.write(recibo1, end=("\n"))
            """
            #recibo = recibo1.split()
            f2.write('\n'.join(recibo1))

        s.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="remote port")
    parser.add_argument('--host', default='localhost', help="remote hostname")
    parser.add_argument('--filein', default='filein.txt', help="file to be read")
    parser.add_argument('--fileout', default='fileout.txt', help="file to be written")
    args = parser.parse_args()

    main(args.host, args.port, args.filein, args.fileout)
