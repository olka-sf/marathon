"""
"Итак, стартуем с небольшой задачки. В каждом языке программирования есть способ получить текущее
 время.

Предлагаю написать программу, которая приветствует Вас следующим образом:

C 00 часов до 04 часов включительно программа при запуске пишет - ""Доброй ночи, {username}""
С 05 часов до 09 часов включительно программа при запуске пишет - ""Доброе утро, {username}""
С 10 часов до 16 часов включительно программа при запуске пишет - ""Добрый день, {username}""
С 17 часов до 23 часов включительно программа при запуске пишет - ""Добрый вечер, {username}""

Само собой, {username} должен заменяться на Ваше имя."
"""

import datetime
import getpass

def say_hi(get_hour, username):
    if 0 <= get_hour <= 4:
        print("Good night, " + username)
    elif 5 <= get_hour <= 9:
        print("Good morning, " + username)
    elif 10 <= get_hour <= 16:
        print("Good day, " + username)
    else:
        print("Good evening, " + username)

get_pst_time = datetime.datetime.now(datetime.timezone.utc).astimezone()
#test1 print(get_pst_time)

get_hour = int(get_pst_time.strftime('%H'))
#test2 print(get_hour)

username = getpass.getuser()
#test3 print(username)

say_hi(get_hour, username)
