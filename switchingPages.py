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

# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget, QMessageBox, QFileDialog

# class ScanPage(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         self.layout = QVBoxLayout()
#         self.label = QLabel("Страница сканирования")
#         self.layout.addWidget(self.label)

#         self.file_button = QPushButton("Выбрать файл")
#         self.file_button.clicked.connect(self.select_file)
#         self.layout.addWidget(self.file_button)

#         self.setLayout(self.layout)

#     def select_file(self):
#         file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл", "", "All Files (*)")
#         if file_path:
#             self.label.setText(f"Выбран файл: {file_path}")

# class AboutPage(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.layout = QVBoxLayout()
#         self.label = QLabel("Страница 'О разработчиках'")
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

#         self.page_widget.addWidget(self.scan_page)
#         self.page_widget.addWidget(self.about_page)

#         self.layout = QVBoxLayout()
#         self.layout.addLayout(self.menu_layout)
#         self.layout.addWidget(self.page_widget)

#         self.setLayout(self.layout)

#     def load_scan_page(self):
#         self.page_widget.setCurrentWidget(self.scan_page)

#     def load_about_page(self):
#         self.page_widget.setCurrentWidget(self.about_page)

#     def close_app(self):
#         confirm = QMessageBox.question(self, 'Подтверждение', 'Вы уверены, что хотите закрыть?',
#                                        QMessageBox.Yes | QMessageBox.No)

#         if confirm == QMessageBox.Yes:
#             self.close()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


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


# """ Для отслеживания файлов """

# import os
# import time

# # Список папок, которые нужно отслеживать
# folder_paths = ['C:\\Users\\dim1a\\Desktop\\TestFolder']

# # Словарь для хранения списка файлов в каждой папке на старте
# initial_files = {folder_path: os.listdir(folder_path) for folder_path in folder_paths}

# # Основной цикл программы
# while True:
#     for folder_path in folder_paths:
#         current_files = os.listdir(folder_path)

#         # Поиск новых файлов
#         new_files = [file for file in current_files if file not in initial_files[folder_path]]

#         # Вывод сообщения при обнаружении нового файла
#         for new_file in new_files:
#             print(f"Новый файл обнаружен в папке {folder_path}: {new_file}")

#         initial_files[folder_path] = current_files

#     time.sleep(5)  # Проверка каждые 5 секунд


""" Готовая версия проги для отслеживания файлов """

# import os
# import time

# # Считывание путей к папкам из файла Folder.txt
# folder_paths = []
# with open('helpers\database_local.txt', 'r') as file:
#     for line in file:
#         folder_paths.append(line.strip())

# # Словарь для хранения списка файлов в каждой папке на старте
# initial_files = {folder_path: os.listdir(folder_path) for folder_path in folder_paths}

# # Основной цикл программы
# while True:
#     for folder_path in folder_paths:
#         current_files = os.listdir(folder_path)

#         # Поиск новых файлов
#         new_files = [file for file in current_files if file not in initial_files[folder_path]]

#         # Вывод сообщения при обнаружении нового файла
#         for new_file in new_files:
#             print(f"Новый файл обнаружен в папке {folder_path}: {new_file}")

#         initial_files[folder_path] = current_files

#     time.sleep(5)  # Проверка каждые 5 секунд


# import os, time

# def track_folders():
#     # Считывание путей к папкам из файла Folder.txt
#     folder_paths = []
#     with open('Folder.txt', 'r') as file:
#         for line in file:
#             folder_paths.append(line.strip())

#     # Словарь для хранения списка файлов в каждой папке на старте
#     initial_files = {folder_path: os.listdir(folder_path) for folder_path in folder_paths}

#     while True:
#         for folder_path in folder_paths:
#             current_files = os.listdir(folder_path)

#             # Поиск новых файлов
#             new_files = [file for file in current_files if file not in initial_files[folder_path]]

#             # Вывод сообщения при обнаружении нового файла
#             for new_file in new_files:
#                 print(f"Новый файл обнаружен в папке {folder_path}: {new_file}")

#             initial_files[folder_path] = current_files

#         # Добавить задержку перед повторной проверкой
#         # Можно изменить интервал по необходимости
#         time.sleep(5)  # Проверка каждые 5 секунд

