import random

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + pivot + quick_sort(greater)


def fibonacci(n):
    if n in [1, 2]:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = left[i]
            i += 1
            k += 1


def random_generator_of_numbers(amount):
    num_list = []
    for i in range(amount):
       num_list.append(random.randint(1,6))
       i+=1
    return num_list

list_to_sort=random_generator_of_numbers(5)
print(quick_sort(list_to_sort))