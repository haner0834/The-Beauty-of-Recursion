import random

def quick_sort(array: list[int]) -> list[int]:
    if len(array) <= 1: return array

    left: list[int] = []
    right: list[int] = []

    middle_count = random.randint(0, len(array) - 1)
    middle_item = array[middle_count]

    for item in array:
        if item > middle_item: right.append(item)
        else: left.append(item)

    print(left, right, "mid=", middle_item)
    
    return quick_sort(left) + quick_sort(right)

