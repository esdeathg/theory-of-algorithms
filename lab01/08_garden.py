#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# Создаем множества цветов
garden_set = set(garden)
meadow_set = set(meadow)

# 1. Выводим все виды цветов
all_flowers = garden_set.union(meadow_set)
print("Все виды цветов:", sorted(all_flowers))

# 2. Выводим цветы, которые растут и там и там (пересечение)
common_flowers = garden_set.intersection(meadow_set)
print("Цветы, растущие и в саду и на лугу:", sorted(common_flowers))

# 3. Выводим цветы, которые растут только в саду (разность)
only_garden = garden_set.difference(meadow_set)
print("Цветы, растущие только в саду:", sorted(only_garden))

# 4. Выводим цветы, которые растут только на лугу (разность)
only_meadow = meadow_set.difference(garden_set)
print("Цветы, растущие только на лугу:", sorted(only_meadow))