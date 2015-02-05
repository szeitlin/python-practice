__author__ = 'szeitlin'

import sys

def read_input():
    ''' Takes stdin, converts to a generator which will yield one line at a time.

    >>> read_input()
    4
    >>> read_input()
    7 4 5 2 3 -4 -3 -5

    :return:
    '''
    line = ""
    line_count = 0
    while True:
        try:
            line = sys.stdin.readline()
            line_count +=1
        except KeyboardInterrupt:
            break
        if not line:
            break

    yield line, line_count



def read_more():
    '''
    Fancy way to call the generator.
    :return:
    '''
    gen = read_input()
    return next(gen)

read_input()
read_more()
