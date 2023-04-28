# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.

import random
def list_random(size):
    list_n=[]
    for i in range(size):
        list_n.append(random.randint(1, 9))
    return list_n

list_size = int(input('How big is our list: '))
list_a = list_random(list_size)
print(list_a)

count=0
for i in range(1,len(list_a)-1):
    if list_a[i-1]<list_a[i] and list_a[i]>list_a[i+1]:
        print(list_a[i])
        count+=1
print(f'count is {count}')
# list_a = (random.randint(0,20) for _ in range(list_size))

