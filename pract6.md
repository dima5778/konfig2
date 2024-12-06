## 1 задание 
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

# 2 Задание
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
