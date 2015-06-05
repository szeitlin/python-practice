__author__ = 'szeitlin'

#first argument is a path to a file.
# each row contains a test case with a word
#and a binary code, separated with a space
#the length of each word is equal to the length of the code
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


def split_input(row):
    """

    :param row: lowercase letters, space, then zeros and ones in a string
    :return: two lists: list of letters, list of numbers
    """

    items = row.split()
    word = items[0]
    code = [int(x) for x in items[1]]
    return word, code

def encrypt():
    """
    returns word encrypted with binary mask.
    :param row: lowercase string, space, int
    :return: capitalized string

    >>> encrypt("hello 11001")
    HEllO
    >>> encrypt("world 10000")
    World
    >>> encrypt("cba 111")
    CBA
    """


    lines = get_params(test_cases)

    while lines:
        capped = ''
        try:
            row = next(lines)
            word, code = split_input(row)

            for i,flag in enumerate(code):
                if flag==1:
                    capped += word[i].upper()
                elif flag==0:
                    capped += word[i]
        except StopIteration:
            break

        print capped


encrypt()