# Создайте программу для игры с конфетами человек против бота.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
def game_prog():
   g = int(input('Вы можете забрать от 1 до 28 конфет. Сколько конфет заберете? '))
   f = False
   while f != True:
      if g > 28 or g < 1:
         g = int(input('Вы можете забрать от 1 до 28 конфет. Сколько конфет заберете? '))
      else:
         f = True
   return g

import os
clear = lambda: os.system('cls')
clear()
from random import randint

name = input('введите Ваше имя: ')
pl_1 = 'Master'
if randint(1,2) == 2:
   pl_1 = name
print('ход игрока ', pl_1)

sum_cand = 2021
while sum_cand != 0:
   print('На столе конфет', sum_cand)
   if pl_1 == 'Master':                # я не успела доделать, но идея есть 
      if 58 < sum_cand <= 86:          # нельзя допускать, чтобы мастеру осталось 58 конфет
         g2 = sum_cand - 58            # идея - нужно оставить игроку 29 конфет, тогда он проиграет
         print('Master забрал ', g2 )
         sum_cand -= g2
      elif sum_cand <= 57:
         g2 = sum_cand-29         
         print('Master забрал ', g2 )
         sum_cand -= g2
      elif sum_cand <= 28:
         g2 = sum_cand
         print('Master забрал ', g2 )
         sum_cand -= g2
      else:
         g2 = randint(1,28)             # иначе выдаем случайные числа
         print('Master забрал ', g2 )
         sum_cand -= g2
      if sum_cand <= 0:
         print('Master победил!!!')
         break
      
      g1 = game_prog()
      sum_cand -= g1
      if sum_cand <= 0:
         print('Вы победили!!!')
         break
   else:
      g1 = game_prog()
      sum_cand -= g1
      if sum_cand <= 0:
         print('Вы победили!!!')
         break
      
      if 58 < sum_cand <= 86:          # нельзя допускать, чтобы мастеру осталось 58 конфет
         g2 = sum_cand - 58            # идея - нужно оставить игроку 29 конфет, тогда он проиграет
         print('Master забрал ', g2 )
         sum_cand -= g2
      elif sum_cand <= 57:
         g2 = sum_cand-29         
         print('Master забрал ', g2 )
         sum_cand -= g2
      elif sum_cand <= 28:
         g2 = sum_cand
         print('Master забрал ', g2 )
         sum_cand -= g2
      else:
         g2 = randint(1,28)             # иначе выдаем случайные числа
         print('Master забрал ', g2 )
         sum_cand -= g2
      if sum_cand <= 0:
         print('Master победил!!!')
         break