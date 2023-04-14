# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 
# 0! = 1 Решить задачу используя цикл while

number = int(input('Type your number: '))
count=1
fact=1
while count<=number:
    fact*=count
    print(fact)
    count+=1