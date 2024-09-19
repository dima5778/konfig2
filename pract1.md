# Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).
## Код
```bash
grep '.*' /etc/passwd | cut -d: -f1 | sort
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
