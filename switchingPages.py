# Вариант: 1

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QStackedWidget

# class TwoPageWidget(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.stacked_widget = QStackedWidget()  # Виджет с возможностью переключения страниц
#         self.page1 = QWidget()  # Первая страница
#         self.page2 = QWidget()  # Вторая страница

#         self.init_ui()

#     def init_ui(self):
#         self.setWindowTitle("Двустраничный виджет")

#         # Настройка содержимого первой страницы
#         layout1 = QVBoxLayout()
#         label1 = QLabel("Это первая страница")
#         self.resize(800, 600)
#         layout1.addWidget(label1)
#         self.page1.setLayout(layout1)
        

#         # Настройка содержимого второй страницы
#         layout2 = QVBoxLayout()
#         label2 = QLabel("Это вторая страница")
#         self.resize(800, 600)
#         layout2.addWidget(label2)
#         self.page2.setLayout(layout2)

#         # Добавление страниц в виджет с возможностью переключения
#         self.stacked_widget.addWidget(self.page1)
#         self.stacked_widget.addWidget(self.page2)

#         # Создание кнопки для переключения страниц
#         self.button = QPushButton("Переключить страницу")
#         self.button.clicked.connect(self.switch_page)

#         # Размещение виджета с возможностью переключения страниц и кнопки
#         layout = QVBoxLayout()
#         layout.addWidget(self.stacked_widget)
#         layout.addWidget(self.button)
#         self.setLayout(layout)

#     def switch_page(self):
#         current_index = self.stacked_widget.currentIndex()
#         if current_index == 0:
#             self.stacked_widget.setCurrentIndex(1)
#         else:
#             self.stacked_widget.setCurrentIndex(0)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     widget = TwoPageWidget()
#     widget.show()
#     sys.exit(app.exec_())



# Вариант: 2

# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget

# class MenuWidget(QWidget):
#     def __init__(self, stacked_widget):
#         super().__init__()

#         self.stacked_widget = stacked_widget

#         self.button1 = QPushButton("Page 1")
#         self.button1.clicked.connect(self.show_page1)
#         self.button2 = QPushButton("Page 2")
#         self.button2.clicked.connect(self.show_page2)
#         self.button3 = QPushButton("Page 3")
#         self.button3.clicked.connect(self.show_page3)

#         layout = QVBoxLayout()
#         layout.addWidget(self.button1)
#         layout.addWidget(self.button2)
#         layout.addWidget(self.button3)
#         self.setLayout(layout)

#     def show_page1(self):
#         self.stacked_widget.setCurrentIndex(0)

#     def show_page2(self):
#         self.stacked_widget.setCurrentIndex(1)

#     def show_page3(self):
#         self.stacked_widget.setCurrentIndex(2)

# class Page1(QWidget):
#     def __init__(self):
#         super().__init__()

#         label = QLabel("This is Page 1")

#         layout = QVBoxLayout()
#         layout.addWidget(label)
#         self.setLayout(layout)

# class Page2(QWidget):
#     def __init__(self):
#         super().__init__()

#         label = QLabel("This is Page 2")

#         layout = QVBoxLayout()
#         layout.addWidget(label)
#         self.setLayout(layout)

# class Page3(QWidget):
#     def __init__(self):
#         super().__init__()

#         label = QLabel("This is Page 3")

#         layout = QVBoxLayout()
#         layout.addWidget(label)
#         self.setLayout(layout)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     stacked_widget = QStackedWidget()
#     page1 = Page1()
#     page2 = Page2()
#     page3 = Page3()
#     stacked_widget.addWidget(page1)
#     stacked_widget.addWidget(page2)
#     stacked_widget.addWidget(page3)

#     menu_widget = MenuWidget(stacked_widget)

#     main_layout = QVBoxLayout()
#     main_layout.addWidget(menu_widget)
#     main_layout.addWidget(stacked_widget)

#     main_widget = QWidget()
#     main_widget.setLayout(main_layout)
#     main_widget.setWindowTitle("Menu Widget")

#     main_widget.show()
#     sys.exit(app.exec_())



# Вариант: 3

# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QLabel

# class MenuWidget(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.layout = QVBoxLayout()

#         self.button1 = QPushButton("Выбрать файл")
#         self.button1.clicked.connect(self.select_file)
#         self.layout.addWidget(self.button1)

#         self.button2 = QPushButton("Кнопка 2")
#         self.layout.addWidget(self.button2)

#         self.button3 = QPushButton("Кнопка 3")
#         self.layout.addWidget(self.button3)

#         self.button4 = QPushButton("Кнопка 4")
#         self.layout.addWidget(self.button4)

#         self.setLayout(self.layout)

