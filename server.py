import socket
from threading import Thread

SERVER = None
PORT = 8080
IP_ADDRESS = '127.0.0.1'

CLIENTS = []

def setup():
    print('IP MESSENGER')
    
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))
    SERVER.listen(100)
    print('Server is waiting for incoming connections...')
    acceptConnections()

setup_thread = Thread(target=setup)
setup_thread.start()

def acceptConnections():
    global SERVER
    global CLIENTS

    while(True):
        client,address = SERVER.accept()
        print(client,address)