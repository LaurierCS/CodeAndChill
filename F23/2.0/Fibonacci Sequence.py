#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fibonacci' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER N as parameter.
#

def fibonacci(N):
    sequence = [0, 1]

    # Generate Fibonacci sequence up to the Nth term
    while len(sequence) < N:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence[:N]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    terms = fibonacci(N)

    fptr.write(' '.join(map(str, terms)))
    fptr.write('\n')

    # final returned output must be a list/array

    fptr.close()
