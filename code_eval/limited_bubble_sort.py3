__author__ = 'szeitlin'

#python3 version for testing memory usage

from array import array
import re
import sys

test_cases = sys.argv[1]

def get_params(test_cases):
    """
    emits parameters for generating the sequence.

    :param test_cases: file, where each line contains 3 numbers that are space delimited.
    must ignore if line is blank
    :return: one list of parameters at a time
    """
    with open(test_cases, 'r') as infile:
        for row in infile:
            if len(row)<0:
               continue
            else:
                try:
                    yield row
                except Exception:
                    continue


def bubble_sort(p):
    """ steps through the list, comparing each pair of items so that the lower ones "bubble" to the front.
        has n-squared efficiency, so it's slow for big lists.

    list (int) -> list (int)
    >>> bubble_sort([3,2,8,7,6,5,4,1], 1)
    [2, 3, 7, 6, 5, 4, 1, 8]

    >>> bubble_sort([40,69,52,42,24,16,66],2)
    [40, 42, 24, 16, 52, 66, 69]

    >>> bubble_sort([54,46,0,34,15,48,47,53,25,18,50,5,21,76,62,48,74,1,43,74,78,29],6)
    [0, 15, 25, 18, 34, 5, 21, 46, 47, 48, 48, 1, 43, 50, 53, 29, 54, 62, 74, 74, 76, 78]

    """
    # identify first item and the item after it in the sequence

    row = get_params(test_cases)

    while row:
        try:
            onerow = next(row)
            seqlist, steps = p.split(onerow)
            seqtemp = [int(x) for x in seqlist.split()]
            seq = array('i', seqtemp)
            steps = int(steps)

            for j in range(steps):
                for i in range(len(seq)-1):

                    if seq[i+1] < seq[i]:
                        seq[i], seq[i+1] = seq[i+1], seq[i]

                    i += 1

            print(' '.join([str(x) for x in seq]))

        except StopIteration:
            break

    return


p = re.compile('\|')
bubble_sort(p)

