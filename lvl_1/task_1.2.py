# Задача 1.2.
import random
import datetime
from datetime import timedelta

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
three_songs = random.choices(my_favorite_songs, k=3)
time_three_songs = round(sum(tm for song, tm in three_songs), 2)
print('Три песни звучат ' + str(time_three_songs) + ' минут')

print('#########')
# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

song1, tm1 = random.choice(list(my_favorite_songs_dict.items()))
song2, tm2 = random.choice(list(my_favorite_songs_dict.items()))
song3, tm3 = random.choice(list(my_favorite_songs_dict.items()))
time_three_songs_dict = round(tm1 + tm2 + tm3, 2)
print(f'Три песни: \n{song1, song2, song3} \nзвучат {str(time_three_songs_dict)} минут')

print('#########')
# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

print('#########')
# Дополнительно
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

for song, tm in my_favorite_songs_dict.items():
    stime = str(tm).split('.')
    sec = int(stime[0]) * 60 + int(stime[1])
    delta = timedelta(seconds=sec)
    print(f'Песня {song} - длительность {delta} минут')
