## Задача 1
1)Устонавливаю jsonnet в git bash с помощью choco install jsonnet перезахожу в него
2)Создаю файл Zd1.jsonnet
3)Использую  команду jsonnet Zd1.jsonnet -o Zd1_1.json
4) Посмотреть файл cat Zd1_1.json
```bash
local arr = std.makeArray(25, function(x) "ИKБO-" + (x + 1) + "-23");

local Person(age, group, name) = {
  age: age,
  group: arr[group - 1],
  name: name,
};

{
  groups: arr,
  students: [
    Person(19, 4, 'Иванов И.И.'),
    Person(18, 5, 'Петров П.П.'),
    Person(18, 5, 'Сидоров С.С.'),
    Person(18, 23, 'Поспелов Д.Д.'),
  ],
  subject: "",
}
```
Вывод
```bash
{
  "groups": [
    "ИКБО-1-23",
    "ИКБО-2-23",
    "ИКБО-3-23",
    "ИКБО-4-23",
    "ИКБО-5-23",
    "ИКБО-6-23",
    "ИКБО-7-23",
    "ИКБО-8-23",
    "ИКБО-9-23",
    "ИКБО-10-23",
    "ИКБО-11-23",
    "ИКБО-12-23",
    "ИКБО-13-23",
    "ИКБО-14-23",
    "ИКБО-15-23",
    "ИКБО-16-23",
    "ИКБО-17-23",
    "ИКБО-18-23",
    "ИКБО-19-23",
    "ИКБО-20-23",
    "ИКБО-21-23",
    "ИКБО-22-23",
    "ИКБО-23-23",
    "ИКБО-24-23"
  ],
  "students": [
    {
      "age": 19,
      "group": "ИКБО-4-23",
      "name": "Иванов И.И"
    },
    {
      "age": 18,
      "group": "ИКБО-5-23",
      "name": "Петров П.П."
    },
    {
      "age": 18,
      "group": "ИКБО-5-23",
      "name": "Сидоров С.С."
    },
    {
      "age": 18,
      "group": "ИКБО-23-23",
      "name": "Поспелов Д.Д."
    }
  ],
  "subject": "Конфигурационное управление"
}
```

## Задача 2
Для второго задания нам нужно написать тоже самое на языке dhall
1)Устонавливаем язык dhall
2)Проверяем устоновку dhall-to-json --help
3)Создаём файл с содержимим 
4) dhall-to-json --file Zd1.dhall > Zd1_2.json
5)Смотрим содержимое cat Zd1_2.json
```bash
let Student = { name : Text, group : Text, age : Natural }

let makeGroup = \(i : Natural) -> "ИКБО-${Natural/show i}-20"

let groups =
      List/fold
        Natural
        (List/range 1 24)
        (List Text)
        (\(i : Natural) (acc : List Text) -> acc # [makeGroup i])
        ([] : List Text)

let students =
      [ { name = "Иванов И.И.", group = makeGroup 4, age = 19 }
      , { name = "Петров П.П.", group = makeGroup 5, age = 18 }
      , { name = "Сидоров С.С.", group = makeGroup 5, age = 18 }
      , { name = "Поспелов Д.Д.", group = makeGroup 23, age = 18 }
      ]

let subject = "Конфигурационное управление"

in { groups = groups, students = students, subject = subject }
```
Вывод
```bash
{
  "groups": [
    "ИКБО-1-23", 
    "ИКБО-2-23", 
    "ИКБО-3-23", 
    "ИКБО-4-23",
    "ИКБО-5-23", 
    "ИКБО-6-23", 
    "ИКБО-7-23",
    "ИКБО-8-23",
    "ИКБО-9-23", 
    "ИКБО-10-23", 
    "ИКБО-11-23", 
    "ИКБО-12-23",
    "ИКБО-13-23",
    "ИКБО-14-23", 
    "ИКБО-15-23", 
    "ИКБО-16-23",
    "ИКБО-17-23",
    "ИКБО-18-23",
    "ИКБО-19-23", 
    "ИКБО-20-23",
    "ИКБО-21-23",
    "ИКБО-22-23",
    "ИКБО-23-23", 
    "ИКБО-24-23"
  ]
  "students": [
    {
      "name": "Иванов И.И.",
      "group": "ИКБО-4-23",
      "age": 19
    },
    {
      "name": "Петров П.П.",
      "group": "ИКБО-5-23",
      "age": 18
    },
    {
      "name": "Сидоров С.С.",
      "group": "ИКБО-5-23",
      "age": 18
    },
    {
      "name": "Поспелов Д.Д.",
      "group": "ИКБО-23-23",
      "age": 18
    }
  ],
  "subject": "Конфигурационное управление"
}
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
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
```
![image](https://github.com/user-attachments/assets/c2a351b8-b314-4388-b642-728c6b190b7b)



