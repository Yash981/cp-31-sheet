t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    if n == 1:
        print(0)
    else:
        op = 0
        i = 0
        while i+1 < len(nums):
            if nums[i] % 2 == nums[i+1] % 2:
                nums[i+1] = nums[i] * nums[i+1]
                nums.pop(i)
                op += 1
                continue
            i += 1
        print(op)
            
        

