# Hackerrank: Day 1: Standard Deviation

import math
import os
import random
import re
import sys
import math

def stdDev(arr):
    length = len(arr)
    
    mean = sum(arr) / length
    
    print("{:.1f}".format(math.sqrt(sum([(arr[i] - mean)*(arr[i] - mean) 
        for i in range(length)])/length))) 


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
