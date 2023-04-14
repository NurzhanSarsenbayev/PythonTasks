# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число.

import random

list_length = int(input('Set list length: '))
list_move = int(input('How many elements should move?: '))
list = []
for i in range(list_length):
    list.append(random.randint(0,6))
print(list)
for i in range(list_move):
    # list.insert(0,list[-1])
    # list.pop(-1)
    list.insert(0,list.pop())
print(list)