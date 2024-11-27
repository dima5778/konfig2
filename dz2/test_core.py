import unittest
from unittest.mock import patch, MagicMock
import json
import os

# Импортируем тестируемые функции из core.py
from core import get_direct_dependencies, build_transitive_dependency_graph, main


class TestDependencyGraph(unittest.TestCase):
    @patch('subprocess.run')
    def test_get_direct_dependencies(self, mock_subprocess_run):
        """
        Тест для функции get_direct_dependencies.
        """
        # Настраиваем мок для subprocess.run
        mock_subprocess_run.return_value = MagicMock(
            stdout="package\nlib1\nlib2\n",
            returncode=0
        )

        # Вызываем функцию и проверяем результат
        result = get_direct_dependencies("example-package")
        expected = ["lib1", "lib2"]
        self.assertEqual(result, expected)

        # Проверяем, что subprocess.run был вызван с правильными параметрами
        mock_subprocess_run.assert_called_once_with(
            ['apk', 'info', '--depends', 'example-package'],
            capture_output=True,
            text=True,
            check=True
        )

    @patch('core.get_direct_dependencies')
    def test_build_transitive_dependency_graph(self, mock_get_direct_dependencies):
        """
        Тест для функции build_transitive_dependency_graph.
        """
        # Настраиваем мок для get_direct_dependencies
        mock_get_direct_dependencies.side_effect = lambda pkg: {
            "package1": ["lib1", "lib2"],
            "lib1": ["lib3"],
            "lib2": [],
            "lib3": []
        }.get(pkg, [])

        # Вызываем функцию и проверяем результат
        dot_graph = build_transitive_dependency_graph("package1")
        expected_dot = (
            "digraph G {\n"
            '    "package1" -> "lib1";\n'
            '    "package1" -> "lib2";\n'
            '    "lib1" -> "lib3";\n'
            "}"
        )
        self.assertEqual(dot_graph, expected_dot)

    @patch('builtins.open')
    @patch('core.build_transitive_dependency_graph')
    @patch('core.json.load')
    def test_main(self, mock_json_load, mock_build_graph, mock_open):
        """
        Тест для функции main.
        """
        # Настроим моки
        mock_json_load.return_value = {
            "graphviz_path": "/usr/bin/dot",
            "package_name": "bash",
            "output_path": "dependencies.dot"
        }
        mock_build_graph.return_value = "digraph G {\n}"

        # Настроим mock_open для чтения конфигурации и записи в файл
        mock_open.side_effect = [MagicMock(), MagicMock()]  # Для config.json и test_output.dot

        # Проверяем вызов main
        with patch('core.print') as mock_print:
            main()

            # Проверяем, что функции были вызваны с правильными параметрами
            mock_build_graph.assert_called_once_with("bash")  # Проверяем, что пакет "bash" был передан в функцию
            mock_open.assert_any_call('config.json', 'r')  # Проверяем открытие config.json для чтения
            mock_open.assert_any_call("dependencies.dot", "w")  # Проверяем открытие для записи
            mock_print.assert_any_call("\nGraphviz DOT format output:")
            mock_print.assert_any_call("digraph G {\n}")

    def tearDown(self):
        """
        Очистка после выполнения тестов, если создавались временные файлы.
        """
        try:
            os.remove("test_output.dot")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
