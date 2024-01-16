# Goes through an non ordered list, if the next value is out of order eleminate it from the list.

array = [1, 2, 3, 9, 8, 11, 9, 8, 12, 14, 2, 3, 7, 10, 9, 15, 6, 5, 11, 12, 13]

def stalin_sort(list):
    i = 0
    while i < len(list) - 1:
        if list[i] > list [i+1]:
            list.pop(i+1)
        else:
            i += 1
        
    return list


print(stalin_sort(array))