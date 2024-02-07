from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, 
    QFileDialog
)
from PyQt5.QtCore import Qt
from app import win_test

class mainwindow(QWidget):
    def _init_(self):
        super()._init_()
        self.set_win()
        self.initUI()
        self.connects()
        self.show()

    def set_win(self):
        '''Нвстройка экрана'''
        self.setWindowTitle('Моя первоя программа')
        self.resize(800, 600)

    def initUI(self):
        '''Создание виджетов и направляющих'''
        layout = QVBoxLayout()

        self.b_malware = QPushButton('Сканировать файл')
        self.b_exit = QPushButton('Выход')

        layout.addwidget(self.b_malware, alignment = Qt.Alignmenter)
        layout.addwidget(self.b_exit, alignment = Qt.Alignmenter)
        
        self.setLayout(layout)

    def connects(self):
        '''Подключение события'''
        self.b_malware.clicked.connect(self.click_malware)
    
    def click_malware(self):
        self.cur_tile = QFileDialog.getOpenFileName()[0]