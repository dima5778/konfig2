## Задача 1
Для первого задания я использовал сайт https://jsonnet.jdocklabs.co.uk/ , чтобы реализвать код на языке Jsonnet.
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
```bash
-- Тип данных для студента
let Student = { name : Text, group : Text, age : Natural }

-- Функция для создания группы
let makeGroup = \(i : Natural) -> "ИКБО-${Natural/show i}-20"

-- Генерация списка групп от 1 до 24
let groups =
      List/build Text (λ(i : Natural) → makeGroup (i + 1)) (List/range 0 23)

-- Список студентов
let students =
      [ { name = "Иванов И.И.", group = makeGroup 4, age = 19 }
      , { name = "Петров П.П.", group = makeGroup 5, age = 18 }
      , { name = "Сидоров С.С.", group = makeGroup 5, age = 18 }
      , { name = "Поспелов Д.Д.", group = makeGroup 23, age = 18 }  
      ]

-- Предмет
let subject = "Конфигурационное управление"

-- Финальная структура JSON
in { groups = groups, students = students, subject = subject }
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

## Задание 5
