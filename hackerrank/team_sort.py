__author__ = 'szeitlin'

#maybe easiest to take an OO approach and then instantiate lists each time?

import itertools

def count_teams():
    '''for each instance of Team, this will be a function to iterate the counter.'''
    team_count = itertools.count()
    return team_count

class Team(list):

    def __init__(self):
        pass

    def grab(self, member):
        self.append(member)


#for testing

# first = Team()
# first.grab(2)
# first.grab(1)
# print first
# first.sort()
# print first

#ideally, really want a method that actually grabs: append to new list and remove from skills list.

#could do del skills[index], or could just do pop in the first place (remember that pop holds onto the number for you)


def assign_teams(skills):
    """Iterates through list of skills ratings and groups according to contiguity.
    Key is to add members in order and then only add to either end, and if not, add to either
    a) either end of a different group, or b) a new group. Otherwise, you have to sort to make it easier to
    tell where a member can go.

    >>> assign_teams([6,1,5,4,1,0,-1,-5,-3,-4])
    [6,5,4], [1,0,-1], [1], [-3,-4,-5]

    """


#first time through is special (no teams yet)

    #instantiate a new list
    first = Team()

    #append the first number to it
    first.grab(skills[0])

    #check whether the second number belongs or not
    if abs(skills[1]-skills[0])==1:
        first.grab(skills[1])

    elif abs(skills[1]-skills[0])>1:
        #make a new team
        second = Team()
        second.grab(skills[1])
        second.sort()

#then iterate through the rest of the list

    #while some members not assigned yet:
        #check if they belong on an existing team
        #if yes, move them there, sort if necessary
        #if no, instantiate a new team and move them there instead
        #sort if necessary





def can_teams_merge(teams):
    """
    Takes the teams list of lists of ints, and checks whether any of them are contiguous.

    :param teams:
    :return:
    """
    pass