# # Вызов функции для отслеживания изменений в папках
# track_folders()


""" Прога для обнаружения нового файла """
# import sys
# import os
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt5.QtCore import QFileSystemWatcher

# class VirusScanner(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Real-Time Virus Scanner')
#         self.setGeometry(100, 100, 300, 100)

#         self.label = QLabel(self)
#         self.label.setGeometry(10, 10, 300, 30)
#         self.label.setText('Watching for new files...')

#         self.watcher = QFileSystemWatcher()
#         self.watcher.directoryChanged.connect(self.directory_changed)


#         # Путь к папке для сканирования
#         folder_to_scan = "C:\\Users\\dim1a\\Desktop\\TestFolder"
#         self.watcher.addPath(folder_to_scan)

#     def directory_changed(self, path):
#         new_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
#         if new_files:
#             for new_file in new_files:
#                 print(f"Добавлен новый файл: {new_file}")
#                 self.label.setText(f"Добавлен новый файл: {new_file}")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     scanner = VirusScanner()
#     scanner.show()
#     sys.exit(app.exec_())


""" Прога для обнаружения нового файла  """
# import sys
# import os
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
# from PyQt5.QtCore import QFileSystemWatcher

# class RealTimeFolderMonitor(QWidget):
#     def __init__(self, folder_path):
#         super().__init__()

#         self.setWindowTitle('Real-Time Folder Monitor')
#         self.setGeometry(100, 100, 400, 300)

#         self.layout = QVBoxLayout()
#         self.setLayout(self.layout)

#         self.folder_path = folder_path
#         self.new_files_label = QLabel('New Files:')
#         self.layout.addWidget(self.new_files_label)

#         self.file_watcher = QFileSystemWatcher()
#         self.file_watcher.directoryChanged.connect(self.directory_changed)
#         self.file_watcher.addPath(folder_path)

#     def directory_changed(self, path):
#         new_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
#         print(new_files)
#         # self.new_files_label.clear()
#         if new_files:
#             for new_file in new_files:
#                 self.new_files_label.setText(self.new_files_label.text() + f'\n{new_file}')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     folder_to_monitor = "C:\\Users\\dim1a\\Desktop\\TestFolder"  # Укажите путь к папке, которую нужно анализировать
#     folder_monitor = RealTimeFolderMonitor(folder_to_monitor)
#     folder_monitor.show()
#     sys.exit(app.exec_())


""" Уже чтот лучше """

# import sys
# import os
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
# from PyQt5.QtCore import QTimer

# class RealTimeFolderAnalyzer(QWidget):
#     def __init__(self, folder_path):
#         super().__init__()

#         self.setWindowTitle('Real-Time Folder Analyzer')
#         self.setGeometry(100, 100, 400, 300)

#         self.layout = QVBoxLayout()
#         self.setLayout(self.layout)

# self.folder_path = folder_path
# self.last_added_file_label = QLabel('Последний добавленный файл: ')
# self.layout.addWidget(self.last_added_file_label)

# self.last_added_file = ''
# self.timer = QTimer()
# self.timer.timeout.connect(self.check_for_new_file)
# self.timer.start(1000)  # Проверять наличие нового файла каждую секунду

#     def check_for_new_file(self):
#         files = [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]
#         files.sort(key=lambda x: os.path.getctime(os.path.join(self.folder_path, x)), reverse=True)
#         print(files)

#         if files:
#             latest_file = files[0]
#             if latest_file != self.last_added_file:
#                 self.last_added_file = latest_file
#                 self.last_added_file_label.setText(f'Последний добавленный файл: {self.last_added_file}')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     folder_to_analyze = "C:\\Users\\dim1a\\Desktop\\TestFolder"  # Укажите путь к папке, которую нужно анализировать
#     folder_analyzer = RealTimeFolderAnalyzer(folder_to_analyze)
#     folder_analyzer.show()
#     sys.exit(app.exec_())


# import os
# import hashlib
# import sys
# import time

# file_list = []

# rootdir = "C:\\Users\\dim1a\\Desktop\\TestFolder"

# print("Program starting!")
# print("[+]Collecting virus definitions and allocating memory[+]")

# for subdir, dirs, files in os.walk(rootdir):
#     for file in files:
#         #print os.path.join(subdir, file)
#         filepath = subdir + os.sep + file

