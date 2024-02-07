from PyQt5.QtWidgets import QApplicatoin
from app import mainwindow

if __name__ == "__main__":
    app = QApplicatoin([])
    mw = mainwindow.MainWindow()
    app.exec_()
