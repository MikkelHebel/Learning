# Quick sort selects a pivot element from the array and rearranges the elements such that all elements less than the pivot are
# on its left and all elements greater are on its right. This pivot element is now in its correct sorted position.
# The algorithm then recursively repeats this process for the left and right sub-arrays, sorting the entire array.

# Big O Notation of Quick Sort:
# O(n log n)

array = [1, 8, 15, 14, 2, 3, 7, 10, 9, 4, 6, 5, 11, 12, 13]

def quick(list):
    length = len(list)
    if length <= 1:
        return list
    else:
        pivot = list.pop()

    numbers_greater = []
    numbers_lower = []

    for item in list:
        if item > pivot:
            numbers_greater.append(item)
        else:
            numbers_lower.append(item)

    return quick(numbers_lower) + [pivot] + quick(numbers_greater)

print(quick(array))