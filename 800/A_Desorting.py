import math
t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    sorty = sorted(nums)
    if nums != sorted(nums):
        print(0)
    else:
        newList = []
        for j in range(n-1):
            newList.append((nums[j+1] - nums[j]) + 1)
        mn = min(newList)
        print(math.ceil(mn/2))
        
