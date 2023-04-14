# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),а Катя должна их отгадать.
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# number_sum = int(input('Sum of your numbers'))
# number_mult= int(input('Mutiplication of your numbers'))

from math import sqrt

'''
x+y = b => y = b-x
x*y = c => x*(b-x) = c => -x*x + b*x -c = 0
Так как a = -1 всегда в этой задаче, то я решил его не писать.
Решим квадратное уравнение:
'''

def calculate(b, c):
    D = b*b + 4*c  # считаем дискриминант
    if D > 0:  # если дискриминанат > 0 - два корня
        sq = sqrt(D)/2
        p = b/2
        x1 = p-sq
        x2 = p+sq
        return [x1, x2]

def main():
    b = int(input('Enter sum: '))
    c = -int(input('Enter mul: '))
    print(calculate(b, c))

main()