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
![image](https://github.com/user-attachments/assets/573b2b92-c5ff-4ba6-b844-8266e0a4eafa)
![image](https://github.com/user-attachments/assets/ef74a768-b547-48c9-b0ca-75f582f06572)
![image](https://github.com/user-attachments/assets/2c426e74-8b45-4675-9082-64cfd7898d0b)




## Задача 2
Для второго задания нам нужно написать тоже самое на языке dhall
1)Устонавливаем язык dhall
2)Проверяем устоновку dhall-to-json --help
3)Создаём файл с содержимим 
4) dhall-to-json --file Zd1.dhall > Zd1_2.json
5)Смотрим содержимое cat Zd1_2.json
```bash
let Prelude = https://prelude.dhall-lang.org/v20.2.0/package.dhall
let generateGroup = λ(i : Natural) → "ИКБО-" ++ Prelude.Natural.show i ++ "-20"

in  { groups =
      [ generateGroup 1, generateGroup 2, generateGroup 3, generateGroup 4
      , generateGroup 5, generateGroup 6, generateGroup 7, generateGroup 8
      , generateGroup 9, generateGroup 10, generateGroup 11, generateGroup 12
      , generateGroup 13, generateGroup 14, generateGroup 15, generateGroup 16
      , generateGroup 17, generateGroup 18, generateGroup 19, generateGroup 20
      , generateGroup 21, generateGroup 22, generateGroup 23, generateGroup 24
      ]
    , students =
      [ { age = 19, group = "ИКБО-4-20", name = "Иванов И.И." }
      , { age = 18, group = "ИКБО-5-20", name = "Петров П.П." }
      , { age = 18, group = "ИКБО-5-20", name = "Сидоров С.С." }
      , { age = 20, group = "ИКБО-23-20", name = "Поспелов Д.Д." }
      ]
    , subject = "Конфигурационное управление"
 }
```
Вывод
![image](https://github.com/user-attachments/assets/333386f7-c6d9-4df6-9a68-05ff81a4bc80)
![image](https://github.com/user-attachments/assets/50e4e543-5f50-4041-aeae-7f5a7693b0c0)
![image](https://github.com/user-attachments/assets/4b1861e1-da02-48b6-826b-d1dcf295a52b)




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



