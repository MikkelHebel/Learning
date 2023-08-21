# Bogo sort, also humorously known as "stupid sort," is a highly inefficient and random sorting algorithm. It works by repeatedly shuffling
# the elements of an array randomly until the elements happen to be in sorted order by chance. Due to its random nature,
# it has an average-case time complexity that's practically unbounded and is not suitable for any serious sorting tasks.

# Big O Notation of Bogo Sort:
# O((n+1)!)
import random

array = [1, 8, 15, 14, 2, 3, 7, 10, 9, 4, 6, 5, 11, 12, 13]
array2 = [3, 1, 2, 4]
array3 = [1, 8, 15, 14, 2, 3, 7, 10, 9, 4]

def bogo(list):
    sorted = False
    random.shuffle(list)

    while sorted == False:
        sorted = True
        for i in range(0, len(list) - 1):
            if list[i] > list[i+1]:
                sorted = False
                random.shuffle(list)


    return list

print(bogo(array3))