# Alpine Linux Dependency Graph Visualizer

## Описание

Инструмент для визуализации графа зависимостей пакетов в Alpine Linux. Граф строится в формате Graphviz DOT и выводится на экран в виде кода.

##Установка 

1.**Клонируйте репозиторий:**
 ```bash
   git clone https://github.com/dima5778/konfig2
   cd alpine-dependency-graph
   ```
2.Установите необходимые зависимости:
```bash
sudo apt-get install graphviz
pip install pytest
```

## Конфигурация

1.Создайте config.json:

```json
{
  "graphviz_path": "/usr/bin/dot",
  "package_name": "bash",
  "output_path": "dependencies.dot"
}
```

## Пример использования

1. Запустите скрипт:
   ```bash
   python core.py config.json
   ```
2. Пример вывода графа:
   ```bash
   digraph G {
    "bash" -> "/bin/sh";
    "bash" -> "so:libc.musl-x86_64.so.1";
    "bash" -> "so:libreadline.so.8";
    "/bin/sh" -> "busybox=1.36.1-r0";
    "/bin/sh" -> "busybox-binsh-1.36.1-r7 depends on:";
    "/bin/sh" -> "busybox=1.36.1-r7";
    "/bin/sh" -> "dash-binsh-0.5.12-r2 depends on:";
    "/bin/sh" -> "dash=0.5.12-r2";
    "/bin/sh" -> "yash-binsh-2.54-r3 depends on:";
    "/bin/sh" -> "yash=2.54-r3";
    "so:libc.musl-x86_64.so.1" -> "musl-1.2.4-r2 depends on:";
    "so:libreadline.so.8" -> "so:libc.musl-x86_64.so.1";
    "so:libreadline.so.8" -> "so:libncursesw.so.6";
    "so:libncursesw.so.6" -> "ncurses-terminfo-base=6.4_p20230506-r0";
    "so:libncursesw.so.6" -> "so:libc.musl-x86_64.so.1";
   }
}

## Тестирование
Запустите тесты:
```bash
python3 -m unittest test_core.py
```

## Требования к окружению
**Убедитесь, что:**
- apk доступен в командной строке для получения зависимостей пакетов.
- Graphviz установлен, и путь к dot указан в config.json.
- Python 3.6 или более поздней версии.

## Возможные проблемы и их решения

- **Ошибка Package not found:**

- Убедитесь, что указанный пакет существует в репозитории Alpine и доступен для анализа.
- **Ошибка Object '<sha1>' not found:**

- Возможно, проблема с неправильным именем пакета или его зависимостями.
- **Граф не читаем или слишком большой:**

- Попробуйте изменить параметры визуализации Graphviz или ограничьте количество пакетов для более четкого отображения.

