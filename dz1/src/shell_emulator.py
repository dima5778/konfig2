import os
import time
import xml.etree.ElementTree as ET
from commands import ls, cd, exit_shell, cal, uptime, find

class ShellEmulator:
    def __init__(self, config_file):
        self.config_file = config_file
        self.start_time = time.time()
        self.load_config()

    def load_config(self):
        """Загружает конфигурацию из XML-файла."""
        tree = ET.parse(self.config_file)
        root = tree.getroot()
        self.start_script = root.find('startScript').text

    def run_start_script(self):
        """Выполняет стартовый скрипт, если он указан."""
        if os.path.exists(self.start_script):
            with open(self.start_script) as f:
                for command in f:
                    self.execute_command(command.strip())

    def execute_command(self, command_line):
        """Выполняет команду из строки."""
        command, *args = command_line.split()
        if command == "ls":
            print(ls())
        elif command == "cd":
            directory = args[0] if args else '.'
            print(cd(directory))
        elif command == "exit":
            print(exit_shell())
            return False
        elif command == "cal":
            print(cal())
        elif command == "uptime":
            print(uptime(self.start_time))
        elif command == "find":
            filename = args[0] if args else ''
            print(find(filename))
        else:
            print(f"Команда {command} не поддерживается.")
        return True

    def start(self):
        """Запускает эмулятор."""
        self.run_start_script()
        while True:
            command_line = input("$ ")
            if not self.execute_command(command_line):
                break

if __name__ == "__main__":
    emulator = ShellEmulator("config.xml")
    emulator.start()
