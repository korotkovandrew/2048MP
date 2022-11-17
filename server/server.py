import socket


HOST = 'localhost'
PORT = 2020 
BUFFER_SIZE = 1024 
DATA_CLOSING_SEQ = '/0'
ENCODING = 'utf-8'

# class SocketServer:
#     def __init__(self, host, port):
#         self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.socket.bind((host, port))
        
#     def __del__(self):
#         self.socket.close()
        
#     def run(self):
#         self.socket.listen(5)
#         while True:
#             try:
#                 conn, addr = self.socket.accept()
#                 print(f"Connected by {addr[0]}:{addr[1]}")
                
#                 while True:
#                     self.serveClient(conn, addr)
                
#                 print(f'Connection closed ({addr[0]}:{addr[1]})')
#                 conn.close()    
            
                
#             except ConnectionError:
#                 print(f'Connection error ({addr[0]}:{addr[1]})')
#                 return
#             except OSError as e:
#                 print(f'Exception: {e}')
#                 return
        
#     def serveClient(self, conn, addr):
#         data = self.socket.recv(1024)
#         self.socket.send(data)
        

# # def recvall(conn):
# #     #TODO реализация, позволяющая передавать более 1024 байт
# #     dataParts = []
# #     dataBytes = b''
    
# #     while not dataBytes.endswith(DATA_CLOSING_SEQ.encode(ENCODING)):
# #         dataBytes = conn.recv(1024)
# #         if not dataBytes:
# #             break
# #         dataParts.append(dataBytes.decode(ENCODING))
        
# #     data = ''.join(dataParts)[:-len(DATA_CLOSING_SEQ)]
# #     dataParts = []
    
# #     print(data)
# #     self.socket.send()
    
        
# if __name__ == '__main__':
#     server = SocketServer(HOST, PORT)
    
#     server.run()
        
import socket, threading

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
        tcpsock.listen(4)
        print("\nListening for incoming connections...")
        (clientSocket, (host, port)) = tcpsock.accept()
        newthread = ClientThread(clientSocket, host, port)
        newthread.start()
        threads.append(newthread)
        
    for t in threads:
        t.join()