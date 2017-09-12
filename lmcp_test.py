import socket
from lmcp import LMCPFactory

def connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 5555)
    print("connecting to %s port %s") % (server_address)
    sock.connect(server_address)
    print("connected")
    return sock

sock = connect()
msg = LMCPFactory.LMCPFactory()

try:
    while True:
        buff = sock.recv(90000)
        print (buff)
        message = msg.getObject(buff)
        print (message)

finally:
    print("closing socket")
    sock.close()
