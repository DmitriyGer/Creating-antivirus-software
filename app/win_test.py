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

    def set_win(self):
        """ Настройка экрана """
        self.setWindowTitle("BaohuMe - Окно сканирования")
        self.resize(500, 400)
    
    def initUI(self):
        """ Создание виджета и направляющих """
        layout = QVBoxLayout()

        s_a = QScrollArea(self)

        data = database.git_info_files(self.cur_file)

        if len(data) == 0:
            label = QLabel("Запрос создан, ожидайте ...")
            layout.addWidget(label, alignment=Qt.AlignCenter)
        else:
            for name in data:
                result = f"Антивирус: {name}\n Результат: {data[name]['result']}\n"
                label = QLabel(result)
                layout.addWidget(label, alignment=Qt.AlignCenter)

        # for i in range(100):
        #     label = QLabel(f"Строка номер {i}")
        #     layout.addWidget(label, alignment=Qt.AlignCenter) 

        content_widget = QWidget()
        content_widget.setLayout(layout)

        s_a.setWidget(content_widget)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(s_a)



    