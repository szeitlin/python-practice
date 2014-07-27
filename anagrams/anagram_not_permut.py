__author__ = 'szeitlin'

import itertools
import re

def anagram(s):
    '''
    sentence as a (str) -> words with same chars & length as subset (at least 2 or more (str))
    ignore word that are not anagrams of other words in the sentence

    >>>anagram("I may opt for a top yam for amy")
    may yam amy
    opt top

    '''
    #assumption: keeping words as they are and just compare them, not find new words by scrambling letters around.

    p = re.compile(r'\W+')

    wordlist = p.split(s)

    permut_dict = {}
    for word in wordlist:
        permut_dict[word] = ["".join(x) for x in itertools.permutations(word, len(word))]

    for word in wordlist:
        if len(word) > 1:
            ana_list = []
            if word in permut_dict:
                ana_list = permut_dict[word]
                for item in ana_list:
                    if item not in wordlist:
                        ana_list.remove(item)
            print ana_list





    #group/remove duplicates & fix formatting?





anagram("Elvis lives in a dirty room dormitory")
#anagram("I may opt for a top yam for amy")