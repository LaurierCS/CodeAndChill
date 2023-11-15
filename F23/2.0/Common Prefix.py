#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'common_prefix' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY words as parameter.
#

def common_prefix(words):
    if not words:
        return ""

    # Sort the strings to ensure the common prefix is among the first and last strings
    words.sort()

    # Compare the first and last strings to find the common prefix
    first_str = words[0]
    last_str = words[-1]

    prefix = []
    for i in range(len(first_str)):
        if i < len(last_str) and first_str[i] == last_str[i]:
            prefix.append(first_str[i])
        else:
            break

    return ''.join(prefix)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = input().rstrip().split()

    result = common_prefix(arr)

    fptr.write(result + '\n')

    fptr.close()
