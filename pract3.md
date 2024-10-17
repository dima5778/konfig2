## Задача 1
Для первого задания я использовал сайт https://jsonnet.jdocklabs.co.uk/ , чтобы реализвать код на языке Jsonnet.
```bash
{
  // Генерация списка групп
  groups: [std.format("ИКБО-%d-20", i) for i in std.range(1, 24)],

  // Список студентов
  students: [
    {
      name: "Иванов И.И.",  // Имя студента
      group: "ИКБО-4-20",   // Группа студента
      age: 19               // Возраст студента
    },
    {
      name: "Петров П.П.",
      group: "ИКБО-5-20",
      age: 18
    },
    {
      name: "Сидоров С.С.",
      group: "ИКБО-5-20",
      age: 18
    },
    {
      name: "Поспелов Д.Д.",     
      group: "ИКБО-23-20",
      age: 18
    }
  ],

  // Название предмета
  subject: "Конфигурационное управление"
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
A = "{" S "}"
B = "(" S ")"
C = a
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'S'))
```

## Задание 5
