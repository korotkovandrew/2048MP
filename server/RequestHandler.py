from socketserver import BaseRequestHandler

from PasswordValid import *

import pickle
import random

#TODO add same config file for client and server
ENCODING = "utf-8"
RECV_SIZE = 1024*10

# TODO add database of users and articles

import json
with open('database.json', 'r', encoding=ENCODING) as f:
    database = json.load(f)
    database['articles'] = {int(articleID): article for articleID, article in database['articles'].items()}


def printDatabase():
    print('Database:')
    for username, user in database['users'].items():
        print(f'User {username}:')
        print(f'\tPassword: {user["password"]}')
        print(f'\tLikes: {user["likes"]}')
    for articleID, article in database['articles'].items():
        print(f'Article {articleID}:')
        print(f'\tTitle: {article["title"]}')
        print(f'\tLikes: {article["likes"]}')
        
printDatabase()
           
class RequestHandler(BaseRequestHandler):
    
    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            data_bytes: bytes = self.request.recv(RECV_SIZE)
            if not data_bytes:
                break
            
            request: dict = pickle.loads(data_bytes, encoding=ENCODING)
            
            match request['type']:
                case 'ping':
                    response = {'code': ''}
                case 'like':
                    response = self.handleLike(request)
                case 'get':
                    response = self.handleGet(request)
                case 'login':
                    response = self.handleLogin(request)
                case 'register':
                    response = self.handleRegister(request)
                case _:
                    response = {'code': 'Unknown request type'}
                    print(f'Unknown request type: {request["type"]}')
                
            self.request.send(pickle.dumps(response))
            self.updateDB()
        print(f'Client {self.client_address} disconnected')
        
    def updateDB(self):
        with open('database.json', 'w') as f:
            json.dump(database, f)

    def handleLike(self, request: dict) -> dict:
        username: str = request['data']['username']
        articleID: int = request['data']['articleID']
        
        if username not in database['users']:
            return {"code": 'User not found'}
        if articleID not in database['articles']:
            return {"code": 'Article not found'}
        if articleID in database['users'][username]['likes']:
            return {"code": 'Already liked'}
        
        database['users'][username]['likes'].append(articleID)
        database['articles'][articleID]['likes'] += 1
        
        print(f'User {username} liked article {articleID}')
        
        return {"code": ''}
    
    def handleLogin(self, request: dict) -> dict:
        username: str = request['data']['username']
        
        if username not in database['users']:
            return {"code": 'User not found'}
        if request['data']['password'] != database['users'][username]['password']:
            return {"code": 'Wrong password'}
        
        print(f'User {username} logged in')
        
        return {"code": ''}
    
    def handleRegister(self, request: dict) -> dict:
        username: str = request['data']['username']
        password: str = request['data']['password']
        
        if username in database['users']:
            return {"code": 'User already exists'}
        
        passwordError: str = checkPassword(password)
        nicknameError: str = checkNickname(username)
        
        if nicknameError:
            return {"code": nicknameError}
        if passwordError:
            return {"code": passwordError}
        
        database['users'].update({username: {"password": password, 
                                             "likes": []}})    
        
        print(f'User {username} registered')
        return {"code": ''}
    
    def handleGet(self, request: dict) -> dict:
        isRandom: bool = request['data']['isRandom']
        
        if isRandom:
            articleID: int = random.choice(list(database['articles'].keys()))
            print(f'User {request["data"]["username"]} got random article {articleID}')
            return {"code": '', 
                    "articleData": database['articles'][articleID],
                    "articleID": articleID,
                    "liked": articleID in database['users'][request['data']['username']]['likes']}
            
        elif request['data']['articleID']:
            if request['data']['articleID'] not in database['articles']:
                return {"code": 'Article not found'}
            
            print(f'User {request["data"]["username"]} got article {request["data"]["articleID"]}')
            
            return {"code": '', 
                    "articleID": request['data']['articleID'],
                    "articleData": database['articles'][request['data']['articleID']],
                    "liked": articleID in database['users'][request['data']['username']]['likes']}
        else:  
            return {"code": 'Not implemented'}

            #TODO ADD 'СППР'         
            username: str = request['data']['username']
            
            if username not in database['users']:
                return {"code": 'User not found'}
            
            # print(f'User {username} logged in')
            