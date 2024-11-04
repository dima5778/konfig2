import os
import time
import calendar
import datetime

def ls():
    """Возвращает список файлов и папок в текущей директории."""
    return os.listdir(os.getcwd())

def cd(directory):
    """Меняет текущую директорию."""
    try:
        os.chdir(directory)
        return os.getcwd()
    except FileNotFoundError:
        return f"Директория {directory} не найдена."

def exit_shell():
    """Завершает сеанс эмулятора."""
    return "exit"

from datetime import datetime, timedelta



def cal():
    """Возвращает текущий месяц и год."""
    today = datetime.now()
    return today.strftime("%B %Y")  # Формат: название месяца ГГГГ



def uptime(start_time):
    """Возвращает время, прошедшее с момента запуска в формате ЧЧ:ММ:СС."""
    uptime_seconds = int(time.time() - start_time)
    uptime_str = str(timedelta(seconds=uptime_seconds))  # Используйте timedelta напрямую
    return uptime_str

def find(filename):
    """Ищет файл или папку в текущей директории и поддиректориях."""
    matches = []
    for root, _, files in os.walk('.'):
        if filename in files:
            matches.append(os.path.normpath(os.path.join(root, filename)))
    return matches if matches else f"Файл {filename} не найден."

