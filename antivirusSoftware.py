import sys, os, hashlib

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QStackedWidget, QMessageBox, QFileDialog
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer

from helpers import database

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
            self.show_testing_page(file)         
            
    """ Функция вызова стр. тест """
    def show_testing_page(self, file):
        
        data = database.git_info_files(file)
        name_file = file.split("/")[-1]

        # self.label.setText(f"Выбранный файл: {name_file}")
        
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
                self.return_to_main()
            else:
                self.label.setText(f"В файле {name_file} обнаружена угроза")
                self.del_malwer(file)

    """ Функция удаления файла """
    def del_malwer(self, file):
        confirm = QMessageBox.question(self, 'BaohuMe - Подтверждение', 'Вы действительно хотите удалить файл?', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            os.remove(file)
            self.confirmation_del_malwer()

    """ Функция подтверждения удаления файла """
    def confirmation_del_malwer(self):
        confirm = QMessageBox.question(self, 'BaohuMe - Подтверждение', 'Файл успешно удален', QMessageBox.Close)
        if confirm == QMessageBox.Close:
            self.label.clear()
            self.label.setText("Страница сканирования")

    """ Функция возвращения на главный экран (угроз не обноружено) """
    def return_to_main(self):
        confirm = QMessageBox.question(self, 'BaohuMe - Подтверждение', 'Угроз не обнаружено, вернуться на главный экран?', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.label.clear()
            self.label.setText("Страница сканирования")
    

""" Страница сканирования в реальном времени """
class ScanRealTime(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.label = QLabel("Страница сканирования в реальном времени")
        self.layout.addWidget(self.label)

        self.real_time_file_button = QPushButton("Запустить мониторинг файловой системы")
        self.real_time_file_button.clicked.connect(self.monitor_files)
        self.layout.addWidget(self.real_time_file_button)

        self.setLayout(self.layout)
    
    """ Функция для мониторинга добавления новых файлов и обнаружения вируса при помощи хеш проверки """
    def monitor_files(self, folder_path):
        confirm = QMessageBox.question(self, 'BaohuMe - Подтверждение', 'Запустить сканирование в реальном времени?', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            print("Отработка команды")
            os.system('time /t')
            
            self.last_added_file = ''
            self.timer = QTimer()
            self.timer.timeout.connect(self.check_for_new_file)
            self.timer.start(2000)  # Проверять наличие нового файла каждую секунду

    """ Функция для обнаружения новых файлов в папке и проверки на наличие угроз при помощи хеширования """       
    def check_for_new_file(self):
        
        def find_files_by_hashes(target_hashes, folders):
            for target_hash in target_hashes:
                for folder in folders:
                    for root, _, files in os.walk(folder):
                        for file_name in files:
                            file_path = os.path.join(root, file_name)
                            with open(file_path, "rb") as f:
                                file_hash = hashlib.sha256(f.read()).hexdigest()
                                if file_hash == target_hash:
                                    print(f"В папке {root} обнаружена угроза: {file_name}")
                                    # print(f"Обнаружена угроза в файле {file_name} с хешем {target_hash} найден в папке: {root}")
                                    break
                    break
        # Пример использования функции
        username = os.getlogin()
        target_hashes = ["e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "16355db04c8444072383393139fff3f6e6c467e475710a29d5182daebede711c"]
        folders = [f"C:\\Users\\{username}\\Desktop\\TestFolder", f"C:\\Users\\{username}\\Downloads", f"C:\\Users\\{username}\\Desktop", f"C:\\Users\\{username}\\Documents"]
        find_files_by_hashes(target_hashes, folders)
        

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


        """ Изменение цвета программы """
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(255, 255, 255))  # Изменение цвета страницы
        self.setPalette(p)


        self.menu_layout = QVBoxLayout()
        self.page_widget = QStackedWidget()

        self.scan_button = QPushButton("Сканирование")
        self.scan_button.clicked.connect(lambda: self.load_page(0))
        self.menu_layout.addWidget(self.scan_button)

        self.scan_real_time = QPushButton("Сканирование в раельном времени")
        self.scan_real_time.clicked.connect(lambda: self.load_page(1))
        self.menu_layout.addWidget(self.scan_real_time)

        self.developers_button = QPushButton("О разработчиках")
        self.developers_button.clicked.connect(lambda: self.load_page(2))
        self.menu_layout.addWidget(self.developers_button)

        self.close_button = QPushButton("Закрыть")
        self.close_button.clicked.connect(self.close_app)
        self.menu_layout.addWidget(self.close_button)

        self.scan_page = ScanPage()
        self.scan_real_time = ScanRealTime()
        self.developers_page = DevelopersPage()

        self.page_widget.addWidget(self.scan_page)
        self.page_widget.addWidget(self.scan_real_time)
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
