import socket
HOST='localhost'
PORT=1025

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind( ('localhost',8000))

print("Me quedo a la espera")
con, addr=s.recvfrom(1024)
print ("Mensaje recibido -->", str(con.decode("utf-8")))
print ("IP cliente:", str(addr[0]))
print ("Puerto cliente:", str(addr[1]))
s.close()