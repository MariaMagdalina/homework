# Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

import os
clear = lambda: os.system('cls')
clear()

def game_prog():    # основная функция игры. возвращает количество конфет, которое выбрал игрок 
   g = int(input('Вы можете забрать от 1 до 28 конфет. Сколько конфет заберете? '))
   f = False
   while f != True:
      if g > 28 or g < 1:
         g = int(input('Вы можете забрать от 1 до 28 конфет. Сколько конфет заберете? '))
      else:
         f = True
   return g

from random import randint
pl_1 = 'Игрок 1 '
pl_2 = 'Игрок 2 '
if randint(1,2) == 2:  # жеребьевка
   pl_1, pl_2 = pl_2, pl_1 
print('Первый ход у ', pl_1)
   
sum_cand = 2021 # количество конфет
while sum_cand != 0:
   print('На столе конфет', sum_cand)
   print(pl_1, 'Ваш ход')   # для первого игрока
   g1 = game_prog()
   sum_cand -= g1   # отнимаем от общего количества конфет выбранные игроком
   if sum_cand <= 0:  # если игрок забрал все конфеты
      print(pl_1, 'Вы победили!!!')
      break
   
   print(pl_2, 'Ваш ход')   # все то же для второго игрока
   g2 = game_prog()
   sum_cand -= g2
   if sum_cand <= 0:
      print(pl_2, 'Вы победили!!!')
      break
   