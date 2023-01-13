
def insertion_sort(myList):
    indexing_length = range(1, len(myList)) #all values after thet first one
    for i in indexing_length:
        valueToSort = myList[i] #take items one by one
        #print(value_to_sort)

        while myList[i-1] > valueToSort and i >0: #while item in the left is greater than right one 
            myList[i], myList[i-1] = myList[i-1], myList[i]
            i = i -1
    return myList


print(insertion_sort([7,8,9,8,7,6,5,6,7,8,9,8,7,6,5,6,7,8]))