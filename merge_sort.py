__author__ = 'szeitlin'

def merge_sort(arr):
    """
    Recursively sorts a list.

    :param arr: list
    :return: sorted list

    >>> merge_sort([20,3,1,2,12,11,9,7])
    [1, 2, 3, 7, 9, 11, 12, 20]
    """
    middle = len(arr)//2
    left = arr[0:middle]
    right = arr[middle:]
    newlist = []

    while len(newlist)< len(arr):
        if left != []:
            if min(left) < min(right):
                newlist.append(min(left))
                left.remove(min(left))
        elif right !=[]:
            if min(right) < min(left):
                newlist.append(min(right))
                right.remove(min(right))

    return newlist

import doctest
doctest.testmod()
