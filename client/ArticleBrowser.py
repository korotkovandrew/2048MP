from PyQt5.QtWidgets import QApplication
import sys

from src.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    
    sys.exit(app.exec())
