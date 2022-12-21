import json
from socketserver import BaseRequestHandler

import Validation

import pickle

RECV_SIZE = 1024*10
ENCODING = "utf-8"

from DBConnector import DBConnector
dbConnector = DBConnector('localhost', 12345)

OK                   = {'code': ''}
USER_NOT_FOUND       = {'code': 'User not found'}
ARTICLE_NOT_FOUND    = {'code': 'Article not found'}
USER_ALREADY_EXISTS  = {'code': 'User already exists'}
WRONG_PASSWORD       = {'code': 'Wrong password'}
UNKNOWN_REQUEST_TYPE = {'code': 'Unknown request type'}
ALREADY_LIKED        = {'code': 'Already liked'}
NOT_IMPLEMENTED      = {'code': 'Not implemented'}

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
                    response = OK
                case 'like':
                    response = self.handleLike(request)
                case 'get':
                    response = self.handleGet(request)
                case 'login':
                    response = self.handleLogin(request)
                case 'register':
                    response = self.handleRegister(request)
                case _:
                    response = UNKNOWN_REQUEST_TYPE
                    print(f'Unknown request type: {request["type"]}')

            self.request.send(pickle.dumps(response))
            
        print(f'Client {self.client_address} disconnected')
    
    
    def handleLike(self, request: dict) -> dict:
        username: str = request['data']['username']
        articleID: int = request['data']['articleID']

        if not dbConnector.getUser(username):
            return USER_NOT_FOUND
        if not dbConnector.getArticle(articleID):
            return ARTICLE_NOT_FOUND
        if articleID in dbConnector.getUserLikes(username):
            return ALREADY_LIKED

        dbConnector.setLiked(username, articleID)
        print(f'User {username} liked article {articleID}')
        
        #TODO update recommendations for other users
        #TODO return recommended articles for user (if any)
        n = 5
        
        dbConnector.getRecommendedArticleIDs(username, n)
        #! remove this
        # get n random articles and return them
        articles = {}
        for _ in range(n):
            articleID, articleData = dbConnector.getRandomArticle()
            articles[articleID] = articleData
        
        print(f'Recommended articles for {username}: {articles}')
        return {"code": "", "data": articles }


    def handleLogin(self, request: dict) -> dict:
        username: str = request['data']['username']

        if not dbConnector.getUser(username):
            return USER_NOT_FOUND
        if request['data']['password'] != dbConnector.getUser(username)['password']:
            return WRONG_PASSWORD

        print(f'User {username} logged in')
        return OK


    def handleRegister(self, request: dict) -> dict:
        username: str = request['data']['username']
        password: str = request['data']['password']

        if dbConnector.getUser(username):
            return USER_ALREADY_EXISTS

        passwordError: str = Validation.checkPassword(password)
        nicknameError: str = Validation.checkNickname(username)

        if nicknameError:
            return {"code": nicknameError}
        if passwordError:
            return {"code": passwordError}

        dbConnector.addUser(username, password)

        print(f'User {username} registered')
        return OK


    def handleGet(self, request: dict) -> dict:
        isRandom: bool = (request['data']['articleID'] == 0)
        
        if isRandom:
            articleID, articleData = dbConnector.getRandomArticle()
            isLiked = dbConnector.isLiked(request['data']['username'], articleID)
            
            print(f'User {request["data"]["username"]} got random article {articleID}')
            return {"code": '', "articleData": articleData, "articleID": articleID, "liked": isLiked }
        else:
            if not dbConnector.getArticle(request['data']['articleID']):
                return {"code": 'Article not found'}
            
            articleID, articleData = dbConnector.getArticle(request['data']['articleID'])
            isLiked = dbConnector.isLiked(request['data']['username'], articleID)
            
            print(f'User {request["data"]["username"]} got article {request["data"]["articleID"]}')
            return {"code": '', "articleID": articleID, "articleData": articleData, "liked": isLiked }
