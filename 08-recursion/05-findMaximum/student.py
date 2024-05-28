
def findMaximum(list):
    if list == []:
        raise IndexError
    if list[-1] > findMaximum(list[:-1]):
        return list[-1]
    else : 
        return findMaximum(list[-2])