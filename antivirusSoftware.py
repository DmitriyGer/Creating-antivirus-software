import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QStackedWidget, QMessageBox, QFileDialog

""" Страница сканирования"""
class ScanPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.label = QLabel("Страница сканирования\n")
        self.layout.addWidget(self.label)

        self.file_button = QPushButton("Выбрать файл")
        self.file_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.file_button)

        self.setLayout(self.layout)

    # Функции
        
    # Функция выбора файла
    def select_file(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.ReadOnly
        file, _ = QFileDialog.getOpenFileName(self, "Выберите файл для сканирования", "", "Все файлы (*)", options=options)
        if file:
            print("Выбран файл:", file)

""" Страница о разработчиках """
class DevelopersPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.label = QLabel("Страница о разработчиках")
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

""" Страница тестирования """
class TestPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.label = QLabel("Страница тестирования")
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

""" Основной класс """
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('BaohuMe')
        self.resize(600, 400)

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

    def close_app(self):
        confirm = QMessageBox.question(self, 'Подтверждение', 'Вы уверены, что хотите закрыть?', QMessageBox.Yes | QMessageBox.No)
        
        if confirm == QMessageBox.Yes:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
