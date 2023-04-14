# Дан список чисел. Определите, сколько в нем встречается различных чисел.

import random

amount_numbers = int(input('Set amount of numbers: '))
number = []
for i in range(amount_numbers):
    number.append(random.randint(0,100))
print(number)
result = set(number)
print(f'amount of unique numbers is {len(result)}')