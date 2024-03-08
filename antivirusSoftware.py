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
                                    print(f"Файл с хешем {target_hash} найден в папке: {root}")
                                    break
                    break
        # Пример использования функции
        username = os.getlogin()
        target_hashes = ["16355db04c8444072383393139fff3f6e6c467e475710a29d5182daebede711c", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"]
        folders = [f"C:\\Users\\{username}\\Desktop\\TestFolder", f"C:\\Users\\{username}\\Downloads", f"C:\\Users\\{username}\\Desktop", f"C:\\Users\\{username}\\Documents"]
        find_files_by_hashes(target_hashes, folders)



        # # Функция для поиска
        # def search_file(file_name, directories):
        #     results = []
        #     for directory in directories:
        #         for root, dirs, files in os.walk(directory):
        #             if file_name in files:
        #                 results.append(os.path.join(root, file_name))
        #     return results
        
        # Создаем базу данных с хешами безопасных файлов
        safe_files = {
            "file1": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "file2.exe": "z9y8x7w6v5u4t3s2r1",
            # Добавьте сюда остальные файлы
        }
        # search_file_len = len(safe_files)

        # # Укажите имя файла, который хотите найти
        # file_to_find = "virus2"

        # # Укажите список папок, в которых нужно выполнить поиск
        # username = os.getlogin()
        # directories_to_search = [f"C:\\Users\\{username}\\Desktop\\TestFolder", f"C:\\Users\\{username}\\Downloads", f"C:\\Users\\{username}\\Desktop", f"C:\\Users\\{username}\\Documents"]
        # directories_to_search_len = len(directories_to_search)
        
        # for i in range(directories_to_search_len):
        #     directories_to_search_str = directories_to_search[i]
        #     print(directories_to_search_str)
        
        # with open(directories_to_search_str + "\\" + file_to_find, "rb") as file:
        #         content = file.read()
        

        # # Хешируем содержимое файла
        # hash_obj = hashlib.sha256()
        # hash_obj.update(content)
        # file_hash = hash_obj.hexdigest()


        # # Проверяем, есть ли хеш в базе безопасных файлов
        # if file_hash in safe_files.values():
        #     print(f"В файле {file_to_find} обнаружена угроза, она находится в папке {directories_to_search}")
        # else:
        #     print(f"В файле {file_to_find} угроз не обнаружено")





        # found_files = search_file(file_to_find, directories_to_search)

        # if found_files:
        #     # print(f"Найден файл '{file_to_find}' в следующих папках:")
        #     for file_path in found_files:
        #         path_file = file_path
        #         # print(file_path)
        # # else:
        # #     print(f"Файл '{file_to_find}' не найден в указанных папках.")

        # # with open(directories_to_search_str + "\\" + file_to_find, "rb") as file:
        # #     content = file.read()

        # # Хешируем содержимое файла
        # hash_obj = hashlib.sha256()
        # hash_obj.update(content)
        # file_hash = hash_obj.hexdigest()


        # # Проверяем, есть ли хеш в базе безопасных файлов
        # if file_hash in safe_files.values():
        #     print(f"В файле {file_to_find} обнаружена угроза, она находится в папке {path_file}")
        # else:
        #     print(f"В файле {file_to_find} угроз не обнаружено")






        # # Создаем базу данных с хешами безопасных файлов
        # safe_files = {
        #     "file1": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        #     "file2.exe": "z9y8x7w6v5u4t3s2r1",
        #     # Добавьте сюда остальные файлы
        # }
        
        # # Путь к папаке для отслеживания новых файлов
        # username = os.getlogin()
        # folder_path = f"C:\\Users\\{username}\\Desktop\\TestFolder"

        # # Последний добавленный файл
        # last_added_file = ''

        # # Прогонка по папке
        # files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        # files.sort(key=lambda x: os.path.getctime(os.path.join(folder_path, x)), reverse=True)
        # print(files)

        # # Прогонка по папкам
        # for folders in folder_path:
        #     for root, dirs, files in os.walk(folders):
        #         for file in files:
        #             file_path = os.path.join(root, file)
        #             # print(file_path)
                    
        # # Выбираем из всех файлов последний
        # if files:
        #     latest_file = files[0]
        #     if latest_file != last_added_file:
        #         last_added_file = latest_file
        
        # # Простматриваем файл с проводника
        # with open(folder_path + "\\" + last_added_file, "rb") as file:
        #     content = file.read()

        # # Хешируем содержимое файла
        # hash_obj = hashlib.sha256()
        # hash_obj.update(content)
        # file_hash = hash_obj.hexdigest()

        # # Проверяем, есть ли хеш в базе безопасных файлов
        # if file_hash in safe_files.values():
        #     print(f"В файле {last_added_file} обнаружена угроза")
        # else:
        #     print(f"В файле {last_added_file} угроз не обнаружено")

            
        
        """ В скором времени удалить """
        # if confirm == QMessageBox.Yes:
        # print('Start_real_time_scan')
        # # Считывание путей к папкам из файла Folder.txt
        # folder_paths = []
        # with open('helpers\database_local.txt', 'r') as file:
        #     for line in file:
        #         folder_paths.append(line.strip())

        # # Словарь для хранения списка файлов в каждой папке на старте
        # initial_files = {folder_path: os.listdir(folder_path) for folder_path in folder_paths}

        # # Основной цикл программы
        # 
        # while True:
        #     for folder_path in folder_paths:
        #         current_files = os.listdir(folder_path)

        #         # Поиск новых файлов
        #         new_files = [file for file in current_files if file not in initial_files[folder_path]]

        #         # Вывод сообщения при обнаружении нового файла
        #         for new_file in new_files:
        #             print(f"Новый файл обнаружен в папке {folder_path}: {new_file}")

        #         initial_files[folder_path] = current_files

        #     # time.sleep(5)  # Проверка каждые 5 секунд
            



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
