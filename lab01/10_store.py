#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Расчет для стола
table_code = goods['Стол']
table_items = store[table_code]
table_quantity = table_items[0]['quantity'] + table_items[1]['quantity']
table_cost = table_items[0]['quantity'] * table_items[0]['price'] + table_items[1]['quantity'] * table_items[1]['price']
print('Стол -', table_quantity, 'шт, стоимость', table_cost, 'руб')

# Расчет для дивана
sofa_code = goods['Диван']
sofa_items = store[sofa_code]
sofa_quantity = sofa_items[0]['quantity'] + sofa_items[1]['quantity']
sofa_cost = sofa_items[0]['quantity'] * sofa_items[0]['price'] + sofa_items[1]['quantity'] * sofa_items[1]['price']
print('Диван -', sofa_quantity, 'шт, стоимость', sofa_cost, 'руб')

# Расчет для стула
chair_code = goods['Стул']
chair_items = store[chair_code]
chair_quantity = chair_items[0]['quantity'] + chair_items[1]['quantity'] + chair_items[2]['quantity']
chair_cost = (chair_items[0]['quantity'] * chair_items[0]['price'] +
             chair_items[1]['quantity'] * chair_items[1]['price'] +
             chair_items[2]['quantity'] * chair_items[2]['price'])
print('Стул -', chair_quantity, 'шт, стоимость', chair_cost, 'руб')