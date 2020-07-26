def deleteListElements(myList, deleteVector):
    for x in deleteVector:
        del myList[int(x)]
    return myList