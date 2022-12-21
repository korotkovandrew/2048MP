# database connector class
import json
import random

import DSS

# TODO add MySQL or something

class DBConnector:
    def __init__(self, databaseIP: str, databasePort: int):
        self.databaseIP = databaseIP
        self.databasePort = databasePort
        self.database = None
        with open('database.json', 'r', encoding="utf-8") as f:
            self.database = json.load(f)

    def updateDatabase(self):
        with open('database.json', 'w', encoding="utf-8") as f:
            json.dump(self.database, f)

    def getUser(self, username: str) -> dict:
        return self.database['users'][username] if username in self.database['users'] else None

    def removeUser(self, username: str) -> None:
        self.database['users'].pop(username)
        self.updateDatabase()

    def getUserLikes(self, username: str) -> list:
        return self.database['users'][username]['likes'] if username in self.database['users'] else None

    def isLiked(self, username: str, articleID: int) -> bool:
        return articleID in self.database['users'][username]['likes']

    def setLiked(self, username: str, articleID: int) -> None:
        stringArticleID = str(articleID)
        self.database['users'][username]['likes'].append(articleID)
        self.database['articles'][stringArticleID]['likes'] += 1
        self.updateDatabase()

    def addUser(self, username: str, password: str):
        self.database['users'].update({username: {"password": password,
                                                  "likes": []}})
        self.updateDatabase()

    def getArticle(self, articleID: int) -> dict:
        stringArticleID = str(articleID)
        return (articleID, 
                self.database['articles'][stringArticleID]) if stringArticleID in self.database['articles'] else None

    def getRandomArticle(self) -> dict:
        stringArticleID: str = random.choice(list(self.database['articles'].keys()))
        article: dict = self.database['articles'][stringArticleID]
        return int(stringArticleID), article

    def getRecommendedArticleIDs(self, username: str, numberOfArticles: int) -> list:
        #! now it just returns random articles
        # TODO СППР
        articles = []
        for _ in range(numberOfArticles):
            articleID, _ = self.getRandomArticle()
            articles.append(articleID)
        
