#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 02:51:35 2023

@author: alinaraimbaeva
"""
'''4. Пользователь вводит целое положительное число. 
Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции.'''

n=int(input("Число: "))
max_n=0
while n>0:
    s=n%10
    if max_n<s:
        max_n=s
    n//=10
print(f"Самая большая цифра в числе - {max_n}")