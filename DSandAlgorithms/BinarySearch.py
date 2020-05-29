
def binarySearch(list, val, max, min):
    list.sort()
    median = (max - min)//2 + 1
    if list[median] == val:
        print(median)
    elif list[0] == val:
        print(0)
    elif list[len(list)-1] == val:
        print(len(list) -1)
    elif list[median] > val:
        return binarySearch(list, val, median - 1, min)
    else:
        return binarySearch(list, val, max, median + 1)

list = [ 12, 11, 13, 5, 6, 7]
binarySearch(list, 13, len(list)-1, 0)
