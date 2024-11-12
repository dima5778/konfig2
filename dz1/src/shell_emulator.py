import os
import tarfile
import xml.etree.ElementTree as ET
import time
from commands import CommandProcessor


class ShellEmulator:
    def __init__(self, config_path):
        self.start_time = time.time()
        self.load_config(config_path)
        self.command_processor = CommandProcessor()
        self.load_filesystem()

    def load_filesystem(self):
        self.current_directory = "/"  # Начинаем с корневой директории
        self.tar = tarfile.open(self.filesystem_path, 'r')

    def load_config(self, config_path):
        tree = ET.parse(config_path)
        root = tree.getroot()
        self.filesystem_path = root.find('virtual_filesystem_path').text
        self.start_script_path = root.find('start_script_path').text

    def close_filesystem(self):
        if self.tar:
            self.tar.close()

    def run(self):
        if self.start_script_path:
            try:
                with open(self.start_script_path, "r") as script:
                    for line in script:
                        self.execute_command(line.strip())
            except Exception as e:
                print(f"Ошибка при чтении стартового скрипта: {e}")

        while True:
            command = input(f"{self.current_directory}> ")
            if command == "exit":
                print("Выход из эмулятора.")
                self.close_filesystem()
                break
            self.execute_command(command)

    def execute_command(self, command):
        try:
            self.command_processor.execute(command, self)
        except Exception as e:
            print(f"Ошибка выполнения команды '{command}': {e}")



if __name__ == "__main__":
    emulator = ShellEmulator("C:\emulator-shell-os\config.xml")
    emulator.run()
