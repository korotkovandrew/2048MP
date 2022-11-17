import socket, threading

from RequestHandler import RequestHandler

HOST = 'localhost'
PORT = 2020 
BUFFER_SIZE = 1024 
DATA_CLOSING_SEQ = '/0'
ENCODING = 'utf-8'

class ClientThread(threading.Thread):
    def __init__(self, socket, host, port):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.socket = socket
        print(f'[+] New thread started for {self.host}:{self.port}')


    def run(self):    
        print(f'Connection from {self.host}:{self.port}')

        while True:
            try:
                #!TODO передача более 1024 байт
                data = self.socket.recv(BUFFER_SIZE)
            except ConnectionResetError:
                print(f"Client broke connection ({self.host}:{self.port})")
                break
            if not data: break
            print ("Client sent : " + data.decode(ENCODING))
            self.socket.send(data)

        print("Client disconnected...")

if __name__ == '__main__':    
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    tcpsock.bind((HOST, PORT))
    threads = []

    while True:
        #!TODO переделать многопоточность
        tcpsock.listen(4)
        print("\nListening for incoming connections...")
        (clientSocket, (host, port)) = tcpsock.accept()
        newthread = ClientThread(clientSocket, host, port)
        newthread.start()
        threads.append(newthread)
