# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
# Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.
# import random

# watermelon_count = int(input('How many watermelons are there: '))
# max_weight=0
# min_weight=0
# # while watermelon_count>0:
# #     watermelon_weight=random.randint(0,300)
# #     if  watermelon_weight>max_weight:
# #         watermelon_weight=max_weight
# #     else:
# #         watermelon_weight=min_weight
# #     print(f'{watermelon_weight}',end = ' ')
# #     watermelon_count-=1
    
# # print(max_weight)
# # print(min_weight)

import random

MAX_WEIGHT = 5000
MIN_WEIGHT = 100


watermelon = int(input("Введите количество арбузов: "))
weigth = 0
max_weigth = MIN_WEIGHT
min_weigth = MAX_WEIGHT

for i in range(watermelon):
    weigth = random.randint(MIN_WEIGHT, MAX_WEIGHT)
    print(weigth, end=" ")
    if weigth > max_weigth:
        max_weigth = weigth
    if weigth < min_weigth:
        min_weigth = weigth
print(f"\nАрбуз для себя получился на {max_weigth} г, а для тёщи {min_weigth} г. Как-то так")