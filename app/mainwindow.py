from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, 
    QFileDialog, QApplication
)
from PyQt5.QtCore import Qt
from app import win_test

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.set_win()
        self.initUI()
        self.connects()
        self.show()

    def set_win(self):
        '''Нвстройка экрана'''
        self.setWindowTitle('BaohuMe')
        self.resize(800, 600)

    def initUI(self):
        '''Создание виджетов и направляющих'''
        layout = QVBoxLayout()

        self.b_malware = QPushButton('Сканировать файл')
        self.b_exit = QPushButton('Выход')

        layout.addWidget(self.b_malware, alignment = Qt.AlignCenter)
        layout.addWidget(self.b_exit, alignment = Qt.AlignCenter)
        
        self.setLayout(layout)

    def connects(self):
        '''Подключение события'''
        self.b_malware.clicked.connect(self.click_malware)
        self.b_exit.clicked.connect(QApplication.quit)
    
    def click_malware(self):
        self.cur_file = QFileDialog.getOpenFileName()[0]
        if not self.cur_file == "":
            self.tw = win_test.TestWin(self.cur_file)
        