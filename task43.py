# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.

import random
def list_random(size):
    list_n=[]
    for i in range(size):
        list_n.append(random.randint(1, 9))
    return list_n

def find_pair(list_n):
    count = 0
    for i in range(len(list_n)):
        for j in range(len(list_n)):
            if list_n[i] == list_n[j]:
                count+=1
                break
    find_pair(list_n)
                
            
            
list_size = int(input('How big is our list: '))
list_a = list_random(list_size)
print(list_a)
count=0
for i in range(len(list_a)):
    if list_a.count(i)>1:
        count+=list_a.count(i) //2
print(count)               