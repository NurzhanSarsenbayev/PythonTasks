# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number_limit = int(input('Type in your number: '))
number_2 = 2
while number_2<=number_limit:
  print(number_2)
  number_2*=2