from random import randint

def selection_sort(unsorted_list):
    sorted_list = unsorted_list[:]

    for i in range(len(sorted_list)):
        current_min_index = i

        for j in range(i + 1, len(sorted_list)):
            if sorted_list[j] < sorted_list[current_min_index]:
                current_min_index = j
        
        sorted_list[i], sorted_list[current_min_index] = sorted_list[current_min_index], sorted_list[i]
        
    return sorted_list

def insertion_sort(unsorted_list):
    sorted_list = unsorted_list[:]
    for i in range(1, len(sorted_list)):
        item_to_insert = sorted_list[i]
        j = i

        while j > 0 and item_to_insert < sorted_list[j-1]:
            sorted_list[j] = sorted_list[j-1]
            j -= 1
        
        sorted_list[j] = item_to_insert

    return sorted_list

def bubble_sort(unsorted_list):
    sorted_list = unsorted_list[:]
    for i in range(len(sorted_list)):
        for j in range(len(sorted_list) - 1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]

    return sorted_list

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    mid = len(unsorted_list) // 2
    left_half = merge_sort(unsorted_list[:mid])
    right_half = merge_sort(unsorted_list[mid:])

    sorted_list = []
    left_index = right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            sorted_list.append(left_half[left_index])
            left_index += 1
        else:
            sorted_list.append(right_half[right_index])
            right_index += 1

    sorted_list.extend(left_half[left_index:])
    sorted_list.extend(right_half[right_index:])

    return sorted_list

def quick_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    pivot = unsorted_list[len(unsorted_list) // 2]
    left_half = [x for x in unsorted_list if x < pivot]
    middle = [x for x in unsorted_list if x == pivot]
    right_half = [x for x in unsorted_list if x > pivot]

    return quick_sort(left_half) + middle + quick_sort(right_half)

def generate_random_list(n):
    return [randint(0, 100) for _ in range(n)]