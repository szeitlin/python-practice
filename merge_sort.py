__author__ = 'szeitlin'

def merge_sort(arr):
    """
    Recursively sorts a list.

    :param arr: list
    :return: sorted list

    >>> merge_sort([20,3,1,2,12,11,9,7])
    [1, 2, 3, 7, 9, 11, 12, 20]
    """
    print(arr)
    middle = len(arr)//2
    left = arr[0:middle]
    print(left)
    right = arr[middle:]
    print(right)
    newlist = []

    while len(newlist)< len(arr):
        if left == [] and right == []:
            break
        if left !=[]:
            if right !=[]:
                if min(left) < min(right):
                    print("left is smaller than right")
                    newlist.append(min(left))
                    left.remove(min(left))
        else:
            newlist.append(min(right))

        if right !=[]:
            if left!=[]:
                if min(right) < min(left):
                    print("right is smaller than left")
                    newlist.append(min(right))
                    right.remove(min(right))
        else:
            newlist.append(min(left))
        print(newlist)

    print(newlist)
    return newlist

#import doctest
#doctest.testmod()
