# Devides a list in half and deletes 1 half of the list until the array is sorted.

array = [1, 2, 3, 4, 5, 6, 13, 7, 9]

def thanos_sort(list):
    sorted = False

    while sorted == False:
        sorted = True
        i = 0

        while i < len(list) - 1:
            list.pop(i)
            i += 1
        
        for i in range(0, len(list) - 1):
            if list[i] > list[i+1]:
                sorted = False

    return list

print(thanos_sort(array))