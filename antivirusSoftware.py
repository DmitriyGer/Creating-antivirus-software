import sys, os, hashlib, webbrowser

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QStackedWidget, QMessageBox, QFileDialog
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont

from helpers import database

""" Страница сканирования"""
class ScanPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        """Текст в блоке 'Страница' """
        self.layout = QVBoxLayout()
        self.label = QLabel("Страница сканирования\n Страница сканирования позволяет проверить файл\n на наличие вредоностного ПО при помощи API-сервиса")
        self.layout.addWidget(self.label)
       
        """ Кнопка 'Выбора файла' """
        self.file_button = QPushButton("Выбрать файл")
        self.file_button.clicked.connect(self.select_file)
        # self.file_button.setStyleSheet("background-color: rgb(35, 74, 73); color: rgb(228, 208, 186);")
        self.layout.addWidget(self.file_button)

        self.setLayout(self.layout)
        
    """ Функция выбора файла """
    def select_file(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Выберите файл для сканирования", "", "Все файлы (*)", options=options)
        if file:   
            self.show_testing_page(file)         
            
    """ Функция вызова стр. тест """
    def show_testing_page(self, file):
        
        data = database.git_info_files(file)
        name_file = file.split("/")[-1]
        
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
        self.label = QLabel("Страница сканирования в реальном времени\n Страница сканирования в реальном времени позволяет отслеживать\n файловый менеджер windows при помощи хэш сканирования, то есть\n обнароживать угрозу ")
        self.layout.addWidget(self.label)

        self.real_time_file_button = QPushButton("Запустить мониторинг файловой системы")
        self.real_time_file_button.clicked.connect(self.monitor_files)
        # self.real_time_file_button.setStyleSheet("background-color: rgb(35, 74, 73); color: rgb(228, 208, 186);")
        self.layout.addWidget(self.real_time_file_button)

        self.setLayout(self.layout)
    
    """ Функция запуска алгоритма сканирования """
    def monitor_files(self):
        confirm = QMessageBox.question(self, 'BaohuMe - Подтверждение', 'Запустить сканирование в реальном времени?', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            os.system('time /t')
            username = os.getlogin()
            target_hashes = ["e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "651b9095f45d292c99a5883a448488868fa2e78103fa72e31976127605bf92e0", "c3812211b7b4ab8fc631509980c091b833091ebf6f5f461aaf0a23cc4345733a"]
            folders = [f"C:\\Users\\{username}\\Desktop\\TestFolder", f"C:\\Users\\{username}\\Downloads", f"C:\\Users\\{username}\\Desktop", f"C:\\Users\\{username}\\Documents", f"C:\\Users\\{username}\\OneDrive\\Рабочий стол", f"C:\\Users\\{username}\\OneDrive\\Документы"]

            """ Лямбда функция служащая для запуска основного кода с определенным интерваалом"""
            self.timer = QTimer()
            self.timer.timeout.connect(lambda: self.check_and_delete_files(target_hashes, folders))  # Лямбда-функция для вызова check_and_delete_files
            self.timer.start(4000)  # Запуск таймера с интервалом в 4 секунды

    """ Функция для проверки наличия и удаления файлов с угрозами """
    def check_and_delete_files(self, target_hashes, folders):
        files_to_delete = self.check_for_new_file(target_hashes, folders)
        for file_data in files_to_delete:
            file_path = file_data["file_path"]
            folder = file_data["folder"]
            if self.del_malwer_real_scan(file_path):
                print(f"File with hash code {file_data['hash_code']} has been deleted. Found in folder: {folder}")

    """ Функция для обнаружения новых файлов в папке и проверки на наличие угроз при помощи хеширования """  
    def check_for_new_file(self, target_hashes, folders):
        found_files = []
        for target_hash in target_hashes:
            for folder in folders:
                for root, _, files in os.walk(folder):
                    for file_name in files:
                        file_path = os.path.join(root, file_name)
                        with open(file_path, "rb") as f:
                            file_hash = hashlib.sha256(f.read()).hexdigest()
                            if file_hash == target_hash:
                                print(f"В папке {root} обнаружена угроза: {file_name}")
                                found_files.append({"hash_code": file_hash, "file_path": file_path, "folder": folder})
                                break
                break
        return found_files

    """ Функция удаления файла """
    def del_malwer_real_scan(self, file_path):
        confirm = QMessageBox.question(self, 'BaohuMe - Подтверждение', f'Обнаружена угроза {file_path}, обезвредить угрозу?', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            os.remove(file_path)
            print(f"Файл {file_path} успешно удален")
            self.confirmation_del_malwer(file_path)
            return True

    """ Функция подтверждения удаления файла """
    def confirmation_del_malwer(self, file_path):
        confirm = QMessageBox.question(self, 'BaohuMe - Подтверждение', f'Файл по пути {file_path} успешно удален', QMessageBox.Close)
        if confirm == QMessageBox.Close:
            self.label.clear()
            self.label.setText("Страница сканирования в реальном времени")
        

""" Страница о разработчиках """
class DevelopersPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.label = QLabel("Сведения о разработчиках\n\n\
Должность\t\tИмя\t\t\tGitHub\t\t\t\te-mail\n\n\
Major Developer\t\tGerasimov Dmitriy\thttps://github.com/DmitriyGer\tdim1a15@mail.ru\n\
Major analyst\t\tLoeva Taisiya\t\thttps://github.com/loevatss\ttayaloeva@mail.ru\n\
Major designer\t\tDryomin Vyacheslav\thttps://github.com/JohnHinster\tDryomin.JH@yandex.ru\n\n\
Наша команда разработчиков - это креативные и целеустремленные специалисты, готовые принимать\n\
сложные вызовы и находить инновационные решения.\n\n\
«Столкнувшись с трудностями, нельзя сдаваться, бежать. Вы должны оценивать ситуацию,\n\
искать решения и верить в то, что все делается к лучшему. Терпение – вот ключ к победе».\n\
\t\t\t\t\t\t\t\t\t\tНик Вуйчич")
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
        # p = self.palette()
        # p.setColor(self.backgroundRole(), QColor(19, 51, 50))  # Изменение цвета страницы
        # self.setPalette(p)

        # font = QFont("Arial", 12)
        # self.setFont(font)

        self.menu_layout = QVBoxLayout()
        self.page_widget = QStackedWidget()

        self.scan_button = QPushButton("Сканирование")
        self.scan_button.clicked.connect(lambda: self.load_page(0))
        # self.scan_button.setStyleSheet("background-color: rgb(35, 74, 73); color: rgb(228, 208, 186);")
        self.menu_layout.addWidget(self.scan_button)

        self.scan_real_time = QPushButton("Сканирование в раельном времени")
        self.scan_real_time.clicked.connect(lambda: self.load_page(1))
        # self.scan_real_time.setStyleSheet("background-color: rgb(35, 74, 73); color: rgb(228, 208, 186);")
        self.menu_layout.addWidget(self.scan_real_time)

        self.developers_button = QPushButton("О разработчиках")
        self.developers_button.clicked.connect(lambda: self.load_page(2))
        # self.developers_button.setStyleSheet("background-color: rgb(35, 74, 73); color: rgb(228, 208, 186);")
        self.menu_layout.addWidget(self.developers_button)

        self.close_button = QPushButton("Закрыть")
        self.close_button.clicked.connect(self.close_app)
        # self.close_button.setStyleSheet("background-color: rgb(35, 74, 73); color: rgb(228, 208, 186);")
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
