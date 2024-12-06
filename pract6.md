## 1 задание 
# Написать программу на Питоне, которая транслирует граф зависимостей civgraph в makefile в духе примера выше. Для мало знакомых с Питоном используется упрощенный вариант civgraph: civgraph.json.
```bash
import json

# Загрузка графа из JSON файла
def load_civgraph(file):
    with open(file, 'r') as f:
        return json.load(f)

# Функция для генерации Makefile
def generate_makefile(civgraph, target):
    visited = set()  # Для отслеживания посещенных задач
    result = []

    # Рекурсивная функция обхода зависимостей
    def visit(tech):
        if tech in visited:
            return
        visited.add(tech)
        for dep in civgraph.get(tech, []):
            visit(dep)
        result.append(tech)

    # Посещаем целевую технологию
    visit(target)

    # Печатаем задачи в порядке их выполнения
    for task in result:
        print(task)

if __name__ == '__main__':
    civgraph = load_civgraph('civgraph.json')
    target = input('Enter the target technology: ')  # Например, mathematics
    generate_makefile(civgraph, target)
```
# Вывод
![image](https://github.com/user-attachments/assets/b9196f49-06b3-4f5c-8b6a-90cbce4193a5)

## 2 Задание
# Реализовать вариант трансляции, при котором повторный запуск make не выводит для civgraph на экран уже выполненные "задачи".
```bash
import json

# Загрузка графа из JSON файла
def load_civgraph(file):
    with open(file, 'r') as f:
        return json.load(f)

# Функция для генерации Makefile
def generate_makefile(civgraph, target):
    visited = set()  # Для отслеживания посещенных задач
    result = []      # Список для хранения порядка выполнения задач
    completed_tasks = set()  # Для хранения уже выполненных задач

    # Рекурсивная функция обхода зависимостей
    def visit(tech):
        if tech in visited:
            return
        visited.add(tech)
        for dep in civgraph.get(tech, []):
            visit(dep)
        result.append(tech)

    # Посещаем целевую технологию
    visit(target)

    # Печатаем задачи в порядке их выполнения, если они еще не были выполнены
    for task in result:
        if task not in completed_tasks:
            print(task)
            completed_tasks.add(task)  # Добавляем задачу в выполненные

if __name__ == '__main__':
    civgraph = load_civgraph('civgraph.json')
    target = input('Enter the target technology: ')  # Например, mathematics
    generate_makefile(civgraph, target)
```
## 3 Задание 
# Добавить цель clean, не забыв и про "животное".
```bash
import json
import os

COMPLETED_TASKS_FILE = "completed_tasks.txt"

def load_completed_tasks():
    if os.path.exists(COMPLETED_TASKS_FILE):
        with open(COMPLETED_TASKS_FILE, 'r') as f:
            return set(f.read().splitlines())
    return set()

def save_completed_tasks(completed_tasks):
    with open(COMPLETED_TASKS_FILE, 'w') as f:
        f.write('\n'.join(completed_tasks))

def clean():
    if os.path.exists(COMPLETED_TASKS_FILE):
        os.remove(COMPLETED_TASKS_FILE)
        print("Cleaned completed tasks.")

def load_civgraph(file):
    with open(file, 'r') as f:
        return json.load(f)

def generate_makefile(civgraph, target):
    visited = set()
    result = []
    completed_tasks = load_completed_tasks()

    def visit(tech):
        if tech in visited or tech in completed_tasks:
            return
        visited.add(tech)
        for dep in civgraph.get(tech, []):
            visit(dep)
        result.append(tech)

    visit(target)

    for task in result:
        if task not in completed_tasks:
            print(task)
            completed_tasks.add(task)

    save_completed_tasks(completed_tasks)

if __name__ == '__main__':
    try:
        civgraph = load_civgraph('civgraph.json')
        action = input('Enter action (make/clean): ').strip().lower()

        if action == 'clean':
            clean()
        elif action == 'make':
            target = input('Enter the target technology: ').strip()
            generate_makefile(civgraph, target)
        else:
            print("Invalid action. Please enter 'make' or 'clean'.")
    except FileNotFoundError:
        print("Error: The file 'civgraph.json' was not found.")
    except json.JSONDecodeError:
        print("Error: The file 'civgraph.json' is not a valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
