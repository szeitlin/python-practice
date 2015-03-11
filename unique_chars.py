__author__ = 'szeitlin'

def unique_chars(word):
    """
    Find non-repeated characters.

    :param word: str
    :return: str

    >>> unique_chars('abba')
    'ab'
    >>> unique_chars('True')
    'True'
    >>> unique_chars('Elviss')
    'Elvis'
    """
    new_word = []

    for char in word:
        if char not in new_word:
            new_word.append(char)

    return ''.join(new_word)

import doctest
doctest.testmod()
