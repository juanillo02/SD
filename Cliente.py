import socket
HOST='localhost'
PORT=1025
addr= (HOST,PORT)

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("Soy el cliente".encode("utf-8"),(HOST,PORT))
s.close()
