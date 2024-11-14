## Клонирование репозитория
Склонируйте репозиторий с исходным кодом и тестами:
```bash
git clone https://github.com/dima5778/konfig2
cd konfig2
```

## Запуск
Запуск эмулятора
```bash
python src/shell_emulator.py
```

## Структура проекта
```bash
/src
  shell_emulator.py
  commands.py
  test_commands.py
config.xml
start_script.sh
virtual_files.tar
```
## Запуск тестов
```bash
python -m unittest src/test_commands.py
```
