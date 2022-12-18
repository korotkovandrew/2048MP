from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog

from src.ClientSocket.Sender import Sender
from src.Requests import *

class MainWindow(Sender, QMainWindow):
    def __init__(self, 
                 serverIP: str, 
                 serverPort: int, 
                 currentUser: str):
        
        Sender.__init__(self, serverIP, serverPort)
        QMainWindow.__init__(self)

        self.initUI(currentUser)
        self.initSignals()
        
        response = self.send(GET(currentUser, True))
        if response['code'] != '':
            self.alert(True, response['code'])
            self.close()
        elif response['liked']:
            self.showLiked()
        
        self.currentArticleID: int = response['articleID']
        self.articleTitleLabel.setText(response['articleData']['title'])
        self.articleText.setText(response['articleData']['content'])

    def initAlertWindow(self):
        self.alertWindow = QDialog()
        uic.loadUi('src/ui/Alert.ui', self.alertWindow)
        self.alertWindow.message.setText('...')

    def initUI(self, username: str):
        self.initAlertWindow()
        
        uic.loadUi('src/ui/MainWindow.ui', self)
        self.setWindowTitle('Article Browser')
        self.setWindowIcon(QIcon('./src/ui/ico/Ab_icon.ico'))
        
        self.articleTitleLabel.setText('NO ARTICLE OPENED')
        self.articleText.setText('')
        self.nicknameLabel.setText(username)
        self.likeButton.setText('♥')
        
            
    def initSignals(self):
        self.randomArticleButton.clicked.connect(self.randomArticleSignal)
        self.likeButton.clicked.connect(self.likeSignal)
    
    def showLiked(self, liked: bool = True):
        if liked:
            self.likeButton.setEnabled(False)
            self.likeButton.setStyleSheet('background-color: #E74C3C;')
        else:
            self.likeButton.setEnabled(True)
            self.likeButton.setStyleSheet('background-color: #303134;')

    def randomArticleSignal(self):
        if self.nicknameLabel.text() == '':
            self.alert(True, 'You are not logged in')
            return
        response = self.send(GET(self.nicknameLabel.text(), True))
        if response['code']:
            self.alert(True, response['code'])
            return
        
        self.currentArticleID = response['articleID']
        self.articleTitleLabel.setText(response['articleData']['title'])
        self.articleText.setText(response['articleData']['content'])
        self.showLiked(response['liked'])
        
    def likeSignal(self):
        if self.nicknameLabel.text() == '':
            self.alert(True, 'You are not logged in')
            return
        if self.currentArticleID == 0:
            self.alert(True, 'You have not opened any article')
            return
        
        response = self.send(LIKE(self.nicknameLabel.text(), 
                                  self.currentArticleID))
        if response['code'] == '':
            self.showLiked(True)

    def alert(self, critical: bool, message: str):
        self.setEnabled(False)
        self.alertWindow.message.setText(message)
        if critical:
            self.alertWindow.setWindowIcon(QIcon('src/ui/ico/critical.ico'))
        else:
            self.alertWindow.setWindowIcon(QIcon('src/ui/ico/info.ico'))
        self.alertWindow.exec_()
        self.setEnabled(True)
            