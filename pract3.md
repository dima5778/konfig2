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
      name: "Ваше имя",     // Здесь добавьте свои данные
      group: "ИКБО-6-20",
      age: 20
    }
  ],

  // Название предмета
  subject: "Конфигурационное управление"
}
```
##Задача 2
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
      , { name = "Ваше имя", group = makeGroup 6, age = 20 }  -- Добавьте свои данные
      ]

-- Предмет
let subject = "Конфигурационное управление"

-- Финальная структура JSON
in { groups = groups, students = students, subject = subject }
```
