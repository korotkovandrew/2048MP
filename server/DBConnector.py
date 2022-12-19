# database connector class
import json
import random

# TODO add database of users and articles
ENCODING = "utf-8"

class DBConnector:
    def __init__(self, databaseIP, databasePort):
        self.databaseIP = databaseIP
        self.databasePort = databasePort
        self.database = None
        with open('database.json', 'r', encoding=ENCODING) as f:
            self.database = json.load(f)
            self.database['articles'] = {
                int(articleID): article for articleID, article in self.database['articles'].items()}


    def __del__(self):
        with open('database.json', 'w', encoding=ENCODING) as f:
            json.dump(self.database, f, indent=4)
        
        
    def getUser(self, username) -> dict:
        print(username)
        return self.database['users'][username] if username in self.database['users'] else None
    
    
    def removeUser(self, username) -> None:
        self.database['users'].pop(username)
        
        
    def getUserLikes(self, username) -> list:
        return self.database['users'][username]['likes'] if username in self.database['users'] else None
        
        
    def isLiked(self, username, articleID) -> bool:
        return articleID in self.database['users'][username]['likes']
        
        
    def setLiked(self, username, articleID) -> None:
        self.database['users'][username]['likes'].append(articleID)
        self.database['articles'][articleID]['likes'] += 1
        
        
    def addUser(self, username, password):
        self.database['users'].update({username: {"password": password,
                                                  "likes": []}})
        
        
    def getArticle(self, articleID) -> dict:
        return self.database['articles'][articleID] if articleID in self.database['articles'] else None
    
    
    def getRandomArticle(self) -> dict:
        articleID = random.choice(list(self.database['articles'].keys()))
        article = self.database['articles'][articleID]
        return articleID, article
        
        
    def getRecommendedArticleID(self, username) -> int:
        # get from user recomendations list (as fast as possible)
        # TODO СППР
        pass
