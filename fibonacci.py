__author__ = 'szeitlin'

def fib1(n):
    """
    Return the nth fibonacci number.

    recursive version runs in O(c^2) time.

    :param n: int
    :return: int

    """
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)



def fib2(n):
    """
    Return the nth fibonacci number.

    iterative dynamic programming version

    runs in O(n) time.

    :param n: int
    :return: int
    """
    n1 = 0
    n2 = 1

    for i in range(n-2):
        n2, n1 = n1, n1+n2

    return n2+n1

