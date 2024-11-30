import unittest
from io import StringIO
from core import ConfigParser  # Проверьте, что файл core.py доступен
import json


class TestConfigParser(unittest.TestCase):

    def setUp(self):
        # Создаем объект парсера перед каждым тестом
        self.parser = ConfigParser()
        self.parser.variables = {}  # Убедимся, что словарь переменных пустой

    def test_transform_value_integer(self):
        result = self.parser.transform_value("42")
        self.assertEqual(result, 42)

    def test_transform_value_float(self):
        result = self.parser.transform_value("42.5")
        self.assertEqual(result, 42.5)

    def test_transform_value_string(self):
        result = self.parser.transform_value('"hello"')
        self.assertEqual(result, "hello")

    def test_transform_value_boolean(self):
        self.assertEqual(self.parser.transform_value("true"), True)
        self.assertEqual(self.parser.transform_value("false"), False)

    def test_transform_value_postfix_expression(self):
        self.parser.variables = {'x': 5, 'y': 10}
        result = self.parser.transform_value("$[ x y + ]")
        self.assertEqual(result, 15)

    def test_transform_value_variable(self):
        self.parser.variables = {'var': 100}
        result = self.parser.transform_value("${var}")
        self.assertEqual(result, 100)

    def test_handle_constant_declaration(self):
        self.parser.handle_constant_declaration("10 -> testVar;")
        self.assertEqual(self.parser.variables['testVar'], 10)

    def test_parse_with_variables(self):
        input_data = """var a := 10
                        var b := 20
                        var result := ${a} + ${b}"""
        input_stream = StringIO(input_data)
        self.parser.parse(input_stream)
        self.assertEqual(self.parser.variables['a'], 10)
        self.assertEqual(self.parser.variables['b'], 20)

    def test_save_to_json(self):
        # Устанавливаем тестовые переменные
        self.parser.variables = {"x": 100, "y": 200}

        # Создаем StringIO для тестирования
        output_stream = StringIO()

        # Сохраняем данные в JSON формат
        self.parser.save_to_json(output_stream)

        # Ожидаемый результат
        expected_output = '{"variables": {"x": 100, "y": 200}, "comments": []}'

        # Проверяем совпадение
        self.assertEqual(json.loads(output_stream.getvalue()), json.loads(expected_output))

    def test_replace_variables_in_expression(self):
        expression = "10 + ${x}"
        self.parser.variables = {'x': 5}
        result = self.parser.replace_variables_in_expression(expression)
        self.assertEqual(result, "10 + 5")


if __name__ == '__main__':
    unittest.main()
