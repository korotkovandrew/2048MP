from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QDialog, QApplication

from src.regexpPatterns import *
import re

class LogInDialog(QDialog):
    def __init__(self):
        super(LogInDialog, self).__init__()
        uic.loadUi('./src/ui/loginDialog.ui', self)
        self.setWindowIcon(QtGui.QIcon('./img/AB_icon.ico'))
        
        self.registerButton.clicked.connect(self.reject) 
        
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.acceptButton.clicked.connect(self.initialInputValidation)
        
        self.show()

    #TODO сделать alert'ы с ошибкой
    def initialInputValidation(self):
        if not re.fullmatch(NICKNAME_RE_PATTERN, self.nickname.text()):
            self.reject()
            print(NICKNAME_VALIDATION_ERROR_MESSAGE)
        elif not re.fullmatch(PASSWORD_RE_PATTERN, self.password.text()):
            self.reject()
            print(PASSWORD_VALIDATION_ERROR_MESSAGE)
        else:
            self.accept()