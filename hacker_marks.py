# Хакер Василий получил доступ к классному журналу и хочет заменить
# все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.
import random


def switch_marks(lst):
    max_mark = max(lst)
    min_mark = min(lst)
    for i in range(len(lst)):
        if lst[i] == max_mark:
            lst[i] = min_mark
    print(lst)


marks_amount = int(input('How many marks were there?: '))
marks = []
for i in range(marks_amount):
    marks.append(random.randint(1, 5))
print(marks)
switch_marks(marks)
