def nestedList(x, newList):
    for l in x:
        if isinstance(l, list):
            nestedList(l, newList)
        else:
            newList.append(l)

def flattenList(nested):
    newList = []
    for x in nested:
        if isinstance(x, list):
            nestedList(x, newList)
            
        else:
            newList.append(x)

    return newList