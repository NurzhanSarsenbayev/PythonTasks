# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

def simple_number(num):
    i=2
    while i<num-1 and num%i!=0:
       i+=1
    return i==num-1

number = int(input('Type your number: '))
print(simple_number(number))

    
    