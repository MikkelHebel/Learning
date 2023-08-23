# Merge sort is a divide-and-conquer sorting algorithm that works by recursively dividing an array into halves until
# each sub-array contains only one element.It then merges these sorted sub-arrays back together in a sorted manner.
# This process of dividing and merging continues until the entire array is sorted.

# Big O Notation of Merge Sort:
# O(n * log(n))

array = [1, 8, 15, 14, 2, 3, 7, 10, 9, 4, 6, 5, 11, 12, 13]

def merge(list):
    if len(list) > 1:
        left_arr = list[:len(list)//2]
        right_arr = list[len(list)//2:]

        # Recursion
        merge(left_arr)
        merge(right_arr)

        # Merge
        i = 0 # Keep track of the left most element of the left array
        j = 0 # Keep track of the left most element of the right array
        k = 0 # Keep track of the index in the merged array.

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                list[k] = left_arr[i]
                i += 1
            else:
                list[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            list[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            list[k] = right_arr[j]
            j += 1
            k += 1

        return list

print(merge(array))