__author__ = 'szeitlin'

import collections
import re

def anagram(s):
    '''
    sentence as a (str) -> words with same chars & length as a subset of the original sentence (require at least 2 or more (str))
    ignore words that are not anagrams of other words in the sentence

    >>> anagram("Elvis has no lives on a dirty room dormitory floor")
    elvis lives
    no on

    >>> anagram("I may opt for a top yam for amy")
    may yam amy
    opt top

    '''
    #assumption: keeping words as they are and just compare them, not find new words by scrambling letters around.

    p = re.compile(r'\W+')

    wordlist = p.split(s)

    for i in range(len(wordlist)):
        wordlist[i] = wordlist[i].lower()

    word_freq = collections.defaultdict(int)

    for word in wordlist:
        if len(word) >1:
            char_freq = collections.defaultdict(int)
            for char in word:
                char_freq[char] +=1
            word_freq[word] = char_freq

    # seen = []
    #
    # for word, freq in word_freq.items():
    #     key = word_freq.pop(word)
    #     #print key
    #
    #     if key in word_freq.values():
    #         seen.extend([word, freq])
    #     elif key not in word_freq.values():
    #         if key in seen:
    #             seen.extend([word, freq])


    seen1 = {}
    seen2 = {}

    for word, freq in word_freq.items():
        key = word_freq.pop(word)
        #print key

        if key in word_freq.values():
            seen1.update({word:key})
        elif key not in word_freq.values():
            if key in seen1.values():
                seen2.update({word:key})


    # for i,v in seen.items():
    #     print i,v

    print seen1.keys(), seen2.keys()

#compare the two dicts by value to format output correctly




    # if len(seen) == 0:
    #     print "no anagrams in this sentence"
    # else:
    #     hit_string = " ".join(seen)
    #     print hit_string


# import doctest
# doctest.testmod()


#currently, returning them in same order as in the original sentence
#want to return the related words as separate strings

#also need to avoid counting repeats as 'matches' ("for" appears twice but is not an anagram)


anagram("Elvis has no lives on a dirty room dormitory floor")





