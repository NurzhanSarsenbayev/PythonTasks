# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n 
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. 
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, не превосходящее 105. 
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.

# "def sum_of_proper_divisors(n):
#     s = 0
#     for k in range(1, n // 2 + 1):
#         if n % k == 0:
#             s += k
#     return s

# for i in range(1, 10000):
#     j = sum_of_proper_divisors(i)
#     if i < j <= n and i == sum_of_proper_divisors(j):
#         print(i, j)"
        
def prompt(msg):
    a = int(input(msg))
    return a

def summarize(number, sum = 0):
    for item in range(1,number//2+1):
        if number%item == 0:
            sum += item
    return sum

k = 10000
print(my_list := [i for i in range(k)])
for item in my_list:    
    if item == summarize(summarize(item)) and item != summarize(item):
        print(item, summarize(item))
