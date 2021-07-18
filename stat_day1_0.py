import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
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

    return median(L), median(data), median(U)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
