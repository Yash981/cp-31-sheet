import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    intervals = []
    for i in range(n):
        if  n-(i+1) >= arr[i]:
            intervals.append([i,i+arr[i]])
    intervals.sort()
    m = len(intervals)
    if m == 0:
        print(n)
        continue
    def binary_search(start,x):
        l,r = start,m-1
        while l <= r:
            mid = (l+r)//2
            if intervals[mid][0] >= x:
                r = mid-1
            else:
                l = mid+1
        return l
    nextIndex = [0]*m
    for i in range(m):
        nextIndex[i] = binary_search(i+1,intervals[i][1]+1)
    # @lru_cache(None)
    # def dp(i):
    #     if i >= m:
    #         return 0
    #     return max((intervals[i][1]-intervals[i][0]+1) + dp(nextIndex[i]),dp(i+1))
    # res = dp(0)
    # dp.cache_clear()
    dp = [0] * (m + 1)  

    for i in range(m - 1, -1, -1):
        take = (intervals[i][1] - intervals[i][0] + 1) + dp[nextIndex[i]]
        skip = dp[i + 1]
        dp[i] = max(take, skip)

    res = dp[0]
    print(n-res)