#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'GradeSort' function below.
#
# The function accepts INTEGER_ARRAY grades as parameter.
#

def GradeSort(grades):
    n = len(grades)

    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            if grades[j] < grades[j+1]:
                grades[j], grades[j+1] = grades[j+1], grades[j]

if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = list(map(int, input().rstrip().split()))

    GradeSort(grades)

    print(' '.join(map(str, grades)))
