__author__ = 'szeitlin'

def split_teams(skills, split_indices):
    '''
    Takes sorted list of skills and splits into separate teams using split_indices based on duplicates alone
    (gaps are handled separately).

    >>> split_teams ([1,2,2,3,6,7,8],[2])
    [[1, 2], [2, 3, 6, 7, 8]]

    >>> split_teams([1,2,2,3,4,5,5,6],[2,6])
    [[1, 2], [2, 3, 4, 5], [5, 6]]

    :return: initial teams as a list of lists
    '''
    teams = []

#base case
    if len(split_indices)==1:
        for item in split_indices:
            teams.append(skills[:item])
            teams.append(skills[item:])
#recursive
    if len(split_indices)> 1:
        temp = []
        for item in split_indices:
            print item
            teams.append(skills[:item])
            temp.append(skills[item:])
            skills=temp
            print skills

    print teams
    return teams

split_teams([1,2,2,3,4,5,5,6],[2,6])

#want some kind of filter or groupby to apply the indices in one step? maybe use pandas series?

