my_list = [4, -1, 2, 4, 3, -5, 0, 2]

print("Input list: " + str(my_list))

def transform_list(numList):
    positiveList = list(filter(lambda x : x >= 0, numList))
    uniqueList = set(positiveList)  
    finalList = sorted(uniqueList)
    return finalList

print("Output list: " + str(transform_list(my_list)))
