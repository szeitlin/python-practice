__author__ = 'szeitlin'

# coding: utf-8
# merge two sorted lists
# 2nd half of merge sort

from collections import deque
import unittest


def merge_sorted_lists(left, right, stop, newlist):
    """ Two sorted lists as deques, any length, can be empty.
    Returns 1 sorted list

    :args left, right: deques
    :arg stop: int target length for final list
    :return newlist: list

    """
    print newlist
    print "newlist is now this long: " + str(len(newlist))



    while len(newlist) != stop:
        #print "newlist not full length yet"

        if list(left) != []:
            #print "left list not empty yet"
            if list(right) == []:
                 if len(left) > 0:
                     newlist.extend(left)
                     left = []
                     #print "left has been added to newlist and destroyed"

            elif left[0] <= right[0]:
                print "left is smaller than right"
                newlist.append(left.popleft())


        elif list(right) != []:
            #print "right list not empty yet"
            if list(left) == []:
                 if len(right) > 0:
                     newlist.extend(right)
                     right = []
                     #print "right has been added to newlist and destroyed"

            elif right[0] <= left[0]:
                #print "right is smaller than left"
                newlist.append(right.popleft())

        merge_sorted_lists(left, right, stop, newlist)

    if len(newlist) == stop:
        #print newlist
        return newlist

def prepare_to_merge(list1, list2):
    """ Convert lists and calculate stopping criteria.
    (2 lists) -> 2 deques, stop (int)
    """
    left = deque(list1)
    right = deque(list2)
    stop = len(left) + len(right)
    newlist = []
    return left, right, stop, newlist


class TestMerges(unittest.TestCase):
    def test_base_case(self):
        left, right, stop, newlist = prepare_to_merge([],[0])
        self.assertEqual(merge_sorted_lists(left,right,stop,newlist),[0])

    def test_equal_lengths(self):
        left, right, stop, newlist = prepare_to_merge([1, 2, 3], [4, 5, 6])
        self.assertEqual(merge_sorted_lists(left, right, stop, newlist), [1, 2, 3, 4, 5, 6])

    def test_one_list_shorter(self):
        left, right, stop, newlist = prepare_to_merge([0, 1], [2, 3, 4])
        self.assertEqual(merge_sorted_lists(left, right, stop, newlist), [0, 1, 2, 3, 4])

        left, right, stop, newlist = prepare_to_merge([0, 1, 2], [3, 4])
        self.assertEqual(merge_sorted_lists(left, right, stop, newlist), [0, 1, 2, 3, 4])

    def test_one_list_empty(self):
        left, right, stop, newlist = prepare_to_merge([], [0, 1, 2])
        self.assertEqual(merge_sorted_lists(left, right, stop, newlist), [0, 1, 2])

        left, right, stop, newlist = prepare_to_merge([0, 1, 2], [])
        self.assertEqual(merge_sorted_lists(left, right, stop, newlist), [0, 1, 2])

    def test_duplicate_entries_retained(self):
        left, right, stop, newlist = prepare_to_merge([0, 1, 1], [1, 2, 2])
        self.assertEqual(merge_sorted_lists(left, right, stop, newlist), [0, 1, 1, 1, 2, 2])



if __name__ == '__main__':
    unittest.main()