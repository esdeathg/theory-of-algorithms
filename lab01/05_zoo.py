#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Исходный список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# 1. Посадить медведя между львом и кенгуру
zoo.insert(1, 'bear')
print("1. После добавления медведя:", zoo)

# 2. Добавить птиц в конец зоопарка
birds = ['rooster', 'ostrich', 'lark']
zoo.extend(birds)
print("2. После добавления птиц:", zoo)

# 3. Убрать слона
zoo.remove('elephant')
print("3. После удаления слона:", zoo)

# 4. Найти клетки льва и жаворонка (нумерация с 1 для человека)
lion_cage = zoo.index('lion') + 1
lark_cage = zoo.index('lark') + 1
print(f"4. Лев сидит в клетке №{lion_cage}, жаворонок в клетке №{lark_cage}")