#         if filepath.endswith(".exe") or filepath.endswith(".dll"):
#             file_list.append(filepath)
#             #print(filepath)

# print("[+]Virus definition and memory allocation complete...[+]")
# print("[+]Starting scan...[+]")
# def countdown():
#     for x in range(4):
#         print(x+1)
#         time.sleep(1)

# countdown()

# def Scan():
#     infected_list = []
#     for f in file_list:
#         virus_defs = open("VirusLIST.txt", "r")
#         file_not_read = False
#         print("\nScanning: {}".format(f))
#         hasher = hashlib.md5()
#         try:
#             with open(f, "rb") as file:
#                 try:
#                     buf = file.read()
#                     file_not_read = True
#                     hasher.update(buf)
#                     FILE_HASHED = hasher.hexdigest()
#                     print("File md5 checksum: {}".format(FILE_HASHED))
#                     for line in virus_defs:
#                         if FILE_HASHED == line.strip():
#                             print("[!]Malware Detected[!] | File name: {}".format(f))
#                             infected_list.append(f)
#                         else:
#                             pass
#                 except Exception as e:
#                     print("Could not read file | Error: {}".format(e))
#         except:
#             pass
#     print("Infected files found: {}".format(infected_list))
#     deleteornot = str(input("Would you like to delete the infected files (y/n): "))
#     if deleteornot.upper() == "Y":
#         for infected in infected_list:
#             os.remove(infected)
#             print("File removed: {}".format(infected))
#     else:
#         print("Executed with exit code 0")
#         os.system("PAUSE")
# Scan()


""" Проверка файла черех хеширование НУЖНО """
# import hashlib

# # Создаем базу данных с хешами безопасных файлов
# safe_files = {
#     "file1.exe": "c3812211b7b4ab8fc631509980c091b833091ebf6f5f461aaf0a23cc4345733a",
#     "file2.exe": "z9y8x7w6v5u4t3s2r1",
#     # Добавьте сюда остальные файлы
# }

# def check_file(file_name):
#     # Читаем содержимое файла
#     with open(file_name, "rb") as file:
#         content = file.read()

#     # Хешируем содержимое файла
#     hash_obj = hashlib.sha256()
#     hash_obj.update(content)
#     file_hash = hash_obj.hexdigest()

#     # Проверяем, есть ли хеш в базе безопасных файлов
#     if file_hash in safe_files.values():
#         print(f"The file {file_name} is safe.")
#     else:
#         print(f"The file {file_name} may be a threat.")

# # Пример использования
# check_file("virus2")
# # check_file("file3.exe")  # Предположительно вредоносный файл


""" Перевод файла в хеш код НУЖНО """
# import hashlib

# def calculate_file_hash(file_path):
#     sha256_hash = hashlib.sha256()
#     with open(file_path, "rb") as f:
#         for byte_block in iter(lambda: f.read(4096), b""):
#             sha256_hash.update(byte_block)
#     return sha256_hash.hexdigest()

# def check_file_integrity(file_path, expected_hash):
#     file_hash = calculate_file_hash(file_path)
#     if file_hash == expected_hash:
#         print(f"The file {file_path} is intact.")
#     else:
#         print(f"The file {file_path} has been modified.")
#         print(f"Expected hash: {expected_hash}")
#         print(f"Actual hash: {file_hash}")

# file_path = "file1.exe"
# expected_hash = "your_expected_hash"

# check_file_integrity(file_path, expected_hash)

""" Перевод из хещ кода в текст НЕ РАБОЧИЙ """
# hash_code = 1234567890
# text = bytes.fromhex(hex(hash_code)[2:]).decode('utf-8')
# print(text)


""" Перевод текста в хеш """
# import hashlib

# def sha256_hash(text):
#     sha256 = hashlib.sha256()
#     sha256.update(text.encode('utf-8'))
#     return sha256.hexdigest()

# text = "file1.exe"
# hash_code = sha256_hash(text)

# print(f"Text: {text}")
# print(f"SHA-256 Hash: {hash_code}")


# import sys
# import os
# import hashlib
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog, QMessageBox

# class ThreatChecker(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Threat Checker')
#         self.setGeometry(100, 100, 300, 200)

