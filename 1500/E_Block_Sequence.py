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
#Normal 1d dp
# import sys
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))

#     dp = [0] * (n + 1)  # dp[n] = 0

#     for i in range(n - 1, -1, -1):
#         # Option 1: delete a[i]
#         dp[i] = dp[i + 1]

#         # Option 2: keep block starting at i
#         if i + a[i] < n:
#             dp[i] = max(dp[i], a[i] + 1 + dp[i + a[i] + 1])

#     # minimum deletions = total - kept
#     print(n - dp[0])