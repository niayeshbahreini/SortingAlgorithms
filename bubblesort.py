

def bubble(myList):
    indexingLenght = len(myList) -1 #because index from 0 but len count from 1
    sortedList = False

    while not sortedList : #as long as sortedList is False we do following actions
        sortedList = True
        for i in range(0,indexingLenght):
            if myList[i] > myList[i+1]:
                sortedList = False
                myList[i] ,myList[i+1] =myList[i+1] ,myList[i]

    return myList

print(bubble([3,48,6,0,88,4,67,63]))