#         self.btn_select_folder = QPushButton('Select Folder', self)
#         self.btn_select_folder.clicked.connect(self.selectFolder)

#         self.lbl_result = QLabel('', self)

#         layout = QVBoxLayout()
#         layout.addWidget(self.btn_select_folder)
#         layout.addWidget(self.lbl_result)

#         self.setLayout(layout)

#     def selectFolder(self):
#         folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
#         if folder_path:
#             threat = self.checkFolder(folder_path)
#             if threat:
#                 self.lbl_result.setText('Threat Detected!')
#             else:
#                 self.lbl_result.setText('No Threat Detected')

#     def checkFolder(self, folder_path):
#         threat_detected = False
#         for root, dirs, files in os.walk(folder_path):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 file_hash = self.calculateHash(file_path)
#                 # Perform threat check with the calculated hash
#                 # If threat detected, set threat_detected = True and break the loop
#                 if threat_detected:
#                     break
#         return threat_detected

#     def calculateHash(self, file_path):
#         hasher = hashlib.md5()
#         with open(file_path, 'rb') as f:
#             buf = f.read()
#             hasher.update(buf)
#         return hasher.hexdigest()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = ThreatChecker()
#     window.show()
#     sys.exit(app.exec_())


""" Поиск файла по определенным папкам """
# import os

# def search_file(file_name, directories):
#     results = []
#     for directory in directories:
#         for root, dirs, files in os.walk(directory):
#             if file_name in files:
#                 results.append(os.path.join(root, file_name))
#     return results


# # Укажите имя файла, который хотите найти
# file_to_find = "virus2"

# username = os.getlogin()
# # Укажите список папок, в которых нужно выполнить поиск
# directories_to_search = [f"C:\\Users\\{username}\\Desktop\\TestFolder", f"C:\\Users\\{username}\\Downloads", 
#                        f"C:\\Users\\{username}\\Desktop", f"C:\\Users\\{username}\\Documents"]

# found_files = search_file(file_to_find, directories_to_search)

# if found_files:
#     print(f"Найден файл '{file_to_find}' в следующих папках:")
#     for file_path in found_files:
#         print(file_path)
# else:
#     print(f"Файл '{file_to_find}' не найден в указанных папках.")



# import os
# username = os.getlogin()
# directories_to_search = [f"C:\\Users\\{username}\\Desktop\\TestFolder", f"C:\\Users\\{username}\\Downloads", f"C:\\Users\\{username}\\Desktop", f"C:\\Users\\{username}\\Documents"]

# for i in range(len(directories_to_search)):
#     print(directories_to_search[i])





# import os
# import hashlib

# def find_file_by_hash(target_hash, folders):
#     for folder in folders:
#         for root, _, files in os.walk(folder):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 with open(file_path, "rb") as f:
#                     file_hash = hashlib.sha256(f.read()).hexdigest()
#                     if file_hash == target_hash:
#                         print(f"Файл с хешем {target_hash} найден в папке: {root}")
#                         return
    
#     print("Файл не найден")

# # Пример использования функции
# username = os.getlogin()
# target_hash = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
# folders = [f"C:\\Users\\{username}\\Desktop\\TestFolder", f"C:\\Users\\{username}\\Downloads", f"C:\\Users\\{username}\\Desktop", f"C:\\Users\\{username}\\Documents"]
# find_file_by_hash(target_hash, folders)



# import os
# import hashlib

# def find_files_by_hashes(target_hashes, folders):
#     for target_hash in target_hashes:
#         for folder in folders:
#             for root, _, files in os.walk(folder):
#                 for file_name in files:
#                     file_path = os.path.join(root, file_name)
#                     with open(file_path, "rb") as f:
#                         file_hash = hashlib.sha256(f.read()).hexdigest()
#                         if file_hash == target_hash:
#                             print(f"Файл с хешем {target_hash} найден в папке: {root}")
#                             break
#                 else:
#                     continue
#                 break
#             else:
#                 continue
#             break
#         else:
#             print(f"Файл с хешем {target_hash} не найден в указанных папках.")
    
