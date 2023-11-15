#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'is_palindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING word as parameter.
#

def is_palindrome(word):
    word = word.lower()
    word = word.replace(" ", "").replace(",", "").replace(".", "").replace("-", "").replace(":", "")
    
    palindrome = (word == word[::-1])
    return bool(palindrome)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    word = input()

    palindrome = is_palindrome(word)

    fptr.write(str(int(palindrome)) + '\n')

    fptr.close()
