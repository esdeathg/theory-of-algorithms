#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Списки с данными о семье
my_family = ['Отец', 'Мать', 'Брат']

# Список с именами и ростом членов семьи (в см)
my_family_height = [
    ['Отец', 180],
    ['Мать', 165],
    ['Брат', 185],
]

# Вывод роста отца
print(f'Рост отца - {my_family_height[0][1]} см')

# Расчет и вывод общего роста семьи
total_height = sum(person[1] for person in my_family_height)
print(f'Общий рост моей семьи - {total_height} см')