# # Пример использования функции
# username = os.getlogin()
# target_hashes = ["e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "z9y8x7w6v5u4t3s2r1", "HASH_3"]
# folders = [f"C:\\Users\\{username}\\Desktop\\TestFolder", f"C:\\Users\\{username}\\Downloads", f"C:\\Users\\{username}\\Desktop", f"C:\\Users\\{username}\\Documents"]
# find_files_by_hashes(target_hashes, folders)







""" !!!Рабочий код поиска по хешам!!! """
# import os
# import hashlib

# def find_files_by_hashes(target_hashes, folders):
#     for target_hash in target_hashes:
#         for folder in folders:
#             for root, _, files in os.walk(folder):
#                 for file_name in files:
#                     file_path = os.path.join(root, file_name)
#                     with open(file_path, "rb") as f:
#                         file_hash = hashlib.sha256(f.read()).hexdigest()
#                         if file_hash == target_hash:
#                             print(f"Файл с хешем {target_hash} найден в папке: {root}")
#                             break
#             break
# # Пример использования функции
# username = os.getlogin()
# target_hashes = ["16355db04c8444072383393139fff3f6e6c467e475710a29d5182daebede711c", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"]
# folders = [f"C:\\Users\\{username}\\Desktop\\TestFolder", f"C:\\Users\\{username}\\Downloads", f"C:\\Users\\{username}\\Desktop", f"C:\\Users\\{username}\\Documents"]
# find_files_by_hashes(target_hashes, folders)




# import os
# import hashlib
# from PyQt5 import QtWidgets

# def display_message(title, message):
#     msg = QtWidgets.QMessageBox()
#     msg.setWindowTitle(title)
#     msg.setText(message)
#     msg.exec_()

# def find_file_by_hash(directory, hash_code):
#     for root, _, files in os.walk(directory):
#         for file in files:
#             file_path = os.path.join(root, file)
#             with open(file_path, "rb") as f:
#                 file_hash = hashlib.md5(f.read()).hexdigest()
#                 if file_hash == hash_code:  # Check if the file's hash matches the provided hash code
#                     return file_path
#     return None

# def delete_file(file_path):
#     os.remove(file_path)
#     return True

# # Пример использования:
# username = os.getlogin()
# hash_code = ["651b9095f45d292c99a5883a448488868fa2e78103fa72e31976127605bf92e0", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "16355db04c8444072383393139fff3f6e6c467e475710a29d5182daebede711c"]
# directory = [f"C:\\Users\\{username}\\Desktop\\TestFolder", f"C:\\Users\\{username}\\Downloads", f"C:\\Users\\{username}\\Desktop", f"C:\\Users\\{username}\\Documents"]
# file_to_delete = find_file_by_hash(directory, hash_code)
# if file_to_delete:
#     if delete_file(file_to_delete):
#         display_message("Файл удален", f"Файл с хеш-кодом {hash_code} был удален.")
#     else:
#         display_message("Ошибка удаления", "Не удалось удалить файл.")
# else:
#     display_message("Файл не найден", f"Файл с хеш-кодом {hash_code} не был найден.")





# import os
# import hashlib

# def find_file_by_hashes_in_folders(folders, target_hashes):
#     found_files = []

    
#     for target_hash in target_hashes:
#         for folder in folders:
#             for root, _, files in os.walk(folder):
#                 for file_name in files:
#                     file_path = os.path.join(root, file_name)
#                     with open(file_path, "rb") as f:
#                         file_hash = hashlib.sha256(f.read()).hexdigest()
#                         if file_hash == target_hash:
#                             print(f"В папке {root} обнаружена угроза: {file_name}")
#                             found_files.append({"hash_code": file_hash, "file_path": file_path, "folder": folder})
#     return found_files

# def delete_file(file_path):
#     os.remove(file_path)
#     return True

# # Пример использования:
# username = os.getlogin()
# hash_codes = ["e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "651b9095f45d292c99a5883a448488868fa2e78103fa72e31976127605bf92e0", "16355db04c8444072383393139fff3f6e6c467e475710a29d5182daebede711c"]
# folders = [f"C:\\Users\\{username}\\Desktop\\TestFolder", f"C:\\Users\\{username}\\Downloads", f"C:\\Users\\{username}\\Desktop", f"C:\\Users\\{username}\\Documents"]
# files_to_delete = find_file_by_hashes_in_folders(folders, hash_codes)
# print(files_to_delete)

