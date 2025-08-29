t = int(input())
for i in range(t):
    n = int(input())
    nums =  list(map(int,input().split()))
    res = 0
    zeroes = 0
    for i in range(n):
        if nums[i] == 0:
            zeroes += 1
        else:
            res = max(zeroes,res)
            zeroes = 0
    res = max(zeroes,res)
    print(res)
            
