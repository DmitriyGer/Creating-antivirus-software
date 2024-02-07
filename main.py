from PyQt5.QtWidgets import QApplication
from app import mainwindow

if __name__ == "__main__":
    app = QApplication([])
    mw = mainwindow.MainWindow()
    app.exec_()
