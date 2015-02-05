__author__ = 'szeitlin'

def find_smallest_team(teams):
    """
    Compare length of each team sublist within the parent list teams.
    note: this way of doing it is very slow, might be faster to sort first or use some smarter algorithm to divide & conquer

    >>> find_smallest_team([[0,1],[1,2],[1,2,3],[0]])
    [0]

    :return: smallest team (shortest sublist)
    """
    #simplest way is to just compare each of them, starting with the first (arbitrary)

    smallest = teams[0]

    for team in teams:
        if len(team) < smallest:
            smallest = team
            #print smallest
        else:
            continue
    return smallest

find_smallest_team([[0,1],[1,2],[1,2,3],[0]])