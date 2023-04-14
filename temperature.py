# Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.

import random

days = 30
index=0
count=1
# random.randit(-3,3)
temperature=0
max_temp_count=0
while index<days:
    temperature+=random.randint(-3,3)
    print(f'temperature {index} -> {temperature}')
    if temperature>0:
        count+=1
        temp_count=count
        if temp_count>max_temp_count:
            max_temp_count=temp_count
    else:
        count=0
    index+=1
print(f'longest streak {max_temp_count}')