# Binary search is a fast and efficient algorithm used to locate a specific target value within a sorted collection, such as an array.It works by repeatedly
# dividing the search range in half, eliminating half of the remaining elements each time, until the target is found or the search range is
# reduced to zero. This approach significantly reduces the number of comparisons required compared to linear search, making it logarithmic in time complexity.

# Big O Notation of Binary Search:
# O(log n)

array = [1, 3, 4, 5, 8, 9, 10, 11, 12, 14, 15, 17, 19, 20, 21, 23, 24, 25, 27, 29, 30, 31, 32, 35, 36, 38, 39, 40, 42, 43, 44, 47, 48, 49, 50, 52, 54, 55, 56, 58, 59, 60, 62, 63, 65, 66, 67, 69, 70, 71, 72, 74, 75, 76, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 94, 96, 97, 98, 99, 100]

def binary_search(list, find):
    start = list[0]
    end = len(list) - 1

    while start <= end:
        midpoint = start + (end - start) // 2
        midpoint_value = list[midpoint]

        if midpoint_value == find:
            return midpoint
        
        elif find < midpoint_value: # Check left
            end = midpoint - 1
        
        else: # Check right
            start = midpoint + 1

    return None

print(binary_search(array, 12))