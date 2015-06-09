__author__ = 'szeitlin'

#python3 version 

import itertools
import re
import sys


test_cases = sys.argv[1]

def get_params(test_cases):
    """
    emits each row

    :param test_cases: file with strings and number of iterations on the end
    must ignore if line is blank

    :return: one row at a time
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


def sorcery(p):
    """
    thanks to friend opensorceress for suggestion to use filter

    :return:
    """
    row = get_params(test_cases)

    while row:
        try:
            onerow = next(row)
            seqlist, steps = p.split(onerow)
            seq = [int(x) for x in seqlist.split()]

            steps = int(steps)

            itertools.repeat(filter(bubble_sort(seq), seq), times=steps)

            print(' '.join([str(x) for x in seq]))

        except StopIteration:
            break

    return



def bubble_sort(seq):

    for i in range(len(seq)-1):

        if seq[i+1] < seq[i]:
            seq[i], seq[i+1] = seq[i+1], seq[i]

        i += 1

    return seq



p = re.compile('\|')
sorcery(p)