# for file_data in files_to_delete:
#     file_path = file_data["file_path"]
#     folder = file_data["folder"]
#     if delete_file(file_path):
#         print(f"File with hash code {file_data['hash_code']} has been deleted. Found in folder: {folder}")
#     else:
#         print("Error deleting file.")





""" !!! РЕЗЕРВ СТРАНИЦЫ СКАНА В РЕАЛЬНОМ ВРЕМЕНИ!!! """
# """ Страница сканирования в реальном времени """
# class ScanRealTime(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         self.layout = QVBoxLayout()
#         self.label = QLabel("Страница сканирования в реальном времени")
#         self.layout.addWidget(self.label)

#         self.real_time_file_button = QPushButton("Запустить мониторинг файловой системы")
#         self.real_time_file_button.clicked.connect(self.monitor_files)
#         self.layout.addWidget(self.real_time_file_button)

#         self.setLayout(self.layout)
    
#     """ Функция для мониторинга добавления новых файлов и обнаружения вируса при помощи хеш проверки """
#     def monitor_files(self):
#         confirm = QMessageBox.question(self, 'BaohuMe - Подтверждение', 'Запустить сканирование в реальном времени?', QMessageBox.Yes | QMessageBox.No)
#         if confirm == QMessageBox.Yes:
#             print("Отработка команды")
#             os.system('time /t')
            
#             self.last_added_file = ''
#             self.timer = QTimer()
#             self.timer.timeout.connect(self.check_for_new_file)
#             self.timer.start(2000)  # Проверять наличие нового файла каждую секунду

           


#     """ Функция для обнаружения новых файлов в папке и проверки на наличие угроз при помощи хеширования """  
#     def check_for_new_file(self):
        
#         def find_files_by_hashes(target_hashes, folders):
#             for target_hash in target_hashes:
#                 for folder in folders:
#                     for root, _, files in os.walk(folder):
#                         for file_name in files:
#                             file_path = os.path.join(root, file_name)
#                             with open(file_path, "rb") as f:
#                                 file_hash = hashlib.sha256(f.read()).hexdigest()
#                                 if file_hash == target_hash:
#                                     print(f"В папке {root} обнаружена угроза: {file_name}")
#                                     self.del_malwer_real_scan(file_name, root)
#                                     # print(f"Обнаружена угроза в файле {file_name} с хешем {target_hash} найден в папке: {root}")
#                                     break
#                     break
#         # Пример использования функции
#         username = os.getlogin()
#         target_hashes = ["651b9095f45d292c99a5883a448488868fa2e78103fa72e31976127605bf92e0", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "16355db04c8444072383393139fff3f6e6c467e475710a29d5182daebede711c"]
#         folders = [f"C:\\Users\\{username}\\Desktop\\TestFolder", f"C:\\Users\\{username}\\Downloads", f"C:\\Users\\{username}\\Desktop", f"C:\\Users\\{username}\\Documents"]
#         find_files_by_hashes(target_hashes, folders)

#     """ Функция удаления файла """ # Дорабоать!!!
#     def del_malwer_real_scan(self, file_name, root):
#         # Попробовать сделать del_malwer_real_scan главной и через if обращаться к find_files_by_hashes
#         confirm = QMessageBox.question(self, 'BaohuMe - Подтверждение', f'В папке {root} обнаружена угроза: {file_name}, обезвредить угрозу?', QMessageBox.Yes | QMessageBox.No)
#         if confirm == QMessageBox.Yes:
#             os.remove(root + "\\" + file_name)
#             print(f"Файл {file_name} успешно удален")
#             self.confirmation_del_malwer()
#             # try:
#             #     # Попытка удаления файла
#             #     os.remove(root + "\\" + file_name)
#             #     print("File deleted successfully.")
#             # except PermissionError:
#             #     # Если возникает ошибка PermissionError, попытка удалить файл с повышенными привилегиями
#             #     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

#     """ Функция подтверждения удаления файла """
#     def confirmation_del_malwer(self):
#         confirm = QMessageBox.question(self, 'BaohuMe - Подтверждение', 'Файл успешно удален', QMessageBox.Close)
#         if confirm == QMessageBox.Close:
#             self.label.clear()
#             self.label.setText("Страница сканирования в реальном времени")
