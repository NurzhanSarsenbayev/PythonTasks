# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
import random
coin_amount = int(input('Enter amount of coins: '))
count_0=0
count_1=0
for i in range(coin_amount):
    coin_side = random.randint(0, 1)
    print(coin_side, end=" ")
    if coin_side==0:
        count_0+=1
    if coin_side==1:
        count_1+=1
# print(f'\n 0 = {count_0}, 1 = {count_1}')
print(f'\nYou need to flip {count_0} coins to even things out' if count_1>count_0 else f'\nYou need to flip {count_1} coins to even things out')
    
# for i in range(watermelon):
#     weigth = random.randint(MIN_WEIGHT, MAX_WEIGHT)
#     print(weigth, end=" ")
#     if weigth > max_weigth:
#         max_weigth = weigth
#     if weigth < min_weigth:
#         min_weigth = weigth