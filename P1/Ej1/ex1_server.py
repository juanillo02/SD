import argparse
import socket
import math

def f(x):
    return math.sqrt(1 - math.pow(x, 2))

def main(host, port):
    # HOST = 'localhost'
    addr = (host, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(addr)
    exit = False
    print("Esperando un mensaje...")
    while exit != 'False':
        buffer, addr = s.recvfrom(1024)
        print("Mensaje recibido: ")
        m = buffer.decode("Utf-8")
        m = m.strip("()")
        a = m.split(",")
        print(a)
        x = float(a[0])
        y = float(a[1])

        if y<f(x) :
            print("below")
            s.sendto("below".encode("Utf-8"), addr)
        elif f(x)>=y :
            print("above")
            s.sendto("above".encode("Utf-8"), addr)
        elif (y<0 or y>1):
            print("error")
            s.sendto("error".encode("Utf-8"), addr)
        buffer2, addr = s.recvfrom(1024)
        print("Mensaje recibido: " + buffer2.decode("utf-8"))

    s.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="listening port")
    parser.add_argument('--host', default='localhost', help="hostname")
    args = parser.parse_args()

    main(args.host, args.port)