#     def select_file(self):
#         file_dialog = QFileDialog()
#         file_path = file_dialog.getOpenFileName()[0]
#         if file_path:
#             self.button1.setText(file_path)

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.menu_widget = MenuWidget()

#         self.label = QLabel("Главное окно")
#         self.label.setAlignment(Qt.AlignCenter)

#         self.layout = QHBoxLayout()
#         self.layout.addWidget(self.menu_widget, 1)
#         self.layout.addWidget(self.label, 4)
#         self.layout.setContentsMargins(10, 10, 10, 10)
#         self.setLayout(self.layout)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())



# Вариант: 4 

# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QFileDialog

# class MenuWidget(QWidget):
#     def __init__(self, stack_widget):
#         super().__init__()

#         self.stack_widget = stack_widget
#         self.layout = QVBoxLayout()

#         self.button1 = QPushButton("Сканирование")
#         self.button1.clicked.connect(self.switch_to_page1)
#         self.layout.addWidget(self.button1)

#         self.button2 = QPushButton("О разработчиках")
#         self.button2.clicked.connect(self.switch_to_page2)
#         self.layout.addWidget(self.button2)

#         self.button3 = QPushButton("Страница 3")
#         self.button3.clicked.connect(self.switch_to_page3)
#         self.layout.addWidget(self.button3)

#         self.button4 = QPushButton("Закрыть")
#         self.button4.clicked.connect(self.switch_to_page4)
#         self.layout.addWidget(self.button4)

#         self.setLayout(self.layout)

#     def switch_to_page1(self):
#         self.stack_widget.setCurrentIndex(0)

#     def switch_to_page2(self):
#         self.stack_widget.setCurrentIndex(1)

#     def switch_to_page3(self):
#         self.stack_widget.setCurrentIndex(2)

#     def switch_to_page4(self):
#         self.stack_widget.setCurrentIndex(3)

# class Page1(QWidget):
#     def __init__(self):
#         super().__init__()
        

#         self.layout = QVBoxLayout()

#         self.file_button = QPushButton("Выбрать файл")
#         self.file_button.clicked.connect(self.select_file)
#         self.layout.addWidget(self.file_button)

#         self.setLayout(self.layout)

#     def select_file(self):
#         file_dialog = QFileDialog()
#         file_path = file_dialog.getOpenFileName()[0]
#         if file_path:
#             print(f"Выбран файл: {file_path}")

# class Page2(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.layout = QVBoxLayout()
#         self.button = QPushButton("Страница 2")
#         self.layout.addWidget(self.button)
#         self.setLayout(self.layout)

# class Page3(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.layout = QVBoxLayout()
#         self.button = QPushButton("Страница 3")
#         self.layout.addWidget(self.button)
#         self.setLayout(self.layout)

# class Page4(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.layout = QVBoxLayout()
#         self.button = QPushButton("Страница 4")
#         self.layout.addWidget(self.button)
#         self.setLayout(self.layout)

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.stack_widget = QStackedWidget()
#         self.page1 = Page1()
#         self.page2 = Page2()
#         self.page3 = Page3()
#         self.page4 = Page4()
#         self.stack_widget.addWidget(self.page1)
#         self.stack_widget.addWidget(self.page2)
#         self.stack_widget.addWidget(self.page3)
#         self.stack_widget.addWidget(self.page4)

#         self.menu_widget = MenuWidget(self.stack_widget)

#         self.layout = QHBoxLayout()
#         self.layout.addWidget(self.menu_widget, 1)
#         self.layout.addWidget(self.stack_widget, 4)
#         self.layout.setContentsMargins(10, 10, 10, 10)
#         self.setLayout(self.layout)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())



# Вариант: 5 Основной

# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QStackedWidget

# class ScanPage(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         self.layout = QVBoxLayout()
#         self.label = QLabel("Страница сканирования")
#         self.layout.addWidget(self.label)

#         self.setLayout(self.layout)

# class DevelopersPage(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         self.layout = QVBoxLayout()
#         self.label = QLabel("Страница о разработчиках")
#         self.layout.addWidget(self.label)

#         self.setLayout(self.layout)

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('BaohuMe')
#         self.resize(800, 600)

#         self.menu_layout = QVBoxLayout()
#         self.page_widget = QStackedWidget()

#         self.scan_button = QPushButton("Сканирование")
#         self.scan_button.clicked.connect(lambda: self.load_page(0))
#         self.menu_layout.addWidget(self.scan_button)

#         self.developers_button = QPushButton("О разработчиках")
#         self.developers_button.clicked.connect(lambda: self.load_page(1))
#         self.menu_layout.addWidget(self.developers_button)

#         self.close_button = QPushButton("Закрыть")
#         self.close_button.clicked.connect(self.close_program)
#         self.menu_layout.addWidget(self.close_button)

