from itertools import accumulate
t = int(input())
for i in range(t):
    n,q = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    prefSum = list(accumulate(nums))
    prefSum.insert(0,0)
    for j in range(q):
        l,r,k = list(map(int,input().split()))
        TotalSum = k * (r-l+1)
        TotalSum += prefSum[l-1]-prefSum[0]
        TotalSum += prefSum[-1]-prefSum[r]
        print('YES' if TotalSum%2 else 'NO')            
            
        