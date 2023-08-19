# The method works by examining each set of adjacent elements in the string, from left to right,switching their positions
# if they are out of order. The algorithm then repeats this process until it can run through the entire string and find
# no two elements that need to be swapped.

# Big O Notation of Bubble Sort:
# O(n^2)

array = [1, 8, 15, 14, 2, 3, 7, 10, 9, 4, 6, 5, 11, 12, 13]

def bubble(list):
    sorted = False

    while sorted == False:
        sorted = True
        # This for loop will iterate through the list and compare each element to the next element.
        # If the element is greater than the next element, it will swap the two elements.
        # If the element is less than the next element, it will not swap the two elements.
        # This will continue until the list is sorted.
        for i in range(0, len(list) - 1):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
    
    return list

print(bubble(array))