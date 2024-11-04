import unittest
import os
import time
import datetime
from commands import ls, cd, exit_shell, cal, uptime, find

class TestCommands(unittest.TestCase):

    def test_ls(self):
        """Тест команды ls."""
        current_files = os.listdir(os.getcwd())
        self.assertEqual(ls(), current_files)

    def test_cd(self):
        """Тест команды cd."""
        initial_directory = os.getcwd()
        os.mkdir("test_dir")
        cd("test_dir")
        self.assertEqual(os.getcwd(), os.path.join(initial_directory, "test_dir"))
        os.chdir(initial_directory)
        os.rmdir("test_dir")

    def test_cd_nonexistent(self):
        """Тест cd для несуществующей директории."""
        self.assertIn("не найдена", cd("nonexistent_dir"))

    def test_exit_shell(self):
        """Тест команды exit."""
        self.assertEqual(exit_shell(), "exit")

    def test_cal(self):
        """Тест команды cal."""
        current_month = datetime.datetime.now().strftime("%B %Y")
        self.assertIn(current_month, cal())

    def test_uptime(self):
        """Тест команды uptime."""
        start_time = time.time() - 100  # эмуляция запуска 100 секунд назад
        uptime_str = uptime(start_time)
        self.assertRegex(uptime_str, r"\d+:\d+:\d+")

    def test_find(self):
        """Тест команды find."""
        with open("testfile.txt", "w") as f:
            f.write("test")
        # Измените здесь ожидаемое значение
        self.assertIn("testfile.txt", find("testfile.txt"))  # Уберите './' перед именем файла
        os.remove("testfile.txt")

    def test_find_nonexistent(self):
        """Тест команды find для несуществующего файла."""
        self.assertIn("не найден", find("nonexistentfile.txt"))

    if __name__ == "__main__":
        unittest.main()
