# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.Добавьте возможность использования скобок, меняющих приоритет операций.
import re
import os
clear = lambda: os.system('cls')
clear()
str_arifm = input('введите арифетическое выражение: ')
a = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=', '+', '-', '*', '/', '(', ')'])
for i in str_arifm:
   if i not in a:
      print('Неверное выражение') 
      exit()
print(eval(str_arifm))
      