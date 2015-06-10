__author__ = 'szeitlin'

#hypothesis seems like overkill in this case, just need to generate some stuff for testing edge cases

import random
import sys

test_cases = sys.argv[1]

with open(test_cases, 'w') as testdata:

    for i in range(50):
        sequence = [random.randint(0,200) for i in range(random.randint(0,50))]

        seq = ' '.join([str(x) for x in sequence])

        steps = random.randint(0,10)

        testdata.write(seq + " | " + str(steps) + '\n')
