dict_ = {}

t = int(input())

for i in range(t):
    name, number = input().split()
    dict_[name] = int(number)
    
while True:
    try:
        query = input()
        if query in dict_.keys():
            print("{}={}".format(query, dict_[query]))
        else:
            print("Not found")
    except EOFError:
        break
