#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
text_first = 'aaatt @4444444 kkkk'
text_new = '' # для записи сжатой строки
prev_i = '' # предыдущий элемент
count = 0   # для подсчета количества элементов
for i in text_first:
   if prev_i == '': # проверка для первого элемента
      prev_i = i  
      count += 1
   elif i == prev_i: # если элемент повторяется
      count += 1
   else:
      text_new += str(count) + prev_i # добавляем в строку - сколько раз встречался элемент и сам элемент
      prev_i = i
      count = 1
text_new += str(count) + prev_i # добавляем в строку последний элемент и его количество
print(text_first)         # первичная строка
print(text_new)     # сжатая строка


text_second = '' # восстановленная строка
for i in range(1, len(text_new), 2):
   text_second += text_new[i] * int(text_new[i-1])                      
print(text_second)         


