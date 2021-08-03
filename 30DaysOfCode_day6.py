t = int(input())

for i in range(t):
    s = input()
    even = ""
    odd = ""
    length = len(s)
    
    for i in range(0, length, 2):
        odd += s[i]
        
    for i in range(1, length, 2):
        even += s[i]
        
    print(odd, even)
    
