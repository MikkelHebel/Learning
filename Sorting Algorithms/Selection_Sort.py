# Selection sort is a simple sorting algorithm that divides an array into two parts: the sorted portion and the unsorted portion.
# In each iteration, it selects the smallest (or largest) element from the unsorted portion and
# swaps it with the first element of the unsorted portion. This process continues until the entire array is sorted.

# Big O Notation of Selection Sort:
# O(n^2)

array = [1, 8, 15, 14, 2, 3, 7, 10, 9, 4, 6, 5, 11, 12, 13]

def selection(list):
    indexing_length = range(0, len(list) - 1)

    for i in indexing_length:
        min_value = i

        for next in range(i+1, len(list)):
            if list[next] < list[min_value]:
                min_value = next
        
        if min_value != i:
            list[min_value], list[i] = list[i], list[min_value]
    
    return list

print(selection(array))