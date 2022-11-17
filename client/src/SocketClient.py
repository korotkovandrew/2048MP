import socket

ENCODING = 'utf-8'
TIMEOUT = 1
# DATA_CLOSING_SEQ = '\r\n\r\n'
DATA_CLOSING_SEQ = '\0'

#TODO реализовать поддержку всех запросов
# Поддерживаемые запросы:
# 'like' (username, article)
# 'log in' (username, password)
# 'sign in' (username, password)
# 'get random article' (-)
# 'get recommended articles' (username)

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
        return self._connected
    
    def formRequest(self, requestType: str, requestArgs: tuple) -> bytes:
        requestString = requestType + '\n'
        requestString += '\n'.join(map(str, requestArgs))
        requestString += DATA_CLOSING_SEQ
        return requestString.encode(ENCODING)
    
    def sendRequest(self, requestType: str, requestArgs: tuple) -> str:
        if not self.isConnected():
            print(f'Request {requestType} {requestArgs} attempt without connection')
            return ''
        
        req = self.formRequest(requestType, requestArgs)
        
        try:
            self._socket.send(req)
            dataBytes = self._socket.recv(1024)
            #TODO поддержка отправки большего количества пакетов
            response = dataBytes.decode(ENCODING)
            
        except Exception as e:
            print(f'Error while sending a {requestType} request with parameters {requestArgs} to {self._host}:{self._port}')
            print(f'Exception: {e}')
            return ''
            
        return response