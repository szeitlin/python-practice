__author__ = 'szeitlin'

#example of dynamic programming problem

def longest_increasing_seq(ordered_list):
    """
    Given a list of N ordered integers, find the longest increasing
    subsequence in this list.

    :param ordered_list:
    :return: sub_list(s)

    >>> longest_increasing_seq([1,2,3,4])
    [1, 2, 3, 4]

    >>> longest_increasing_seq([16,3,5,19,10,14,12,0,15])
    [3,5,10,12,15]
    [3,5,10,14,15]

    >>> longest_increasing_seq([16,3,19,5,20,9,21,10])
    [16, 19, 20, 21]
    [3, 5, 9, 10]
    """
   #create sub-lists
    temp = []

    for i in range(len(ordered_list)):
        sub_list = [ordered_list[i]]

        for j in range(i, len(ordered_list)):

            if ordered_list[j] >= sub_list[-1]:
                sub_list.append(ordered_list[j])

        sub_list = sub_list[1:]
        #print(sub_list)


    #compare lengths of lists

        if len(sub_list) >= len(temp):
            longest = sub_list
            #print("the longest I've seen is:" + str(longest))
            temp = sub_list


    #don't forget to deal with case where there's more than one list of the same length

    #current version also won't work if there are negative numbers

            return longest

