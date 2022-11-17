from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QDialog, QApplication

class SignInDialog(QDialog):
    def __init__(self):
        super(SignInDialog, self).__init__()
        uic.loadUi('./src/ui/signInDialog.ui', self)
        
        self.setWindowIcon(QtGui.QIcon('./img/AB_icon.ico'))
        
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordRepeat.setEchoMode(QtWidgets.QLineEdit.Password)
        self.acceptButton.clicked.connect(self.accept)
        
        self.show()