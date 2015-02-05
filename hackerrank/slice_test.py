__author__ = 'szeitlin'

from itertools import izip, chain

def split_teams(skills, split_indices):
    """
    Try using islice to do this for you. Looks like it will do the version for 1 split very easily, as a generator.
    Not sure it will help with the multi-split case?

    >>> split_teams ([1,2,2,3,6,7,8],2)
    [[1, 2], [2, 3, 6, 7, 8]]

    >>> split_teams([1,2,2,3,4,5,5,6],[2,6])
    [[1, 2], [2, 3, 4, 5], [5, 6]]

    :param skills: iterable (list)
    :param split_indices is also a list

    :return:
    """
    #solution from stack overflow. I still don't quite understand how it works.

    pairs = izip(chain([0], split_indices), chain(split_indices, [None]))

    return (skills[i:j] for i,j in pairs)

for n in split_teams ([1,2,2,3,6,7,8],[2]):
    print n

for y in split_teams([1,2,2,3,4,5,5,6],[2,6]):
    print y