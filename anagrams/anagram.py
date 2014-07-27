__author__ = 'szeitlin'

import collections
import re

def anagram(s):
    '''
    sentence as a (str) -> words with same chars & length as a subset of the original sentence
    (require at least 2 or more letters)
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

#create a dict of word:char counts for each word

    word_freq = collections.defaultdict(int)

    for word in wordlist:
        if len(word) >1:
            char_freq = collections.defaultdict(int)
            for char in word:
                char_freq[char] +=1
            word_freq[word] = char_freq

#find anagrams by comparing char counts

    seen = {}

    for word, freq in word_freq.items():
        key = word_freq.pop(word)

        if key in word_freq.values():
            seen.update({word:key})
        elif key not in word_freq.values():
            if key in seen.values():
                seen.update({word:key})

#sort by values and output as a string

    result = sorted(seen.items(), key = lambda x: x[1]) #this returns tuples

    text = [x[0] for x in result] #just want the strings

    if len(text) == 0:
        print "no anagrams in this sentence"
    else:
        hit_string = " ".join(text)
        print hit_string


# import doctest
# doctest.testmod()

#ultimately, would want to return the related words together on separate lines

anagram("Elvis has no lives on a dirty room dormitory floor")

anagram("I may opt for a top yam for amy")




