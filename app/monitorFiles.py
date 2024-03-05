import os, time
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea, QLabel
)

from PyQt5.QtCore import Qt

class TestWin(QWidget):
    def __init__(self, cur_file):
        super().__init__()
        self.cur_file = cur_file
        self.set_win()
        self.monitoring_Folders()
        self.initUI()
        self.show()

    """ Настройка экрана """
    def set_win(self):
        self.setWindowTitle("BaohuMe - Окно сканирования")
        self.resize(700, 500)
    
        """ Функция для обнаружения добавленных файлов """
    def monitoring_Folders(self):
        layout = QVBoxLayout()
        print('Start_real_time_scan')
        # Считывание путей к папкам из файла Folder.txt
        folder_paths = []
        with open('helpers\database_local.txt', 'r') as file:
            for line in file:
                folder_paths.append(line.strip())

        # Словарь для хранения списка файлов в каждой папке на старте
        initial_files = {folder_path: os.listdir(folder_path) for folder_path in folder_paths}

        # Основной цикл программы
        while True:
            for folder_path in folder_paths:
                current_files = os.listdir(folder_path)

                # Поиск новых файлов
                new_files = [file for file in current_files if file not in initial_files[folder_path]]

                # Вывод сообщения при обнаружении нового файла
                for new_file in new_files:
                    result = (f"Новый файл обнаружен в папке {folder_path}: {new_file}")
                    label = QLabel(result)
                    layout.addWidget(label, alignment=Qt.AlignCenter)
                    print(f"Новый файл обнаружен в папке {folder_path}: {new_file}")

                initial_files[folder_path] = current_files

            time.sleep(5)  # Проверка каждые 5 секунд


    """ Создание виджета и направляющих """
    def initUI(self):
        layout = QVBoxLayout()
        s_a = QScrollArea(self)

        # """ Название сканируемого файла """
        # name_file = self.cur_file.split("/")[-1]


        # """ Перебор по БД, обнаружение кол-во срабатываний """
        # return_scan = 0
        # for name in data:
        #     if data[name]['result'] != None:
        #         return_scan += 1


        # """ Вывод результатов сканирования пользователю """
        # if len(data) == 0:
        #     label = QLabel("Запрос создан, ожидайте ...")
        #     layout.addWidget(label, alignment=Qt.AlignCenter)
        # else:
        #     if return_scan == 0:
        #         result = f"В файле {name_file} угрозы не обнаружены"
        #         label = QLabel(result)
        #         layout.addWidget(label, alignment=Qt.AlignCenter)
        #     else:
        #         result = f"В файле {name_file} обнаружена угроза"
        #         label = QLabel(result)
        #         layout.addWidget(label, alignment=Qt.AlignCenter)
        #         self.dm = del_malwer.WarningWindow(self.cur_file)


    
                
    

        """ Проверка работы вывода алгоритма. Простой список от 1 до 100 """
        # for i in range(100):
        #     label = QLabel(f"Строка номер {i}")
        #     layout.addWidget(label, alignment=Qt.AlignCenter) 

        content_widget = QWidget()
        content_widget.setLayout(layout)

        s_a.setWidget(content_widget)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(s_a)
        
    