#         self.scan_page = ScanPage()
#         self.developers_page = DevelopersPage()

#         self.page_widget.addWidget(self.scan_page)
#         self.page_widget.addWidget(self.developers_page)

#         self.layout = QHBoxLayout()
#         self.layout.addLayout(self.menu_layout)
#         self.layout.addWidget(self.page_widget)

#         self.setLayout(self.layout)

#     def load_page(self, page_num):
#         self.page_widget.setCurrentIndex(page_num)

#     def close_program(self):
#         QApplication.quit()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())



# Вариант: 6

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget, QMessageBox, QFileDialog

class ScanPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.layout = QVBoxLayout()
        self.label = QLabel("Страница сканирования")
        self.layout.addWidget(self.label)

        self.file_button = QPushButton("Выбрать файл")
        self.file_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.file_button)

        self.setLayout(self.layout)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл", "", "All Files (*)")
        if file_path:
            self.label.setText(f"Выбран файл: {file_path}")

class AboutPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.label = QLabel("Страница 'О разработчиках'")
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('BaohuMe')
        self.resize(800, 600)

        self.menu_layout = QVBoxLayout()
        self.page_widget = QStackedWidget()

        self.scan_button = QPushButton("Сканирование")
        self.scan_button.clicked.connect(self.load_scan_page)
        self.menu_layout.addWidget(self.scan_button)

        self.about_button = QPushButton("О разработчиках")
        self.about_button.clicked.connect(self.load_about_page)
        self.menu_layout.addWidget(self.about_button)

        self.close_button = QPushButton("Закрыть")
        self.close_button.clicked.connect(self.close_app)
        self.menu_layout.addWidget(self.close_button)

        self.scan_page = ScanPage()
        self.about_page = AboutPage()

        self.page_widget.addWidget(self.scan_page)
        self.page_widget.addWidget(self.about_page)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.menu_layout)
        self.layout.addWidget(self.page_widget)

        self.setLayout(self.layout)

    def load_scan_page(self):
        self.page_widget.setCurrentWidget(self.scan_page)

    def load_about_page(self):
        self.page_widget.setCurrentWidget(self.about_page)

    def close_app(self):
        confirm = QMessageBox.question(self, 'Подтверждение', 'Вы уверены, что хотите закрыть?',
                                       QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.Yes:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



# Вариант: 7 Взять текстовые блоки

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog


# class ScanPage(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.layout = QVBoxLayout()
#         self.label = QLabel("Для начала сканирования, выберите файл")
#         self.layout.addWidget(self.label)

#         self.file_button = QPushButton("Выбрать файл")
#         self.file_button.clicked.connect(self.select_file)
#         self.layout.addWidget(self.file_button)

#         self.setLayout(self.layout)

#     def select_file(self):
#         options = QFileDialog.Options()
#         options |= QFileDialog.ReadOnly
#         file, _ = QFileDialog.getOpenFileName(self, "Выберите файл для сканирования", "",
#                                               "Все файлы (*)", options=options)
#         if file:
#             print("Выбран файл:", file)


# class AboutPage(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.layout = QVBoxLayout()
#         self.label = QLabel("Информация о разработчиках:")
#         self.layout.addWidget(self.label)

#         self.developer1 = QLabel("Имя разработчика 1")
#         self.layout.addWidget(self.developer1)

#         self.developer2 = QLabel("Имя разработчика 2")
#         self.layout.addWidget(self.developer2)

#         self.setLayout(self.layout)


# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.menu_layout = QVBoxLayout()
#         self.page_widget = QWidget()

#         self.scan_button = QPushButton("Сканирование")
#         self.scan_button.clicked.connect(self.load_scan_page)
#         self.menu_layout.addWidget(self.scan_button)

#         self.about_button = QPushButton("О разработчиках")
#         self.about_button.clicked.connect(self.load_about_page)
#         self.menu_layout.addWidget(self.about_button)

#         self.close_button = QPushButton("Закрыть")
#         self.close_button.clicked.connect(self.close_app)
#         self.menu_layout.addWidget(self.close_button)

#         self.scan_page = ScanPage()
#         self.about_page = AboutPage()

#         self.page_layout = QVBoxLayout()
#         self.page_layout.addWidget(self.scan_page)
#         self.page_layout.addWidget(self.about_page)

#         self.page_widget.setLayout(self.page_layout)

#         self.layout = QVBoxLayout()
#         self.layout.addLayout(self.menu_layout)
#         self.layout.addWidget(self.page_widget)

#         self.setLayout(self.layout)

#     def load_scan_page(self):
#         self.page_layout.setCurrentWidget(self.scan_page)

#     def load_about_page(self):
#         self.page_layout.setCurrentWidget(self.about_page)

#     def close_app(self):
#         self.close()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


