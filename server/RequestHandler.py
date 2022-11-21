# TCP request handler class that recieves and sends long messages

import socketserver

ENCODING = 'utf-8'
SUPPORTED_COMMANDS = ['PING', 'LIKE', 'LOGIN', 'REGISTER', 'GET']

class Message:
    def __init__(self, dataBytes: bytes):
        data = dataBytes.decode(ENCODING).split('\n')
        self.type, *self.args = data[0], data[1:]
    
    def fromString(string: str):
        data = string.split('\n')
        return Message((data[0] + '\n' + '\n'.join(data[1:]) + '\n').encode(ENCODING))
        
    def tobytes(self):
        return (self.type + '\n' + '\n'.join(map(str, self.args)) + '\n').encode(ENCODING)

class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        dataBytes = self.request.recv(1024)
        request = Message(dataBytes)
                
        response = self.handleRequest(request)
        self.request.sendall(response.tobytes())

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

