import re
import json
import sys

class ConfigParser:
    def __init__(self, output_file=None):
        self.variables = {}
        self.comments = []
        self.output_file = output_file

    def transform_value(self, value):
        """
        Преобразует строковое значение в соответствующий тип данных.
        :param value: строка
        :return: преобразованное значение
        """
        value = value.strip()
        if value.startswith('$[') and value.endswith(']'):
            # Постфиксная нотация
            expression = value[2:-1].strip()
            tokens = expression.split()
            stack = []
            for token in tokens:
                if token in self.variables:  # Переменная
                    stack.append(self.variables[token])
                elif token.isdigit():  # Число
                    stack.append(float(token))
                elif token in ['+', '-', '*', '/']:  # Арифметическая операция
                    if len(stack) < 2:
                        raise ValueError("Недостаточно операндов для операции")
                    b = stack.pop()
                    a = stack.pop()
                    if token == '+':
                        stack.append(a + b)
                    elif token == '-':
                        stack.append(a - b)
                    elif token == '*':
                        stack.append(a * b)
                    elif token == '/':
                        stack.append(a / b)
                else:
                    raise ValueError(f"Не удалось интерпретировать токен '{token}'.")
            if len(stack) != 1:
                raise ValueError("Некорректное выражение в постфиксной нотации")
            return stack[0]
        elif value.startswith('${') and value.endswith('}'):
            # Переменная
            variable_name = value[2:-1].strip()
            if variable_name in self.variables:
                return self.variables[variable_name]
            else:
                raise ValueError(f"Переменная '{variable_name}' не определена.")
        elif value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        elif value.isdigit():
            return int(value)
        else:
            try:
                return float(value)
            except ValueError:
                return value.strip('"')

    def evaluate_postfix(self, tokens):
        stack = []

        for token in tokens:
            if token.replace('.', '', 1).isdigit():  # Если токен — число
                stack.append(float(token))
            elif token in {'+', '-', '*', '/'}:  # Операторы
                if len(stack) < 2:
                    raise ValueError(f"Ошибка: недостаточно операндов для операции '{token}'.")
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a / b)
            else:
                raise ValueError(f"Ошибка: некорректный токен '{token}' в выражении.")

        if len(stack) != 1:
            raise ValueError(f"Ошибка: некорректное выражение.")
        return stack[0]

    def handle_constant_declaration(self, line):
        match = re.match(r'(.+)\s*->\s*(\w+);', line)
        if match:
            value = match.group(1).strip()
            name = match.group(2).strip()

            value = self.transform_value(value)

            if value is not None:
                self.variables[name] = value
                print(f"Добавлена константа: {name} = {value}")
            else:
                print(f"Ошибка: Не удалось обработать значение '{value}' для константы '{name}'.")
        else:
            match_postfix = re.match(r'(\$.+)\s*->\s*(\w+);', line)
            if match_postfix:
                expression = match_postfix.group(1).strip()
                name = match_postfix.group(2).strip()

                value = self.transform_value(expression)

                if value is not None:
                    self.variables[name] = value
                    print(f"Добавлена константа (с выражением): {name} = {value}")
                else:
                    print(f"Ошибка: Не удалось обработать выражение '{expression}' для константы '{name}'.")
            else:
                print(f"Ошибка: Некорректный синтаксис в строке '{line}'.")

    def replace_variables_in_expression(self, expression):
        if '${' in expression and '}' in expression:
            variables_in_expression = re.findall(r'\${(\w+)}', expression)
            for var in variables_in_expression:
                if var in self.variables:
                    expression = expression.replace(f'${{{var}}}', json.dumps(self.variables[var]))
                else:
                    print(f"Ошибка: Переменная '{var}' не найдена в выражении '{expression}'.")
                    return None
        return expression

    def parse(self, input_stream):
        lines = input_stream.readlines()
        for line in lines:
            line = line.strip()

            if not line or line.startswith('#'):
                continue

            if line.startswith('::'):
                self.comments.append(line[2:].strip())
                continue

            if '->' in line and line.endswith(';'):
                self.handle_constant_declaration(line)
            elif line.startswith('var '):
                self.handle_variable_declaration(line)
            elif line.startswith('list('):
                self.handle_list_declaration(line)
            elif line.startswith('dict('):
                self.handle_dict_declaration(line)
            else:
                print(f"Ошибка: Некорректный синтаксис в строке '{line}'.")

    def handle_variable_declaration(self, line):
        match = re.match(r'var (\w+) := (.+)', line)
        if match:
            var_name = match.group(1)
            value = self.evaluate_expression(match.group(2).strip())
            self.variables[var_name] = value
            print(f"Добавлена переменная: {var_name} = {value}")
        else:
            print(f"Ошибка: Некорректный синтаксис переменной в строке '{line}'.")

    def handle_list_declaration(self, line):
        match = re.match(r'list\((.+)\)', line)
        if match:
            items = match.group(1).split(',')
            items = [self.evaluate_expression(item.strip()) for item in items]
            self.variables['list'] = items
            print(f"Добавлен список: {items}")
        else:
            print(f"Ошибка: Некорректный синтаксис списка в строке '{line}'.")

    def handle_dict_declaration(self, line):
        match = re.match(r'dict\((.+)\)', line)
        if match:
            dict_content = match.group(1)
            items = dict_content.split(',')

            dictionary = {}
            for item in items:
                key_value_match = re.match(r'(\w+):\s*(.+)', item.strip())
                if key_value_match:
                    key = key_value_match.group(1)
                    value = key_value_match.group(2)
                    value = self.evaluate_expression(self.replace_variables_in_expression(value.strip()))
                    dictionary[key] = value
                else:
                    print(f"Ошибка: Некорректный формат элемента словаря '{item.strip()}'.")
                    return

            self.variables['dict'] = dictionary
            print(f"Добавлен словарь: {dictionary}")
        else:
            print(f"Ошибка: Некорректный синтаксис словаря в строке '{line}'.")

    def evaluate_expression(self, expression):
        expression = self.replace_variables(expression)

        if re.match(r'^\d+(\.\d+)?$', expression):
            return float(expression) if '.' in expression else int(expression)

        if expression.startswith('"') and expression.endswith('"'):
            return expression[1:-1]

        if expression.lower() in ('true', 'false'):
            return expression.lower() == 'true'

        try:
            return eval(expression)
        except Exception as e:
            print(f"Ошибка вычисления выражения '{expression}': {e}")
            return None

    def replace_variables(self, expression):
        matches = re.findall(r'\${(\w+)}', expression)
        for var in matches:
            if var in self.variables:
                expression = expression.replace(f'${{{var}}}', str(self.variables[var]))
            else:
                print(f"Ошибка: Переменная '{var}' не найдена.")
                return None
        return expression

    def save_to_json(self, output):
        """
        Сохраняет текущие переменные и комментарии в JSON-формате.
        :param output: путь к файлу или поток для записи
        """
        data = {
            "variables": self.variables,
            "comments": self.comments
        }
        if isinstance(output, str):  # Если передан путь к файлу
            with open(output, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        else:  # Если передан поток (например, StringIO)
            json.dump(data, output, ensure_ascii=False, indent=4)


def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "output.json"

        # Открываем файл с явным указанием кодировки UTF-8
        with open(input_file, 'r', encoding='utf-8') as file:
            parser = ConfigParser(output_file)
            parser.parse(file)
            parser.save_to_json(output_file)
    else:
        print("Ошибка: Не указан файл входных данных или выходной файл.")


if __name__ == '__main__':
    main()
