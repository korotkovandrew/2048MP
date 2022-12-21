# QtWidget for main window to display label and button to return id of article to open to main window
# class stores id of article and its title

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class RecommendationWidget(QWidget):
    def __init__(self, articleID: int, articleTitle: str):
        super().__init__()
        
        self.articleID: int = articleID
        self.articleTitle: str = articleTitle
        self.initUI()
        
    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(5)
        self.setLayout(self.layout)
        
        self.label = QLabel(self.articleTitle)
        self.label.setStyleSheet('color: #315ae3; background-color: #303134; border-radius: 2px; padding: 10px;')
        self.label.setWordWrap(True)
        self.label.setMaximumWidth(260) 
        self.label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        
        self.layout.addWidget(self.label)
        
        self.button = QPushButton('Open')
        
        self.layout.addWidget(self.button)