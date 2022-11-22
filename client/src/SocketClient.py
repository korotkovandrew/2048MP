import socket

ENCODING = 'utf-8'
TIMEOUT = 1

#TODO реализовать поддержку всех запросов
# Поддерживаемые запросы:
# 'LIKE' (username, article)
# 'LOGIN' (username, password)
# 'REGISTER' (username, password)
# 'GET' (-)

#TODO вынести в папку API
# message class for storing requests and responses
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

class SocketClient:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.settimeout(TIMEOUT)
        
        try: 
            self._socket.connect((self._host, self._port))
        except socket.error as exc:
            print(f'Connection failed ({self._host}:{self._port}). Exception: {exc}')
            self._connected = False
            return
            
        self._connected = True
        print(f'Connection success ({self._host}:{self._port})') 
        
    def __del__(self):
        self._socket.close()
        print(f'Connection closed ({self._host}:{self._port})')
        
    def isConnected(self) -> bool:
        return self._connected and self._socket is not None
    
    def sendRequest(self, requestType: str, requestArgs: tuple) -> Message:
        if not self.isConnected():
            print(f'Request {requestType} {requestArgs} attempt without connection')
            response = Message('ERROR', 'Connection failed')
        try:
            message = Message(requestType, requestArgs)
            self._socket.send(message.toBytes())
            response = Message.fromBytes(self._socket.recv(1024))
            #TODO поддержка отправки большего количества пакетов
        except Exception as e:
            print(f'Error while sending a {requestType} request with parameters {requestArgs} to {self._host}:{self._port}')
            print(f'Exception: {e}')
            response = Message('ERROR', f'Error while sending a {requestType} request')
            
        return response