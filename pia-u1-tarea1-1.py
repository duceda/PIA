my_list_1 = [4, -1, 2, 4, 3, -5, 0, 2]

print("Input list 1: " + str(my_list_1))


## Opcion 1 - Dividirlo en funciones independientes
def delete_negative_numbers(numList):
    positiveList = list(filter(lambda x : x >= 0, numList))
    return positiveList

def delete_duplicated_numbers(numList):
    uniqueList = set(numList)
    return uniqueList
    

def sort_list_numbers(numList):
    sortedList = sorted(numList)
    return sortedList

print("Output list 1: " + str(sort_list_numbers(delete_duplicated_numbers(delete_negative_numbers(my_list_1)))))


## Opcion 2 - Hacerlo todo en una línea importando numpy
import numpy

my_list_2 = [4, -1, 2, 4, 3, -5, 0,  2]
print("Input list 2: " + str(my_list_2))
print("Output list 2:" + str(list(numpy.unique(list(filter(lambda x : x >= 0, my_list_2))))))