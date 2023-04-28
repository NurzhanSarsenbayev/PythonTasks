# 39. Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве
import random
def list_random(size):
    list_n=[]
    for i in range(size):
        list_n.append(random.randint(1, 9))
    return list_n


list_size = int(input('how big are our lists: '))
list_a = list_random(list_size)
list_b = list_random(list_size)
print(list_a)
print(list_b)

for i in list_a:
    if i not in list_b:
        print(i, end = ' ')

