# An insertion sort compares values in turn, starting with the second value in the list. If this value is greater than the
# value to the left of it, no changes are made. Otherwise this value is repeatedly moved left until it meets a value that is less than it.
# The sort process then starts again with the next value.

# Big O Notation of Insertion Sort:
# O(n^2)

array = [1, 8, 15, 14, 2, 3, 7, 10, 9, 4, 6, 5, 11, 12, 13]

def insertion(list):
    indexing_length = range(1, len(list))

    for i in indexing_length:
        while list[i-1] > list[i] and i > 0:
            list[i-1], list[i] = list[i], list[i-1]
            i = i - 1

    return list

print(insertion(array))