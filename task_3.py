# Создайте программу для игры в ""Крестики-нолики"".
import os
clear = lambda: os.system('cls')
clear()

def desk(): # наглядная таблица с номерами клеток
   for i in range(1,9,3):
      print(' -------------')
      print ("|", i, "|", i+1, "|", i+2, "|")
   print(' -------------') 

def table_game(list): # рабочая таблица 
   print('для того, чтобы сделать ход выберите номер клетки')
   for i in range(3):
      print(' -------------')
      print ("|", list[i*3], "|", list[i*3+1], "|", list[i*3+2], "|")
   print(' -------------') 

XO_list =[] # список, в который будем записывать X и O
for i in range(9):
   XO_list.append(' ')

desk()
table_game(XO_list)

step = 1 # помогает чередовать X и O
win = 0  # для фиксации победы
for i in range(9):   
   t = True
   while t != False:
      motion = int(input('Выберите номер клетки '))
      if XO_list[motion-1] != ' ':
         print('Эта клетка занята. Выберите другую')
      else:
         t = False
   if step == 1:
      XO_list[motion-1] = 'X'
   else:
      XO_list[motion-1] = 'O'
   step *= -1   

   clear()
   desk()
   table_game(XO_list)
    
   # далее проверка победителя   
   if XO_list[0] == 'X' and XO_list[4] == 'X' and XO_list[8] == 'X':
      print('выиграли X !!!')
      win = 1
   elif XO_list[0] == 'O' and XO_list[4] == 'O' and XO_list[8] == 'O':
      print('выиграли O !!!')
      win = 1
   elif XO_list[2] == 'X' and XO_list[4] == 'X' and XO_list[6] == 'X':
      print('выиграли X !!!')
      win = 1
   elif XO_list[2] == 'O' and XO_list[4] == 'O' and XO_list[6] == 'O':
      print('выиграли O !!!')
      win = 1     
   else:   
      for i in range(3):
         if XO_list[i*3] == 'X' and XO_list[i*3+1] == 'X' and XO_list[i*3+2] == 'X':
            print('выиграли X !!!')
            win = 1
         elif XO_list[i*3] == 'O' and XO_list[i*3+1] == 'O' and XO_list[i*3+2] == 'O':
            print('выиграли O !!!')
            win = 1   
         elif XO_list[i] == 'X' and XO_list[i+3] == 'X' and XO_list[i+6] == 'X':
            print('выиграли X !!!')
            win = 1
         elif XO_list[i] == 'O' and XO_list[i+3] == 'O' and XO_list[i+6] == 'O':
            print('выиграли O !!!')
            win = 1
   if win == 1:
      break
if win == 0:
   print('победителя нет!')     
   
        
