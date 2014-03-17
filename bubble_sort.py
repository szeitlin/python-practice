__author__ = 'szeitlin'

def bubble_sort(seq):
    """ steps through the list, comparing each pair of items so that the lower ones "bubble" to the front.
        has n-squared efficiency, so it's slow for big lists.

    list (int) -> list (int)
    >>> bubble_sort([3,2,8,7,6,5,4,1])
    [1,2,3,4,5,6,7,8]
    """
    #identify first item and the item after it in the sequence

    i = 0

    #compare the items and swap them by using a temporary variable to hold one
    #e.g.  c = a, a = b, b = c

    #loop until counter reaches the beginning of the sequence

    while seq[0] != min(seq):
        for i in range (len(seq)-1):
            first_item = seq[i]
            next_item = seq[i + 1]

            if next_item < first_item:
                temp = next_item
                next_item = first_item
                first_item = temp
                seq[i] = first_item
                seq[i + 1] = next_item

                i += 1
            else:
                i += 1


    print seq
