# Hackerrank: 10 Days of Statistics: Day 1: Interquartile Range

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def median(data):
    data = sorted(data)
    length = len(data)

    len_half = length // 2
    
    if length % 2 != 0:
        return data[len_half]
    
    else:
        return int((data[len_half] + data[len_half - 1])/2)

def quartiles(data):
    data = sorted(data)
    length = len(data)

    mid = length // 2
       
    if length % 2 != 0:
        L = data[:mid]
        U = data[mid+1:]

    else:
        L = data[:mid] 
        U = data[mid:]

    return median(L), median(U)


def interQuartile(values, freqs):
    len_val = len(values)
    
    expanded_data = []
    
    for i in range(len_val):
        for j in range(freqs[i]):
            expanded_data.append(values[i])

    q1, q3 = quartiles(expanded_data)
    
    print("{:.1f}".format(q3-q1))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
