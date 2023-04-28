# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.

def reverse_list(n):
#     if n == 1:
#         return '1'
#     else:
#         return f'{n} -> {reverse_list(n-1)}'

    return ('1' if n==1 else f'{n} -> {reverse_list(n-1)}')

num = int(input('Type your N: '))
print(reverse_list(num))

    
