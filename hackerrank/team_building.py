__author__ = 'szeitlin'

#using stdin and stdout, each input will contain:

#t = number test cases, where each test line contains:

#n number of students, followed by a sequence of x skill level values

#idea is to maximize team size, where teams have consecutive skill values with no gaps & no duplicates

#return the smallest team size - check this

from itertools import izip, chain
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


def get_test_size(line, line_count):
    '''
    Read the first line of the input.

    Can use this to limit the number of loops based on the total input.

    :return: t
    '''
    try:
        if line_count==0:
            return test_size = line
        elif len(line) > 0:
            print "this is not a test_size line"
            continue
    except Exception as e:
        print e

def read_more():
    '''
    Fancy way to call the generator.
    :return:
    '''
    gen = read_input()
    return next(gen)

def get_student_list_length(line, line_count):
    '''
    Read the first number of each line after the first line.
    :return: n (int)
    '''
    try:
        if line_count > 0:
            return n = int(line[0])
        elif len(line) <=0:
            print "this is not a student list line"
            continue
    except Exception as e:
        print e

def get_skill_levels(n, line):
    '''
    Takes skill levels from input string and converts to list of ints.

    Copy skill levels to a tuple to return later?

    :return:skills as list of x (ints)

    '''
    skills = []
    for i in range(n):
        skills.append(int(line[i]))

    print skills
    return skills

def sorted_skills(skills):
    '''
    Create temporary list to evaluate skill levels for grouping.
    Currently sorts in place.
    :return: sorted (list of ints)
    '''
    return sorted(skills)

def find_duplicates(n, skills):
    """
    Check skills list for duplicates, and use these as initial team-splitting criteria. If more than two in a row,
    I think (?) this will return the indices of the odd-numbered ones.

    >>> find_duplicates([0,1,2,3])
    []

    >>> find_duplicates([1,2,2,3,4])
    [1]

    >>> find_duplicates([1,2,3,3,3,4])
    [2,4]

    :return: index (or indices) for non-unique numbers

    """
    split_indices = []

    for i in range(n - 1):
        if skills[i] == skills[i+1]:  #this is also not working when I try to test it, b/c it says list index out of range
            split_indices.append(i)

    return split_indices

def find_gap(teams):
    '''
    Compare numbers in the sub-lists looking for the index where they stop being sequential (after sort).

    >>> find_gap([[0,1,2],[0,1,2,3]])

    >>> find_gap([[0,2,3],[2,3,5,6]])
    [[0,0],[1,1]]

    >>> find_gap([[0,2,4],[1,2,3,4]])
    [[0,0],[0,1]]

    >>> find_gap([[1,2,3,5])
    2

    >>> find_gap([-1,1,2])
    0

    :return: list of indices to identify gaps = the index of the last sequential element before the gap.
    where the numbers are in order of [team, member]
    '''
    gap_indices = []
    team_number=-1

    for team in teams:
        team_number +=1
        for j in range(len(team)-1):
            if team[j+1] - team[j] >1:
                gap_indices.append([team_number,j])

    return gap_indices

    #might be good to use filter for this, in conjunction with split_teams?

def split_further(teams, gap_indices):
    """
    Splits teams at gaps, using the gap_indices.

    >>> split_further([[0,2,3],[2,3,5,6]], [[0,1],[1,1]])
    [[0],[2,3],[2,3],[5,6]]

    >>> split_further([[0,2,4], [1,2,3,4]], [[0,0],[0,1]])
    [[0],[2],[4],[1,2,3,4]]

    :param teams: list of lists to split
    :param gap_indices: list of paired coordinates
    :return:
    """
    final_teams=[]




def split_teams(skills, split_indices):
    """
    Try using itertools to do this for you. Note that it's a generator, so you have to call the results out accordingly.

    >>> split_teams ([1,2,2,3,6,7,8],2)
    [[1, 2], [2, 3, 6, 7, 8]]

    >>> split_teams([1,2,2,3,4,5,5,6],[2,6])
    [[1, 2], [2, 3, 4, 5], [5, 6]]

    :param skills: iterable (list)
    :param split_indices is also a list

    :return:
    """
    #solution from stack overflow.

    pairs = izip(chain([0], split_indices), chain(split_indices, [None]))

    return (skills[i:j] for i,j in pairs)



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
        if len(team) < shortest:
            smallest = team
            print smallest
        else:
            continue
    return smallest










line, line_count = read_input()
t = get_test_size(line, line_count)
line, line_count = read_more() #want to loop over this t times
n = get_student_list_length(line, line_count)
skills = get_skill_levels(n, line)
skills = sorted_skills(skills)
split_indices = find_duplicates(n, skills)
teams = split_teams(skills, split_indices)
#remove gaps
find_smallest_team(teams)
