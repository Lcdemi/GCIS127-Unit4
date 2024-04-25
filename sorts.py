import math

def shift(a_list, index):
    target = a_list[index]
    while index > 0 and a_list[index-1] > target:
        a_list[index] = a_list[index-1]
        index -= 1
    a_list[index] = target

def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        shift(a_list, index)
    return a_list

def split(a_list):
    mid = len(a_list) // 2
    left = a_list[:mid]
    right = a_list[mid:]
    return left, right

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    if left_index < len(left):
        merged += left[left_index:]
    else:
        merged += right[right_index:]
    
    return merged

def merge_sort(a_list):
    if len(a_list) < 2:
        return a_list
    else:
        left, right = split(a_list)
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
        merged = merge(sorted_left, sorted_right)
        return merged
    
def partition(a_list, pivot):
    less_pivot = []
    same_pivot = []
    more_pivot = []
    for value in a_list:
        if value > pivot:
            more_pivot.append(value)
        elif value < pivot:
            less_pivot.append(value)
        else:
            same_pivot.append(value)
    return less_pivot, same_pivot, more_pivot

def quicksort(a_list):
    if len(a_list) <= 1:
        return a_list
    else:
        pivot = a_list[0]
        less, same, more = partition(a_list, pivot)
        sorted_less = quicksort(less)
        sorted_more = quicksort(more)
        
        return sorted_less + same + sorted_more
    
def quick_insertion_sort(a_list, n, stack = 1):
    n = len(a_list)
    if len(a_list) <= 1:
        return a_list
    elif stack > 2 * (math.log2(n)):
        return insertion_sort(a_list)
    else:
        less, equal, greater = partition(a_list, a_list[0])
        return quick_insertion_sort(less, n, stack = stack + 1) + equal + quick_insertion_sort(greater, n, stack = stack + 1)

# [1, 2, 3, 4, 5, 6, 7, 8]
# [1][2, 3, 4, 5, 6, 7, 8]
# [1][2][3, 4, 5, 6, 7, 8]
# [1][2][3][4, 5, 6, 7, 8]
# [1][2][3][4][5, 6, 7, 8]
# [1][2][3][4][5] 6, 7, 8]
# [1][2][3][4][5][6] 7, 8]
# [1][2][3][4][5][6][7][8]
