import math
t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    total_product = math.prod(nums) 
    prefix_product = 1
    for i,num in enumerate(nums):
        total_product //= num
        prefix_product *= num
        if prefix_product == total_product:
            print(i+1)
            break
    else:
        print(-1)

        

        
