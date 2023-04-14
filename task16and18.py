# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
# 1 2 3 4 5
# 3
# -> 1

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
# 1 2 3 4 5
# 6
# -> 5


import random

list_size = int(input('Set size of your list: '))
list = []
count = 0
for i in range(list_size):
    list.append(random.randint(10,16))
print(list)
find_number= int(input('What number do you want to find?: '))
for i in range(list_size):
    if list[i]==find_number:
        count+=1
if count==0:
    temp_dif=abs(find_number-list[0])
    temp_number=list[0]
    for i in range(list_size):
        if temp_dif>abs(find_number-list[i]):
            temp_dif=abs(find_number-list[i])
            temp_number=list[i]
    print(f'There is no number that you wish to find, but closest is {temp_number}')
else:
    print(f'Amount of times your number was found is {count}')



