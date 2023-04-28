# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются
# в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы
# множеств.

import random

def random_generator_of_numbers(amount):
    num_list = []
    for i in range(amount):
       num_list.append(random.randint(1,6))
       i+=1
    return num_list

def list_sorting_up(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
    less = [i for i in list[1:] if i <= pivot]
    greater = [i for i in list[1:] if i > pivot]
    return list_sorting_up(less) + pivot + list_sorting_up(greater)

num_n = int(input('type first amount of numbers: '))
num_m = int(input('type second amount of numbers: '))

print(list_sorting_up(random_generator_of_numbers(num_n)))
print(list_sorting_up(random_generator_of_numbers(num_m)))
