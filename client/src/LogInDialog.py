from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QDialog, QApplication

class LogInDialog(QDialog):
    def __init__(self):
        super(LogInDialog, self).__init__()
        uic.loadUi('./src/ui/loginDialog.ui', self)
        
        self.setWindowIcon(QtGui.QIcon('./img/AB_icon.ico'))
        
        self.registerButton.clicked.connect(self.rejected)
        
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.acceptButton.clicked.connect(self.accept)
        
        self.show()
