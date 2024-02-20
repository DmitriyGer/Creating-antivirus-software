import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QStackedWidget, QMessageBox, QFileDialog, QScrollArea

from helpers import database
from app import del_malwer

""" Страница сканирования"""
class ScanPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        """Текст в блоке 'Страница' """
        self.layout = QVBoxLayout()
        self.label = QLabel("Страница сканирования\n")
        self.layout.addWidget(self.label)
       
        """ Кнопка 'Выбора файла' """
        self.file_button = QPushButton("Выбрать файл")
        self.file_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.file_button)

        self.setLayout(self.layout)
        

    """ Функция выбора файла """
    def select_file(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.ReadOnly
        file, _ = QFileDialog.getOpenFileName(self, "Выберите файл для сканирования", "", "Все файлы (*)", options=options)
        if file:
            print("Выбран файл:", file)   
            self.show_testing_page(file)         
            

    """ Функция вызова стр. тест """
    def show_testing_page(self, file):
        data = database.git_info_files(file)
        name_file = file.split("/")[-1]
        self.label.setText(f"Выбранный файл: {name_file}")
        
        """ Перебор по БД, обнаружение кол-во срабатываний """
        return_scan = 0
        for name in data:
            if data[name]['result'] != None:
                return_scan += 1

        """ Вывод результатов сканирования пользователю """
        if len(data) == 0:
            self.label.setText("Запрос создан, ожидайте ...")
        else:
            if return_scan == 0:
                self.label.setText(f"В файле {name_file} угрозы не обнаружены")
            else:
                self.label.setText(f"В файле {name_file} обнаружена угроза")
                # self.dm = del_malwer.WarningWindow(file)
                # del_malwer(file)

    """ Функция удаления файла """
    def del_malwer(self, file):
        confirm = QMessageBox.question(self, 'BaohuMe - Подтверждение', 'Вы действительно хотите удалить файл?', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            os.remove(file)
            


""" Страница о разработчиках """
class DevelopersPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.label = QLabel("Страница о разработчиках")
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)


""" Основной класс """
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('BaohuMe')
        self.resize(800, 500)

        self.menu_layout = QVBoxLayout()
        self.page_widget = QStackedWidget()

        self.scan_button = QPushButton("Сканирование")
        self.scan_button.clicked.connect(lambda: self.load_page(0))
        self.menu_layout.addWidget(self.scan_button)

        self.developers_button = QPushButton("О разработчиках")
        self.developers_button.clicked.connect(lambda: self.load_page(1))
        self.menu_layout.addWidget(self.developers_button)

        self.close_button = QPushButton("Закрыть")
        self.close_button.clicked.connect(self.close_app)
        self.menu_layout.addWidget(self.close_button)

        self.scan_page = ScanPage()
        self.developers_page = DevelopersPage()

        self.page_widget.addWidget(self.scan_page)
        self.page_widget.addWidget(self.developers_page)

        self.layout = QHBoxLayout()
        self.layout.addLayout(self.menu_layout)
        self.layout.addWidget(self.page_widget)

        self.setLayout(self.layout)

    def load_page(self, page_num):
        self.page_widget.setCurrentIndex(page_num)


    """ Закрытие программы """
    def close_app(self):
        confirm = QMessageBox.question(self, 'Подтверждение', 'Вы уверены, что хотите закрыть?', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
