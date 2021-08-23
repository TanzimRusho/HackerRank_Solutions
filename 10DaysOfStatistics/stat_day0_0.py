# Hackerrank: 10 Days of Statistics: Day 0: Mean, Median, and Mode
# calculate mean, median, mode of a sequence of numbers

def mean(nums, length):
    return sum(nums) / length
    
def median(nums, length):
    nums = sorted(nums)
    
    if length % 2 != 0:
        return nums[length//2]
    else:
        return (nums[length//2] + nums[length//2 - 1])/2
    
def mode(nums, length):
    nums = sorted(nums)
    
    dict_ = {}
    
    for i in range(length):
        if nums[i] in dict_:
            dict_[nums[i]] += 1
        else:
            dict_[nums[i]] = 0
            
    return max(dict_, key=dict_.get)
            

def main():
    n = int(input()) 
    nums = [int(x) for x in input().split()]
    
    length = len(nums)

    print("{:.1f}".format(mean(nums, length)))
    print("{:.1f}".format(median(nums, length)))
    print("{}".format(mode(nums, length)))
    
if __name__ == "__main__":
    main()
