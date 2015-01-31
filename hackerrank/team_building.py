__author__ = 'szeitlin'

#using stdin and stdout, each input will contain:

#t = number test cases, where each test line contains:

#n number of students, followed by a sequence of x skill level values

#idea is to maximize team size, where teams have consecutive skill values with no gaps & no duplicates

#return the smallest team size - check this

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


def remove_dups(uns):
    ''' unsorted list -> unsorted list with no duplicates
        remove duplicates from an unsorted list.
        >>>remove_dups([2,3,2,1,5,3,1])
	[2,3,1,5]
    '''
    unique = []
    for item in uns:
        if item not in unique:
            unique.append(item)
        else:
            continue

    return unique


def split_teams(skills):
    '''
    Takes sorted list of skills and splits into separate teams if gaps are > 1.

    >>> split_teams ([1,2,3,6,7,8])
    [1,2,3], [6,7,8]

    :return: list of lists
    '''
    teams = []
    for i in skills:
        if ((i+1) - i) > 1:
            teams.append(skills[:i])

    #note: might be good to use filter or reduce for this



def compare_team_sizes():

def check_for_sequential(skills):
    '''
    Further check after finding gaps.
    note: not sure if it's ok to have duplicates within a line if they're in separate groups, or not at all?

    main logic will go in here, I think.

    >>> check_for_sequential([1,2,3])
    True
    >>> check_for_sequential([2,4,6])
    False
    >>> check_for_sequential([-1,1,2])
    False

    :return:
    '''


def get_test_size(line, line_count):
    '''
    Read the first line of the input.
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
    Copy skill levels to a tuple to return later.
    :return:skills as list of x (ints)
    '''
    skills = ()
    for i in range(n):
        skills.append(int(line[i]))
    return skills


def sorted_skills(skills):
    '''
    Create temporary list to evaluate skill levels for grouping.
    :return: sorted (list of ints)
    '''
    return sorted(list(skills))

