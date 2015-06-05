__author__ = 'szeitlin'

#coding: utf-8

# """
# Write a program that prints out the final series of numbers where those divisible by X, Y
# and both are replaced by F for fizz, B for buzz and FB for fizz buzz.
#
# Your program should accept a file as its first argument.
#
# The file contains multiple separated lines; each line contains 3 numbers that are space delimited.
#
# The first number is the first divider (X), the second number is the second divider (Y),
# and the third number is how far you should count (N).
#
# You may assume that the input file is formatted correctly, and that the numbers are valid positive integers.
#
# example file:
# 3 5 10
# 2 7 15
#
# >>> fizzbuzz(file)
# 1 2 F 4 B F 7 8 F B
# 1 F 3 F 5 F B F 9 F 11 F 13 FB 15
#
# your output should print out one line per set. Ensure that there are no trailing empty spaces in each line you print.
#
# CONSTRAINTS:
#
# The number of test cases <= 20
# "X" is in range [1, 20]
# "Y" is in range [1, 20]
# "N" is in range [21, 100]
#
# """

def get_params(infile):
    """
    emits parameters for generating the sequence.

    :param infile: each line contains 3 numbers that are space delimited.
    :return: one list of parameters at a time
    """
    with open(infile, 'r') as infile:
        for line in infile:
            temp = line.split(' ')
            params = [int(x) for x in temp if len(x) < 4]
            if len(params) > 0:
                yield params


def make_list(infile):
    """
    Takes the params and generates the appropriate output list.

    :param params: comma-delimited list
    :return:
    """


    lines = get_params(infile)

    while lines:
        outlist = []
        try:
            params = next(lines)
            for i in range(1,params[2]+1):
                if i%params[0]==0 and i%params[1]==0:
                    outlist.append('FB')
                elif i%params[0] == 0:
                    outlist.append('F')
                elif i%params[1] == 0:
                    outlist.append('B')
                else:
                    outlist.append(i)
            print outlist

        except StopIteration:
            break





make_list("test1.txt")
