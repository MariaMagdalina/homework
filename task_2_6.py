#Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, список повторяемых и убрать дубликаты из заданной последовательности. 
import os
clear = lambda: os.system('cls')
clear()
from random import randint
N = 10
lst = [] # список
lst_unique = [] # список уникальных элементов
lst_repeat = [] # список повторяемых элементов
lst_not_dupl = [] # список без дубликатов

for i in range(N):
   lst.append(randint(0, 10)) # заполняем список случайными числами 
print('список: ', lst)
for i in lst: # перебираем каждый элемент из списка
   k = 0      # количество повторов элемента в списке
   for j in range(N): # сравниваем текущий элемент с каждым элементом в списке
      if i not in lst_not_dupl:
         lst_not_dupl.append(i)
      if i == lst[j]:
         k += 1       
   if k < 2:
      lst_unique.append(i)
   elif i not in lst_repeat:
      lst_repeat.append(i)
print('Уникальные элементы: ', lst_unique) 
print('Повторяемые элементы: ', lst_repeat) 
print('Спислк без дубликатов: ', lst_not_dupl) 