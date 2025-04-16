#!/usr/bin/env python3
# -*- coding: utf-8 -*-

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Первый фильм (ручной поиск первой запятой)
comma_pos = 0
while my_favorite_movies[comma_pos] != ',':
    comma_pos += 1
first_movie = my_favorite_movies[:comma_pos]
print(first_movie)

# Последний фильм (ручной поиск с конца)
comma_pos = len(my_favorite_movies) - 1
while my_favorite_movies[comma_pos] != ',':
    comma_pos -= 1
last_movie = my_favorite_movies[comma_pos + 2:]
print(last_movie)

# Второй фильм (поиск второй запятой)
first_comma_pos = 0
while my_favorite_movies[first_comma_pos] != ',':
    first_comma_pos += 1

second_comma_pos = first_comma_pos + 1
while my_favorite_movies[second_comma_pos] != ',':
    second_comma_pos += 1

second_movie = my_favorite_movies[first_comma_pos + 2:second_comma_pos]
print(second_movie)

# Второй с конца (поиск предпоследней запятой)
last_comma_pos = len(my_favorite_movies) - 1
while my_favorite_movies[last_comma_pos] != ',':
    last_comma_pos -= 1

prev_comma_pos = last_comma_pos - 1
while my_favorite_movies[prev_comma_pos] != ',':
    prev_comma_pos -= 1

second_last_movie = my_favorite_movies[prev_comma_pos + 2:last_comma_pos]
print(second_last_movie)