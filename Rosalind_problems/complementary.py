def complementary(s):
    '''
    (str) -> (str)

    Returns the reverse complementary strand of s.

    >>>complementary('AAACCCTTTGGG')
    CCCAAAGGGTTT

    '''

    reverse = s[::-1]

    old = 'ATCG'
    new = 'TAGC'
    lookatthis = str.maketrans(old, new)

    complement = reverse.translate(lookatthis)

    print(complement)

    
