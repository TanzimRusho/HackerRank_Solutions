#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    binary = bin(n).replace("0b", "")
    
    count = 0
    count_instances = []
    length = len(binary)
    
    for i in range(1, length):
        if binary[i] == "1" and binary[i-1] == "1":
            count += 1
        if binary[i] == "0" and binary[i-1] == "1":
            count += 1
            count_instances.append(count)
            count = 0
        if i == length-1 and binary[i]=="1":
            count += 1
            count_instances.append(count)

    print(max(count_instances))
