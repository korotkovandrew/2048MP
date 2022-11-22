import sys

from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtCore import QUrl

from src.LogInDialog import LogInDialog
from src.SignInDialog import SignInDialog
from src.SocketClient import SocketClient

HOST, PORT = 'localhost', 2020

FULL_ARTICLE_LINK_PLACEHOLDER = 'https://google.com'

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('./src/ui/mainWindow.ui', self)
        self.setWindowIcon(QtGui.QIcon('./img/AB_icon.ico'))

        self._client = SocketClient(HOST, PORT)
        if not self._client.isConnected():
            # TODO gui уведомление об ошибке подключения
            print("Connection error. Application was closed")
            sys.exit()

        # TODO окно регистрации
        
        self._currentUser = ''

        #TODO определить в каком виде хранится статья для удобной работы с ней
        self._openedArticle = ''  # ?
        self._currentArticleText = self.articleText.toPlainText()
        self._currentArticleLink = FULL_ARTICLE_LINK_PLACEHOLDER
        
        self.updateGui()
        
        self.logInButton.clicked.connect(self.logInButtonPressed)
        self.signInButton.clicked.connect(self.signInButtonPressed)
        self.likeButton.clicked.connect(self.likeButtonPressed)
        self.randomArticleButton.clicked.connect(self.randomArticleButtonPressed)

        self.show()
        
    def isLoggedIn(self):
        return self._currentUser != ''

    def updateRecommendations(self):
        self._client.sendRequest('GET', ())
        pass
    
    def updateGui(self):
        self.articleText.setText(self._currentArticleText)
        
        self.fullArticleLinkLabel.linkActivated.connect(lambda: QtGui.QDesktopServices.openUrl(QUrl(self._currentArticleLink)))
        self.fullArticleLinkLabel.setText(f'<a style="color: inherit; text-decoration: inherit;" href="{self._currentArticleLink}">Open Full Article</a>')
        
        self.updateRecommendations()

    def likeButtonPressed(self):
        if not self.isLoggedIn():
            print("Attempt to like without registration")
            self.logInButtonPressed()
        else:
            response = self._client.sendRequest('LIKE', (self._currentUser, self._openedArticle))
            #TODO реакция на ответ сервера по запросу лайка
            print(f'Like {(self._currentUser)} -> {response}')

    def randomArticleButtonPressed(self):
        response = self._client.sendRequest('GET', ())
        print(f'Random article -> {response}')
        
    def recommendedArticleButtonPressed(self, article):
        response = self._client.sendRequest('GET', (self._currentUser))
        print(f'Recommended article -> {response}')
        
    def logInButtonPressed(self):
        logInDialog = LogInDialog()
        logInDialog.registerButton.clicked.connect(logInDialog.close)
        logInDialog.registerButton.clicked.connect(self.signInButtonPressed)

        if not logInDialog.exec():
            return
        
        nickname = logInDialog.nickname.text()
        password = logInDialog.password.text()
        response = self._client.sendRequest('LOGIN', (nickname, password))
        #TODO реакция на ответ сервера по запросу входа в аккаунт
        print(f'Log in {(nickname, password)} -> {response}')

    def signInButtonPressed(self):
        signInDialog = SignInDialog()

        if not signInDialog.exec():
            return
        
        nickname = signInDialog.nickname.text()
        password = signInDialog.password.text()
        response = self._client.sendRequest('REGISTER', (nickname, password))
            
        #TODO реакция на ответ сервера по запросу регистрации аккаунта
        print(f'Sign in {(nickname, password)} -> {response}')
