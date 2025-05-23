import os
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QLabel, QApplication
)
from PyQt5.QtCore import Qt

class WarningWindow(QWidget):
    def __init__(self, cur_file):
        super().__init__()
        self.cur_file = cur_file
        self.set_win()
        self.initUI()
        self.connects()
        self.show()

    def set_win(self):
        '''Нвстройка экрана'''
        self.setWindowTitle('BaohuMe - Внимание, угроза!')
        self.resize(600, 400)


    """ Создание виджета и направляющих """
    def initUI(self):
        layout = QVBoxLayout()

        """ Работа над кнопками "Удалить" или "Игнорировать" """
        self.delite = QPushButton('Удалить')
        self.ignore = QPushButton('Игнорировать')

        layout.addWidget(self.delite, alignment = Qt.AlignLeft)
        layout.addWidget(self.ignore, alignment = Qt.AlignRight)

        self.setLayout(layout)


    """ Подключение событий """
    def connects(self):
        self.delite.clicked.connect(self.click_delite)
        self.ignore.clicked.connect(QApplication.quit)

    
    """ Функция удаления файла """
    def click_delite(self):
        layout = QVBoxLayout()
        os.remove(self.cur_file)
        result = "Угроза успешно удалена"
        label = QLabel(result)
        layout.addWidget(label, alignment=Qt.AlignCenter)
        

    
    # """ Функция для игнорирования угрозы """
    # def click_ignore(self):
    #     self.ignore.clicked.connect(QApplication.quit)