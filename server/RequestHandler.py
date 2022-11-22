# TCP request handler class that recieves and sends long messages

import socketserver

ENCODING = 'utf-8'
SUPPORTED_COMMANDS = ['PING', 'LIKE', 'LOGIN', 'REGISTER', 'GET']


class Message:
    def __init__(self, messageType: str, *args: any):
        self.type = messageType
        self.args = args

    @staticmethod
    def fromString(string: str):
        data = string.split('\n')
        return Message(data[0], data[:1])
        
    @staticmethod
    def fromBytes(dataBytes: bytes):
        return Message.fromString(dataBytes.decode(ENCODING))
    
    def toBytes(self):
        return (self.type + '\n' + '\n'.join(map(str, self.args)) + '\n').encode(ENCODING)
    
    def __str__(self) -> str:
        return self.type + '\n' + '\n'.join(map(str, self.args))
    
    
class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(f'Connection from {self.client_address[0]}:{self.client_address[1]}')
        dataBytes = self.request.recv(1024)
        print(type(dataBytes))
        while dataBytes:
            message = Message.fromBytes(dataBytes)
            response = self.handleRequest(message)
            print(f'Request: {message}')
            self.request.sendall(response.toBytes())
            dataBytes = self.request.recv(1024)

    def handleRequest(self, message: Message) -> Message:
        if message.type not in SUPPORTED_COMMANDS:
            return Message.fromString(f'ERROR\nUnsupported command\n{message.type}')
        
        if message.type == 'PING':
            print(f'Ping from {self.client_address[0]}:{self.client_address[1]}')
        elif message.type == 'LIKE':
            print(f'Like {message.args}')
        elif message.type == 'LOGIN':
            print(f'Login {message.args}')
        elif message.type == 'REGISTER':
            print(f'Register {message.args}')
        elif message.type == 'GET':
            print(f'Get {message.args}')
        
        return Message.fromString(f'OK\n{message.type} {message.args}')

