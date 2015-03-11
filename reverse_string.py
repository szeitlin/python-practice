__author__ = 'szeitlin'

def reverse_string(word):
    """
    Return reversed string.

    :param word: str
    :return: str

    >>> reverse_string('mah')
    'ham'

    """
    charlist = [char for char in word]
    charlist.reverse() #in place
    return ''.join(charlist)

import doctest
doctest.testmod()
