#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 02:45:03 2023

@author: alinaraimbaeva
"""
'''3. Узнайте у пользователя число n. 
Найдите сумму чисел n + nn + nnn. 
Например, пользователь ввёл число 3. 
Считаем 3 + 33 + 333 = 369.'''

n=input('Введите число: ')
print(f"{n} + {n*2} + {n*3} = {int(n)+int(n*2)+int(n*3)}")