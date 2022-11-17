from PyQt5.QtWidgets import QApplication
import sys

sys.path.insert(1, './src')
from MainWindow import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
