__author__ = 'szeitlin'

def extractTags(fizzfoo):
    """
        str -> list of strings corresponding to bracketed tags in the string.

        >> extractTags('[fizz] thing [/fizz] fuzz [zip]')
        ['fizz', '/fizz', 'zip']
    """

    list = []
    word = ""
    i = 1
    for i in range(len(fizzfoo) + 1):
        if fizzfoo[i-1] == '[':
            word = ""
            while fizzfoo[i] != ']':
                word = word + fizzfoo[i]
                i += 1

            list.append(word)


    print list

extractTags('[fizz] thing')
extractTags('[fizz] thing [/fizz] fuzz [zip]')
