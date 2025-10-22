import re

num_list_1 = [0,1,2,3,4,5,6,7,8,9,10,17,25,43]
num_list_2 = [0,2,4,6,8,10,16,18,20]

print("Num list 1: " + str(num_list_1))
print("Num list 2: " + str(num_list_2))


def get_dictionary_from_num_lists(numList1, numList2):
    set1 = set(numList1)
    set2 = set(numList2)
    num_list_dictionary = {}
    
    num_list_dictionary["intersection"] = set1.intersection(set2) # o set1 & set2
    num_list_dictionary["union"] = set1.union(set2) # o set1 | set2
    num_list_dictionary["symetric_diff"] = set1.symmetric_difference(set2)
    
    return num_list_dictionary


print("Output dictionary: " + str(get_dictionary_from_num_lists(num_list_1, num_list_2)))
