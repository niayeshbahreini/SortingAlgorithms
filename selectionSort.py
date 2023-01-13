

def selectionSort(myList):
    indexing_length = range(0, len(myList)-1)
    for i in indexing_length:
        minValue = i
        for j in range(i+1,len(myList)):
            if myList[j] < myList[minValue]:
                minValue = j


        if minValue !=i:
            myList[minValue],myList[i] = myList[i] , myList[minValue]
    return myList

print(selectionSort([1,3,4,66,11,9,1,2,3,]))