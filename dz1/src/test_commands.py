import unittest
from unittest.mock import patch
from shell_emulator import ShellEmulator, CommandProcessor
import tarfile
import os

class TestShellEmulator(unittest.TestCase):

    def setUp(self):
        """Настройка тестового окружения"""
        # Указываем путь к существующему tar файлу
        self.tar_path = "C:/emulator-shell-os/virtual_files.tar"
        self.config_path = "C:/emulator-shell-os/config.xml"

        # Инициализируем эмулятор с настоящим tar архивом
        self.emulator = ShellEmulator(self.config_path)

    def test_ls_root(self):
        """Тестируем команду ls в корневой директории"""
        with patch('sys.stdout') as mock_stdout:
            # Эмулируем команду ls на уровне корня
            self.emulator.current_directory = "/"
            self.emulator.command_processor.ls(self.emulator)
            output = ''.join([call[0][0] for call in mock_stdout.write.call_args_list]).splitlines()
            # Проверяем, что в выводе присутствуют файлы и папки
            self.assertIn("dir1", output)
            self.assertIn("dir2", output)
            self.assertIn("file3.txt", output)

    def test_ls_dir1(self):
        """Тестируем команду ls в директории dir1"""
        with patch('sys.stdout') as mock_stdout:
            # Эмулируем команду ls в поддиректории dir1
            self.emulator.current_directory = "/dir1"
            self.emulator.command_processor.ls(self.emulator)
            output = ''.join([call[0][0] for call in mock_stdout.write.call_args_list]).splitlines()
            # Проверяем, что выводится содержимое папки dir1
            self.assertNotIn("Нет файлов или директорий в текущей директории.", output)
            self.assertIn("file1.txt", output)
            self.assertNotIn("dir2", output)  # Проверка, что других директорий нет

    def test_cd_to_existing_directory(self):
        """Тестируем команду cd на переход в существующую директорию"""
        with patch('sys.stdout') as mock_stdout:
            # Переход в существующую директорию dir1
            self.emulator.command_processor.cd(self.emulator, ["dir1"])
            # Проверка, что текущая директория установилась в "/dir1"
            self.assertEqual(self.emulator.current_directory.rstrip('/'), "/dir1")
            output = "".join([call[0][0] for call in mock_stdout.write.call_args_list])
            self.assertIn("Текущая директория: /dir1", output)

    def test_cd_to_non_existing_directory(self):
        """Тестируем команду cd на переход в несуществующую директорию"""
        with patch('sys.stdout') as mock_stdout:
            # Переход в несуществующую директорию
            self.emulator.command_processor.cd(self.emulator, ["non_existing_dir"])
            output = [call[0][0] for call in mock_stdout.write.call_args_list]
            self.assertIn("Директория 'non_existing_dir' не найдена.", output)

    def test_cd_up(self):
        """Тестируем команду cd с переходом на уровень вверх"""
        with patch('sys.stdout') as mock_stdout:
            # Переход в dir1, а затем на уровень вверх
            self.emulator.current_directory = "/dir1"
            self.emulator.command_processor.cd(self.emulator, [".."])
            # Проверяем, что путь изменился на "/"
            self.assertEqual(self.emulator.current_directory, "/")
            output = [call[0][0] for call in mock_stdout.write.call_args_list]
            self.assertIn("Текущая директория: /", output)

    def test_uptime(self):
        """Тестируем команду uptime"""
        with patch('sys.stdout') as mock_stdout:
            # Тестируем команду uptime
            self.emulator.command_processor.uptime()
            output = [call[0][0] for call in mock_stdout.write.call_args_list]
            self.assertTrue(any("Время работы:" in line for line in output))

    def test_find_existing_file(self):
        """Тестируем команду find для существующего файла"""
        with patch('sys.stdout') as mock_stdout:
            # Поиск файла file1.txt в архиве
            self.emulator.command_processor.find(self.emulator, ["file1.txt"])
            output = [call[0][0] for call in mock_stdout.write.call_args_list]
            self.assertIn("dir1/file1.txt", output)

    def test_find_non_existing_file(self):
        """Тестируем команду find для несуществующего файла"""
        with patch('sys.stdout') as mock_stdout:
            # Поиск несуществующего файла
            self.emulator.command_processor.find(self.emulator, ["non_existing_file.txt"])
            output = [call[0][0] for call in mock_stdout.write.call_args_list]
            self.assertIn("Файл 'non_existing_file.txt' не найден.", output)

    def test_cal(self):
        """Тестируем команду cal"""
        with patch('sys.stdout') as mock_stdout:
            # Тестируем вывод календаря
            self.emulator.command_processor.cal()
            output = [call[0][0] for call in mock_stdout.write.call_args_list]
            # Проверяем, что год и месяц присутствуют в выводе, игнорируя пробелы
            self.assertIn("November 2024", output[0].strip())  # Убираем начальные пробелы и проверяем

if __name__ == "__main__":
    unittest.main()
