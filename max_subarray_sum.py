__author__ = 'szeitlin'

def max_subarray_sum1(arr):
    """
    Returns contiguous subarray with largest sum.

    List comprehension version runs in O(n^2) time.

    (from http://20bits.com/article/introduction-to-dynamic-programming)

    :param arr: list
    :return: sum, range that designates location of the array by indices.
    """
    return max([(sum(arr[j:i]), (j,i)) for i in range(1,len(arr)+1) for j in range(i)])


def max_subarray_sum2(arr):
    """
    Returns contiguous subarray with largest sum.

    "optimal substructure" dynamic programming version
    runs in O(n) time.

    :param arr: list
    :return: sum, range that designates location of the array by indices.
    """

    bounds = (0,0)
    optimal = -float('infinity')
    temp = 0
    j = 0

    for i in range(len(arr)):
        temp = temp + arr[i]

        if temp > optimal:
            bounds = (j, i+1)
            optimal = temp

        if temp < 0:
            temp = 0
            j = i+1

    return (optimal, bounds)
