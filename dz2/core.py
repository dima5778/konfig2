import subprocess
import json


def get_direct_dependencies(package_name):
    """
    Получить прямые зависимости указанного пакета.
    """
    try:
        result = subprocess.run(
            ['apk', 'info', '--depends', package_name],
            capture_output=True,
            text=True,
            check=True
        )
        # Убираем лишние строки и фильтруем зависимости
        dependencies = result.stdout.strip().split('\n')[1:]
        return [dep.strip() for dep in dependencies if dep.strip()]
    except subprocess.CalledProcessError:
        return []
    except Exception as e:
        print(f"Error while processing {package_name}: {e}")
        return []


def build_transitive_dependency_graph(package_name):
    """
    Строит транзитивный граф зависимостей для указанного пакета.
    """
    graph = {}  # Словарь для хранения зависимостей {пакет: [его зависимости]}
    visited = set()  # Множество для отслеживания уже обработанных пакетов

    def dfs(package):
        if package in visited:  # Пропускаем, если пакет уже обработан
            return
        visited.add(package)
        dependencies = get_direct_dependencies(package)
        graph[package] = dependencies
        for dep in dependencies:
            dfs(dep)  # Рекурсивно обрабатываем зависимости

    dfs(package_name)

    # Формируем вывод в формате DOT
    dot_output = ["digraph G {"]
    for pkg, deps in graph.items():
        for dep in deps:
            dot_output.append(f'    "{pkg}" -> "{dep}";')
    dot_output.append("}")
    return "\n".join(dot_output)


def main():
    # Чтение конфигурационного файла
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    # Получение данных из конфигурационного файла
    graphviz_path = config.get("graphviz_path", "")
    package_name = config.get("package_name", "")
    output_path = config.get("output_path", "dependencies.dot")

    if not package_name:
        print("Error: Package name not provided in config.")
        return

    # Строим граф зависимостей
    dot_graph = build_transitive_dependency_graph(package_name)

    # Выводим граф на экран
    print("\nGraphviz DOT format output:")
    print(dot_graph)

    # Сохраняем граф в файл
    with open(output_path, "w") as f:
        f.write(dot_graph)
        print(f"\nGraph saved to {output_path}")


if __name__ == "__main__":
    main()
