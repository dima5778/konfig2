## Задача 1
1)Устонавливаю jsonnet в git bash с помощью choco install jsonnet перезахожу в него
2)Создаю файл Zd1.jsonnet
3)Использую  команду jsonnet Zd1.jsonnet -o Zd1_1.json
4) Посмотреть файл cat Pr3_1zd.json
Вывод
```bash
local groups = [
  "ИКБО-1-24",
  "ИКБО-2-24",
  "ИКБО-3-24",
  "ИКБО-4-24",
  "ИКБО-5-24",
  "ИКБО-6-24",
  "ИКБО-7-24",
  "ИКБО-8-24",
  "ИКБО-9-24",
  "ИКБО-10-24",
  "ИКБО-11-24",
  "ИКБО-12-24",
  "ИКБО-13-24",
  "ИКБО-14-24",
  "ИКБО-15-24",
  "ИКБО-16-24",
  "ИКБО-17-24",
  "ИКБО-18-24",
  "ИКБО-19-24",
  "ИКБО-20-24",
  "ИКБО-21-24",
  "ИКБО-22-24",
  "ИКБО-23-24",
  "ИКБО-24-24"
];

local student(name, age, group, subject) = {
  name: name,
  age: age,
  group: group,
  subject: subject,
};

local students = [
  student("Иванов И.И.", 19, "ИКБО-4-23", "Конфигурационное управление"),
  student("Петров П.П.", 18, "ИКБО-5-23", "Конфигурационное управление"),
  student("Сидоров С.С.", 18, "ИКБО-5-23", "Конфигурационное управление"),
  student("Поспелов", 18, "ИКБО-23-23", "Конфигурационное управление")
];

{
  groups: groups,
  students: students,
}
```


## Задача 2
Для второго задания нам нужно написать тоже самое на языке dhall
1)Устонавливаем язык dhall
2)Проверяем устоновку dhall-to-json --help
3)Создаём файл с содержимим 
4) dhall-to-json --file Zd1.dhall > Zd1_2.json
5)Смотрим содержимое cat Pr3_2zd.json
```bash
local groups = [
  "ИКБО-1-24",
  "ИКБО-2-24",
  "ИКБО-3-24",
  "ИКБО-4-24",
  "ИКБО-5-24",
  "ИКБО-6-24",
  "ИКБО-7-24",
  "ИКБО-8-24",
  "ИКБО-9-24",
  "ИКБО-10-24",
  "ИКБО-11-24",
  "ИКБО-12-24",
  "ИКБО-13-24",
  "ИКБО-14-24",
  "ИКБО-15-24",
  "ИКБО-16-24",
  "ИКБО-17-24",
  "ИКБО-18-24",
  "ИКБО-19-24",
  "ИКБО-20-24",
  "ИКБО-21-24",
  "ИКБО-22-24",
  "ИКБО-23-24",
  "ИКБО-24-24"
];

local student(name, age, group, subject) = {
  name: name,
  age: age,
  group: group,
  subject: subject,
};

local students = [
  student("Иванов И.И.", 19, "ИКБО-4-23", "Конфигурационное управление"),
  student("Петров П.П.", 18, "ИКБО-5-23", "Конфигурационное управление"),
  student("Сидоров С.С.", 18, "ИКБО-5-23", "Конфигурационное управление"),
  student("Поспелов", 18, "ИКБО-23-23", "Конфигурационное управление")
];

{
  groups: groups,
  students: students,
}
```
Вывод
```bash

```
## Задание 3
Просто добавляем BNF для языка едениц и нулей
```bash
BNF = '''
S = "10" | "100" | "11" | "101101" | "000"
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'S'))
```
![image](https://github.com/user-attachments/assets/b99eb2a2-f921-43e1-b442-972af5a4c419)


## Задание 4
Тоже самое только пустое значение в скобках обозначаю буквой а
```bash
BNF = '''
S = A | B | C
A = { S }
B = ( S )
C = a
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'S'))
```
![image](https://github.com/user-attachments/assets/da2e6d9d-7d53-4a6a-957b-66ffdee45490)


## Задание 5
```bash
BNF = '''
E = ( E B F ) | U ( E ) | F
F = P B P | U P | P
P = x | y | (x) | (y)
U = ~
B = & | V

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
'''
![image](https://github.com/user-attachments/assets/200e8694-0179-41e9-83d9-58902c332025)

