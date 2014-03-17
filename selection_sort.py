__author__ = 'szeitlin'

def selection_sort (seq):
    '''
    linear passes through a disordered sequence to restore order.
    On2 (not efficient for long lists)

    list (int) -> list (int)

    >>>selection_sort[2,3,4,7,6,5,1,8]
    [1,2,3,4,5,6,7,8]
    '''
    i = 0
    newseq = []
    while len(seq) > 0:
        j = min(seq)
        newseq.append(j)
        seq.remove(j)   #remove the item from the list, as opposed to pop(), which refers to the index

    print newseq

selection_sort([2,3,4,7,6,5,1,8])
