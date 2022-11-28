#Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, список повторяемых и убрать дубликаты из заданной последовательности. Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]
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
# формируем список уникальных элементов
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
print(lst_unique) 
print(lst_repeat) 
print(lst_not_dupl) 