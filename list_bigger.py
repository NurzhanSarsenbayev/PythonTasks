# Дан список, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов списка,
# больших предыдущего (элемента с предыдущим номером)

import random

list_length = int(input('Set list length: '))
list = []
count = 0
for i in range(list_length):
    list.append(random.randint(0,6))
print(list)

for i in range(len(list)-1):
    if list[i]<list[i+1]:
        count+=1
print(f'{count} times')