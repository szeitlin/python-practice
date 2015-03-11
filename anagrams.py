__author__ = 'szeitlin'

import random

def anagrams(word):
    """
    Return permutations of word.

    :param word: str
    :return: str

    >>> anagrams('Elvis')
    'lives'
    """
    letters = [x.lower() for x in word]

    aword = [letters.pop(random.randrange(len(letters))) for i in range(len(letters))]

    return ''.join(aword)

import doctest
doctest.testmod()
