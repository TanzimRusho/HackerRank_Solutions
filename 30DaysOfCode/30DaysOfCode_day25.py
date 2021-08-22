import math

t = int(input())

for i in range(t):
    n = int(input())
    
    if n == 1:
        print("Not prime")
        continue
    
    sq = math.sqrt(n)
    sq_ = int(sq) + 1
    flag = True 
    
    for j in range(2, sq_):
        if n % j == 0:
            flag = False
            
    if flag:
        print("Prime")
    else:
        print("Not prime")
