# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

# number = int(input('Type your number: '))
# fib = 1
# count = 1
# while count <= number:
#     current = (fib-1)+(fib-2)
#     fib += 1
#     count += 1
#     print(fib)
# if number == fib:
#     print(count)
# else:
#     print(-1)

n1 = 0
n2 = 1
i = 1

num = int(input('type your number: '))
while n2 < num:
    n1, n2 = n2, n1+n2
    # n1 = n2
    # n2= n1+n2
    i+=1
# if n2 == num:
#     print(i)
# else:
#     print(-1)
print(i if num == n2 else-1)
