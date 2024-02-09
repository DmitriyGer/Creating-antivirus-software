from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea, QLabel
)

from PyQt5.QtCore import Qt
from helpers import database

class TestWin(QWidget):
    def __init__(self, cur_file):
        super().__init__()
        self.cur_file = cur_file
        self.set_win()
        self.initUI()
        self.show()

    """ Настройка экрана """
    def set_win(self):
        self.setWindowTitle("BaohuMe - Окно сканирования")
        self.resize(700, 500)
    
    """ Создание виджета и направляющих """
    def initUI(self):
        layout = QVBoxLayout()
        s_a = QScrollArea(self)


        """ Объявление базы данных """
        data = database.git_info_files(self.cur_file)


        # """ Построчный перебор по базе данных и вывод результатов сканирования """
        # if len(data) == 0:
        #     label = QLabel("Запрос создан, ожидайте ...")
        #     layout.addWidget(label, alignment=Qt.AlignCenter)
        # else:
        #     for name in data:
        #         result = f"Антивирус: {name}\n Результат: {data[name]['result']}\n"
        #         label = QLabel(result)
        #         layout.addWidget(label, alignment=Qt.AlignCenter)


        """ Название сканируемого файла """
        name_file = self.cur_file.split("/")[-1]


        """ Перебор по БД обнаружение кол-во срабатываний """
        return_scan = 0
        for name in data:
            if data[name]['result'] != None:
                return_scan += 1


        """ Вывод результатов сканирования пользователю """
        if len(data) == 0:
            label = QLabel("Запрос создан, ожидайте ...")
            layout.addWidget(label, alignment=Qt.AlignCenter)
        else:
            if return_scan == 0:
                result = f"В файле {name_file} угрозы не обнаружены"
                label = QLabel(result)
                layout.addWidget(label, alignment=Qt.AlignCenter)
            else:
                result = f"В файле {name_file} обнаружена угроза"
                label = QLabel(result)
                layout.addWidget(label, alignment=Qt.AlignCenter)
                

        """ Проверка работы вывода алгоритма. Простой список от 1 до 100 """
        # for i in range(100):
        #     label = QLabel(f"Строка номер {i}")
        #     layout.addWidget(label, alignment=Qt.AlignCenter) 

        content_widget = QWidget()
        content_widget.setLayout(layout)

        s_a.setWidget(content_widget)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(s_a)