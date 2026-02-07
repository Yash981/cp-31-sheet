t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    # @lru_cache(None)
    # def dp(i,turn):
    #     if i >= n:
    #         return 0
    #     ans = 1e9
    #     if turn:
    #         curr = 1 if arr[i] == 1 else 0
    #         ans = min(ans,curr + dp(i+1,not turn))
    #         curr += 1 if i+1 < n and arr[i+1] == 1 else 0
    #         ans = min(ans,curr + dp(i+2,not turn))
    #     else:
    #         ans = min(ans,dp(i+1,not turn),dp(i+2,not turn))
    #     return ans
    # res = dp(0,True)
    # dp.cache_clear()
    # print(res)
    dp = [[0]*2 for _ in range(n+2)] #1- friend turn, 0 - my turn
    for i in range(n-1,-1,-1):
        dp[i][1] = min((1 if arr[i] == 1 else 0) + dp[i+1][0],
                       (1 if arr[i] == 1 else 0) + (1 if i+1 < n and arr[i+1] == 1 else 0) + dp[i+2][0]) 
        dp[i][0] = min(dp[i+1][1],dp[i+2][1]) 
    print(dp[0][1]) #why dp[0][1] because first turn is of friend
