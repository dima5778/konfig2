# Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).
## Код
``` bash
grep '.*' /etc/passwd | cut -d: f1 | sort
```

```bash
localhost:~# grep '.*' /etc/passwd | cut -d: -f1 | sort
adm
at
bin
cron
cyrus
daemon
dhcp
ftp
games
guest
halt
lp
mail
man
news
nobody
ntp
operator
postmaster
root
shutdown
smmsp
squid
sshd
svn
sync
uucp
vpopmail
xfs
```

# Задача 2
Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 5 наибольших портов, как показано в примере ниже:
## Код
```bash
awk '{print $2, $1}' /etc/protocols | sort -nr | head -n 5
```
```bash
localhost:~# awk '{print $2, $1}' /etc/protocols | sort -nr | head -n 5
103 pim
98 encap
94 ipip
89 ospf
81 vmtp
```

# Задача 3
Написать программу banner средствами bash для вывода текстов, как в следующем примере (размер баннера должен меняться!):
## Код
```bash
#!/bin/bash

text=$*
length=${#text}

for i in $(seq 1 $((length + 2))); do
    line+="-"
done

echo "+${line}+"
echo "| ${text} |"
echo "+${line}+"
```
```bash
dimap@dima5778 MINGW64 ~/downloads
$ ./3.sh "123"
+-----+
| 123 |
+-----+

```

# Задача 4
Написать программу для вывода всех идентификаторов (по правилам C/C++ или Java) в файле (без повторений).
## Код
```bash
#!/bin/bash

file="$1"

id=$(grep -o -E '\b[a-zA-Z]*\b' "$file" | sort -u)

```
```bash
dimap@dima5778 MINGW64 ~/downloads grep -oE '\b[a-zA-Z_][a-zA-Z0-9_]*\b' hello.c | grep -vE '\b(int|void|return|if|else|for|while|include|stdio)\b' | sort | uniq
h
hello
main
n
printf
world
```

# Задача 5
Написать программу для регистрации пользовательской команды (правильные права доступа и копирование в /usr/local/bin).
## Код
```bash
#!/bin/bash

file=$1

chmod 755 "./$file"

sudo cp "$file" /usr/local/bin/
```

Например, пусть программа называется reg:
```bash
dimap@dima5778 MINGW64 ~/downloads ./reg.sh banner.sh
dimap@dima5778 MINGW64 ~/downloads ls /usr/local/bin
banner.sh  ngrok
```

# Задача 6
Написать программу для проверки наличия комментария в первой строке файлов с расширением c, js и py.
## Код
```bash
#!/bin/bash

# Проход по всем файлам с расширениями .c, .js, .py
for file in $(find . -type f \( -name "*.c" -o -name "*.js" -o -name "*.py" \)); do
    # Чтение первой строки файла
    first_line=$(head -n 1 "$file")
    
    # Проверка, начинается ли строка с комментария (для C, JS и Python)
    if [[ "$file" == *.c || "$file" == *.js ]]; then
        if [[ "$first_line" =~ ^(//|/\*) ]]; then
            echo "Файл $file содержит комментарий в первой строке."
        else
            echo "Файл $file не содержит комментарий в первой строке."
        fi
    elif [[ "$file" == *.py ]]; then
        if [[ "$first_line" =~ ^# ]]; then
            echo "Файл $file содержит комментарий в первой строке."
        else
            echo "Файл $file не содержит комментарий в первой строке."
        fi
    fi
done

```

