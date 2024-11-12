import tarfile
import os
import time
import calendar
import datetime

class CommandProcessor:
    def __init__(self):
        self.start_time = time.time()

    def execute(self, command, shell):
        cmd_parts = command.split()
        cmd_name = cmd_parts[0]
        args = cmd_parts[1:]

        if cmd_name == "ls":
            self.ls(shell)
        elif cmd_name == "cd":
            self.cd(shell, args)
        elif cmd_name == "cal":
            self.cal()
        elif cmd_name == "uptime":
            self.uptime()
        elif cmd_name == "find":
            self.find(shell, args)
        else:
            print(f"Команда '{cmd_name}' не поддерживается.")

    def ls(self, shell):
        """Вывод содержимого текущей директории в архиве tar."""
        current_dir = shell.current_directory.strip('/')  # Убираем лишние слэши для правильного поиска

        if not current_dir:
            current_dir = "."  # Устанавливаем корневую директорию, если она пустая

        try:
            # Список для хранения имен файлов и директорий
            contents = []

            for member in shell.tar.getmembers():
                # Проверка, является ли элемент файлом/папкой в текущей директории
                member_path = member.name.strip('/')

                # Если текущая директория — корневая, берем только первую часть имени
                if current_dir == "." and '/' not in member_path:
                    contents.append(member_path)
                # Для поддиректорий проверяем, чтобы путь содержал текущую директорию как префикс
                elif member_path.startswith(current_dir + '/'):
                    relative_path = member_path[len(current_dir) + 1:]
                    if '/' not in relative_path:
                        contents.append(relative_path)

            if contents:
                print("\n".join(contents))
            else:
                print("Нет файлов или директорий в текущей директории.")
        except Exception as e:
            print(f"Ошибка при доступе к содержимому архива: {e}")

    def cd(self, shell, args):
        """Переход в указанную директорию в архиве tar или на уровень вверх."""
        if not args:
            print("Не указана директория для перехода.")
            return

        path = args[0]

        if path == "..":
            # Если текущая директория - не корень, идем на уровень вверх
            if shell.current_directory != "/":
                shell.current_directory = os.path.dirname(shell.current_directory.rstrip('/'))
                if not shell.current_directory or shell.current_directory == "":
                    shell.current_directory = "/"
                print(f"Текущая директория: {shell.current_directory}")
            else:
                print("Вы уже находитесь в корневой директории.")
            return

        # Удаляем ведущий слэш из пути, если он есть
        if path.startswith('/'):
            path = path[1:]

        new_dir = os.path.join(shell.current_directory, path).strip('/')
        # Если это не корневая директория, добавляем слэш в начале
        if new_dir and not new_dir.startswith('/'):
            new_dir = "/" + new_dir

        try:
            # Проверяем существование директории
            dir_exists = any(
                member.name.rstrip('/') == new_dir.strip('/')
                for member in shell.tar.getmembers()
                if member.isdir()
            )

            if dir_exists:
                shell.current_directory = new_dir + "/"
                if shell.current_directory == "//":
                    shell.current_directory = "/"
                print(f"Текущая директория: {shell.current_directory}")
            else:
                print(f"Директория '{path}' не найдена.")
        except Exception as e:
            print(f"Ошибка при открытии архива: {e}")

    def cal(self):
        """Выводит календарь на текущий месяц."""
        print(calendar.month(datetime.datetime.now().year, datetime.datetime.now().month))

    def uptime(self):
        """Выводит время работы эмулятора."""
        elapsed_time = time.time() - self.start_time
        hours, remainder = divmod(int(elapsed_time), 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"Время работы: {hours} ч {minutes} м {seconds} с")

    def find(self, shell, args):
        """Поиск файлов в архиве."""
        if not args:
            print("Не указано имя файла для поиска.")
            return
        filename = args[0]
        try:
            # Работаем с открытым архивом
            found_files = [member.name for member in shell.tar.getmembers() if filename in member.name]

            if found_files:
                for file in found_files:
                    print(file)
            else:
                print(f"Файл '{filename}' не найден.")
        except Exception as e:
            print(f"Ошибка при открытии архива: {e}")
