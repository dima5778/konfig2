## Задача 1
Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?
```bash
(venv) C:\Users\dimap\OneDrive\Рабочий стол\confa\task_2>pip3 show matplotlib
Name: matplotlib
Version: 3.9.2
Summary: Python plotting package
Home-page:
Author: John D. Hunter, Michael Droettboom
Author-email: Unknown <matplotlib-users@python.org>
License: License agreement for matplotlib versions 1.3.0 and later
=========================================================
Location: C:\Users\dimap\OneDrive\Рабочий стол\confa\task_2\venv\Lib\site-packages
Requires: contourpy, cycler, fonttools, kiwisolver, numpy, packaging, pillow, pyparsing, python-dateutil
Required-by:
```
Установка без pip, тоже самое надо сделать со всеми зависимостями
```bash
pip install git+https://github.com/matplotlib/matplotlib.git
cd matplotlib
python setup.py install
```
