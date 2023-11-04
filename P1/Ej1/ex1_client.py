import argparse
import socket
import random

def main(host, port, n):
    # HOST = 'localhost'
    addr= (host, port)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    below_counter = 0
    i = 0
    for i in range(0, int(n)):
        x = str(random.uniform(0, 1))
        y = str(random.uniform(0, 1))

        print ("Enviando un mensaje...")
        m = "("+x+","+y+")"
        s.sendto(m.encode("Utf-8"), addr)
        print("Mensaje enviado.")
        buffer1, addr = s.recvfrom(1024)
        b = buffer1.decode("Utf-8")
        print ("Mensaje recibido: "+ b,addr)
        if b == "below":
            below_counter = below_counter + 1
            i=i+1
        pi = 4.0 * float(below_counter) / float(n)
        print("El valor aproximado de pi con " + str(n) + " puntos aleatorios es " + str(pi))
        s.sendto(str("exit").encode("Utf-8"), addr)

    s.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="remote port")
    parser.add_argument('--host', default='localhost', help="remote hostname")
    parser.add_argument('--number', default=100000, help="number of random points to be generated")
    args = parser.parse_args()

    main(args.host, args.port, args.number)
