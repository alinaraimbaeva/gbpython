#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 01:54:20 2023

@author: alinaraimbaeva
"""
'''2. Пользователь вводит время в секундах. 
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк.'''

sec=int(input('Введите время в секундах: '))

hour=round(sec/3600,2)
minute=round(sec/60,2)
print(f"Время в формате чч:мм:сс - {hour}:{minute}:{sec}")
